from __future__ import annotations
import contextlib
import copy
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import build
import validate
import workbench

class PackagingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.native=build.expected_native();cls.dist=build.distribution(cls.native)
    def test_counts_and_namespaces(self):
        m=json.loads(self.native['native/MANIFEST.json'])
        self.assertEqual(len(m['targets']['chatgpt']),16)
        self.assertEqual(len(m['targets']['claude-chat']),20)
        self.assertEqual(len(m['targets']['claude-code']),20)
        self.assertTrue(all(n.startswith('hoyt-') for n in m['targets']['chatgpt']))
    def test_all_skill_metadata_and_links(self):
        for host in build.HOSTS:
            prefix=f'native/{host}/skills/'
            names={p[len(prefix):].split('/')[0] for p in self.native if p.startswith(prefix)}
            for n in names:
                with self.subTest(host=host,name=n):
                    entries={p[len(prefix):]:b for p,b in self.native.items() if p.startswith(prefix+n+'/')}
                    self.assertEqual(validate.validate_skill(entries)['name'],n)
    def test_frontmatter_is_valid_yaml_with_real_parser(self):
        try:import yaml
        except ImportError:self.skipTest('optional PyYAML parser unavailable; strict generated-format parser still runs')
        for p,b in self.native.items():
            if p.endswith('/SKILL.md'):
                header=b.decode().split('---\n')[1]
                data=yaml.safe_load(header)
                self.assertEqual(data['name'],Path(p).parent.name)
    def test_descriptions_are_unique(self):
        c=json.loads((ROOT/'src/catalog.json').read_text())
        self.assertEqual(len({s['description'] for s in c['skills']}),20)
    def test_every_skill_has_boundary_cases(self):
        c=json.loads((ROOT/'src/catalog.json').read_text())
        for s in c['skills']:
            self.assertEqual(set(s['examples']),{'normal','paraphrase','near_miss','failure'})
            self.assertGreaterEqual(len(s['steps']),5)
    def test_archive_determinism(self):self.assertEqual(self.dist,build.distribution(build.expected_native()))
    def test_archive_counts_and_size(self):
        uploads={p:b for p,b in self.dist.items() if '/UPLOAD_' in p}
        self.assertEqual(len(uploads),36)
        for p,b in uploads.items():
            with self.subTest(path=p):validate.validate_zip(b);self.assertLess(len(b),25_000_000)
    def test_every_upload_runs_helper_in_isolation(self):
        for path,raw in self.dist.items():
            if '/UPLOAD_' not in path:continue
            with self.subTest(path=path),tempfile.TemporaryDirectory() as d:
                z=zipfile.ZipFile(io.BytesIO(raw));validate.validate_zip(raw);z.extractall(d)
                root=next(Path(d).iterdir());script=root/'scripts/workbench.py'
                result=subprocess.run([sys.executable,str(script),'validate',str(root/'assets/ledger.example.json')],cwd=d,capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertFalse(json.loads(result.stdout)['live_authority_or_truth_verified'])
    def test_carrier_not_accepted_as_single_skill(self):
        for p,b in self.dist.items():
            if '/UPLOAD_' not in p:
                with self.subTest(path=p),self.assertRaises(ValueError):validate.validate_zip(b)
    def test_carrier_checksums_and_nested_uploads(self):
        for path,raw in self.dist.items():
            if '/UPLOAD_' in path:continue
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                root=Path(z.namelist()[0]).parts[0]
                sums=z.read(root+'/SHA256SUMS.txt').decode().splitlines()
                for line in sums:
                    expected,p=line.split('  ',1);self.assertEqual(hashlib.sha256(z.read(root+'/'+p)).hexdigest(),expected)
                self.assertIn(root+'/README-UNZIP-FIRST.md',z.namelist())
                cases=json.loads(z.read(root+'/cases.json'))['cases']
                self.assertEqual(len(cases),80 if 'hoyt-' in path else 100)
                self.assertIn(root+'/results-template.json',z.namelist())
    def test_no_code_permission_grants_or_hooks(self):
        plugin=json.loads(self.native['native/claude-code/.claude-plugin/plugin.json'])
        self.assertEqual(set(plugin),{'name','version','description','author','repository','license'})
        for p,b in self.native.items():
            self.assertNotIn('/hooks/',p);self.assertNotIn('.mcp.json',p)
            if p.endswith('SKILL.md'):self.assertNotIn('\nallowed-tools:',b.decode());self.assertNotIn('!`',b.decode())
    def test_bridge_is_user_invoked_only_in_code(self):
        meta,_=validate.frontmatter(self.native['native/claude-code/skills/bridge/SKILL.md'])
        self.assertIs(meta['disable-model-invocation'],True)
    def test_readonly_reviewer_actual_tool_allowlist(self):
        s=self.native['native/claude-code/agents/evidence-reviewer.md'].decode()
        self.assertIn('tools: Read, Grep, Glob',s);self.assertIn('maxTurns: 8',s)
        self.assertNotIn('Bash',s);self.assertNotIn('Write',s)
    def test_all_bridge_templates_block_without_review(self):
        for p,b in self.native.items():
            if p.endswith('assets/bridge.template.json'):
                with self.subTest(path=p),self.assertRaises(workbench.Invalid):workbench.validate_bridge(json.loads(b))
    def test_personal_examples_do_not_contain_internal_sources(self):
        for p,b in self.native.items():
            if p.startswith('native/chatgpt/') and p.endswith('ledger.example.json'):
                data=json.loads(b);self.assertEqual(data['environment'],'personal');workbench.validate_ledger(data)
    def test_schema_fixtures_with_official_jsonschema_library(self):
        try:import jsonschema
        except ImportError:self.skipTest('optional jsonschema validation unavailable; runtime invariants tested separately')
        for name,fixture in [('ledger','ledger'),('people','people'),('bridge','bridge-released-synthetic'),('patch','patch'),('action-receipt','action-receipt')]:
            with self.subTest(name=name):
                schema=json.loads((ROOT/f'schemas/{name}.schema.json').read_text());jsonschema.Draft202012Validator.check_schema(schema)
                jsonschema.Draft202012Validator(schema,format_checker=jsonschema.FormatChecker()).validate(json.loads((ROOT/f'fixtures/{fixture}.json').read_text()))
    def test_malformed_zip_rejected(self):
        for entries in [ {'bad/SKILL.md':b'no YAML'}, {'a/SKILL.md':b'', 'b/SKILL.md':b''}, {'../escape':b'x'} ]:
            with self.subTest(entries=list(entries)),self.assertRaises(ValueError):validate.validate_skill(entries)
    def test_missing_reference_rejected(self):
        prefix='native/chatgpt/skills/'
        entries={p[len(prefix):]:b for p,b in self.native.items() if p.startswith(prefix+'hoyt-start/')}
        del entries['hoyt-start/references/records.md']
        with self.assertRaises(ValueError):validate.validate_skill(entries)
    def test_duplicate_zip_members_rejected(self):
        out=io.BytesIO()
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            with zipfile.ZipFile(out,'w') as z:z.writestr('a/SKILL.md','x');z.writestr('a/SKILL.md','y')
        with self.assertRaises(ValueError):validate.validate_zip(out.getvalue())
    def test_symlink_zip_refused(self):
        out=io.BytesIO()
        with zipfile.ZipFile(out,'w') as z:
            i=zipfile.ZipInfo('a/link');i.create_system=3;i.external_attr=0o120777<<16;z.writestr(i,'/tmp/elsewhere')
        with self.assertRaises(ValueError):validate.validate_zip(out.getvalue())
    def test_package_names_match_code_marketplace(self):
        p=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
        self.assertEqual(p['plugins'][0]['source'],'./native/claude-code')
        self.assertEqual(p['plugins'][0]['name'],'skillpedia')
    def test_generated_edits_are_not_silently_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            dest=Path(d)
            for name in ['src','fixtures','schemas','tools']:
                shutil.copytree(ROOT/name,dest/name,ignore=shutil.ignore_patterns('__pycache__'))
            for name in ['VERSION','LICENSE']:shutil.copy(ROOT/name,dest/name)
            with patch.object(build,'ROOT',dest):
                build.sync_native();p=dest/'native/chatgpt/skills/hoyt-start/SKILL.md';p.write_text(p.read_text()+'\nmy changes\n')
                with self.assertRaises(ValueError):build.sync_native()
                self.assertTrue(p.read_text().endswith('my changes\n'))
    def test_clean_copy_rebuild_equivalence(self):
        with tempfile.TemporaryDirectory() as d:
            dest=Path(d)
            for name in ['src','fixtures','schemas','tools','docs','evals']:
                shutil.copytree(ROOT/name,dest/name,ignore=shutil.ignore_patterns('__pycache__'))
            for name in ['VERSION','LICENSE','SECURITY.md']:shutil.copy(ROOT/name,dest/name)
            with patch.object(build,'ROOT',dest):
                n=build.build();self.assertEqual(n,self.native)
                rebuilt=build.distribution(n);self.assertEqual(rebuilt,self.dist)

if __name__=='__main__':unittest.main()
