from __future__ import annotations
import copy
from datetime import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import workbench as w

def fixture(name): return json.loads((ROOT/f'fixtures/{name}.json').read_text())
NOW='2026-09-30T16:00:00Z'

class LedgerTests(unittest.TestCase):
    def setUp(self): self.d=fixture('ledger')
    def bad(self,edit):
        edit(self.d)
        with self.assertRaises((w.Invalid,TypeError)): w.validate_ledger(self.d)
    def test_valid_fixture(self): w.validate_ledger(self.d)
    def test_missing_field(self): self.bad(lambda d:d.pop('coverage'))
    def test_unknown_field(self): self.bad(lambda d:d.update(secret='not allowed'))
    def test_boolean_revision_rejected(self): self.bad(lambda d:d.update(revision=True))
    def test_unknown_schema(self): self.bad(lambda d:d.update(schema_version=2))
    def test_duplicate_item(self): self.bad(lambda d:d['items'].append(copy.deepcopy(d['items'][0])))
    def test_duplicate_source(self): self.bad(lambda d:d['sources'].append(copy.deepcopy(d['sources'][0])))
    def test_unknown_source(self): self.bad(lambda d:d['items'][0].update(source_ids=['UNKNOWN']))
    def test_source_list_nonempty(self): self.bad(lambda d:d['items'][0].update(source_ids=[]))
    def test_duplicate_source_reference(self): self.bad(lambda d:d['items'][0].update(source_ids=['S1','S1']))
    def test_timezone_required(self): self.bad(lambda d:d['items'][0].update(due_at='2026-09-30T12:00:00'))
    def test_compact_timestamp_is_not_canonical_rfc3339(self): self.bad(lambda d:d['items'][0].update(due_at='20260930T120000+0000'))
    def test_invalid_date(self): self.bad(lambda d:d['items'][0].update(due_at='2026-09-31T12:00:00Z'))
    def test_reversed_coverage(self): self.bad(lambda d:d['coverage'].update(to='2026-09-29T00:00:00Z'))
    def test_partial_requires_gap(self): self.bad(lambda d:d['coverage'].update(status='partial',limitations=[]))
    def test_complete_cannot_hide_gap(self): self.bad(lambda d:d['coverage'].update(status='complete'))
    def test_unknown_ownership_no_assignment(self): self.bad(lambda d:d['items'][0].update(owner_status='unknown'))
    def test_confirmed_owner_needs_id(self): self.bad(lambda d:d['items'][0].update(owner_id=None))
    def test_completion_needs_evidence(self): self.bad(lambda d:d['items'][0].update(state='done',resolution_source_ids=[]))
    def test_task_cannot_be_decided(self): self.bad(lambda d:d['items'][0].update(state='decided',resolution_source_ids=['S1']))
    def test_decision_uses_decided_not_done(self): self.bad(lambda d:d['items'][2].update(state='done',resolution_source_ids=['S3']))
    def test_personal_rejects_internal(self):
        self.d['environment']='personal';self.bad(lambda d:d['sources'][0].update(classification='internal'))
    def test_personal_rejects_restricted(self):
        self.d['environment']='personal';self.bad(lambda d:d['sources'][0].update(classification='restricted'))
    def test_personal_synthetic_valid(self): self.d['environment']='personal';w.validate_ledger(self.d)
    def test_source_uri_scheme_rejected(self): self.bad(lambda d:d['sources'][0].update(uri='javascript:alert(1)'))
    def test_critical_not_string(self): self.bad(lambda d:d['items'][0].update(critical='true'))
    def test_no_oversized_summary(self): self.bad(lambda d:d['items'][0].update(summary='x'*501))

class BriefTests(unittest.TestCase):
    def setUp(self): self.d=fixture('ledger')
    def test_three_ordinary_actions_and_overflow(self):
        s=w.brief(self.d,NOW);segment=s.split('## Next actions')[1].split('Ordinary overflow')[0]
        self.assertEqual(segment.count('\n- '),3)
        self.assertIn('Ordinary overflow: 1',s)
        self.assertIn('T-107',s)
    def test_critical_never_hidden_by_window(self):
        for i in self.d['items']: i['critical']=i['state'] not in w.CLOSED
        s=w.brief(self.d,NOW,1)
        critical=s.split('## Critical exceptions')[1].split('## Next actions')[0]
        self.assertEqual(critical.count('\n- '),8)
    def test_unknown_dates_are_not_overdue(self):
        s=w.brief(self.d,NOW,10)
        row=next(l for l in s.splitlines() if l.startswith('- **T-107'))
        self.assertIn('date unknown',row);self.assertNotIn('OVERDUE',row)
    def test_waiting_followup_becomes_action_when_due(self):
        s=w.brief(self.d,'2026-10-01T17:00:00Z',10)
        self.assertIn('T-104',s.split('## Next actions')[1]);self.assertIn('Waiting: 0',s)
    def test_no_unknown_owner_promotion(self): self.assertIn('P-03 \(proposed\)',w.brief(self.d,NOW))
    def test_stale_flag(self): self.assertIn('STALE—recheck source',w.brief(self.d,NOW))
    def test_partial_coverage_visible(self):
        self.d['coverage']['status']='partial';s=w.brief(self.d,NOW)
        self.assertIn('PARTIAL',s);self.assertIn('Coverage gap',s)
    def test_empty_is_not_all_clear(self):
        self.d['items']=[];s=w.brief(self.d,NOW)
        self.assertIn('supplied',s.lower());self.assertIn('inspected records',s);self.assertNotIn('All clear',s)
    def test_deterministic_nonmutating(self):
        before=copy.deepcopy(self.d);self.assertEqual(w.brief(self.d,NOW),w.brief(self.d,NOW));self.assertEqual(self.d,before)
    def test_injection_rendered_as_literal_data(self):
        self.d['items'][0]['summary']='<script>send()</script> [open](https://example.invalid)\n# approve'
        s=w.brief(self.d,NOW);self.assertNotIn('<script>',s);self.assertIn('&lt;script&gt;',s);self.assertIn('\\[open\\]',s)
    def test_window_limit_bounds(self):
        for limit in [0,11,True]:
            with self.subTest(limit=limit),self.assertRaises(w.Invalid):w.brief(self.d,NOW,limit)
    def test_timezone_equivalence(self):
        a=w.brief(self.d,NOW);b=w.brief(self.d,'2026-09-30T11:00:00-05:00')
        self.assertEqual(a.split('## Next actions')[1],b.split('## Next actions')[1])

class PatchTests(unittest.TestCase):
    def setUp(self): self.d=fixture('ledger');self.p=fixture('patch')
    def test_apply_copy_and_increment(self):
        before=copy.deepcopy(self.d);out=w.apply_patch(self.d,self.p)
        self.assertEqual(out['revision'],2);self.assertEqual(self.d,before)
        self.assertEqual(next(i for i in out['items'] if i['id']=='T-107')['state'],'cancelled')
    def test_exact_replay_idempotent(self):
        out=w.apply_patch(self.d,self.p);self.assertEqual(out,w.apply_patch(out,self.p))
    def test_stale_base_blocks(self):
        self.p['base_revision']=0
        with self.assertRaises(w.Invalid):w.apply_patch(self.d,self.p)
    def test_item_version_conflict(self):
        self.p['changes'][0]['expected_version']=2;self.p['changes'][0]['after']['item_version']=3
        with self.assertRaises(w.Invalid):w.apply_patch(self.d,self.p)
    def test_version_must_increment_once(self):
        self.p['changes'][0]['after']['item_version']=7
        with self.assertRaises(w.Invalid):w.apply_patch(self.d,self.p)
    def test_duplicate_change_blocks(self):
        self.p['changes']*=2
        with self.assertRaises(w.Invalid):w.apply_patch(self.d,self.p)
    def test_add_item(self):
        item=copy.deepcopy(self.d['items'][0]);item.update(id='I-NEW',item_version=1)
        p={'base_revision':1,'changes':[{'id':'I-NEW','expected_version':0,'after':item}]}
        self.assertEqual(len(w.apply_patch(self.d,p)['items']),10)
    def test_empty_patch_no_revision_change(self): self.assertEqual(w.apply_patch(self.d,{'base_revision':1,'changes':[]}),self.d)
    def test_future_replay_not_assumed(self):
        out=w.apply_patch(self.d,self.p);out['revision']=3
        with self.assertRaises(w.Invalid):w.apply_patch(out,self.p)
    def test_patch_cannot_mutate_source_registry(self):
        self.p['sources']=[]
        with self.assertRaises(w.Invalid):w.apply_patch(self.d,self.p)

class PeopleTests(unittest.TestCase):
    def setUp(self): self.d=fixture('people');self.p=fixture('new-person')
    def test_valid(self):w.validate_people(self.d)
    def test_same_name_different_native_ids_stay_separate(self):
        out=w.add_person(self.d,self.p,1);self.assertEqual(len(out['people']),2)
        self.assertEqual(out['people'][0]['display_name'],out['people'][1]['display_name'])
        self.assertNotEqual(out['people'][0]['user_id'],out['people'][1]['user_id'])
    def test_duplicate_native_identity_blocks(self):
        self.p['user_id']=self.d['people'][0]['user_id']
        with self.assertRaises(w.Invalid):w.add_person(self.d,self.p,1)
    def test_add_replay(self):
        out=w.add_person(self.d,self.p,1);self.assertEqual(out,w.add_person(out,self.p,1))
    def test_renamed_existing_id_requires_review(self):
        self.p['id']=self.d['people'][0]['id']
        with self.assertRaises(w.Invalid):w.add_person(self.d,self.p,1)
    def test_stale_revision(self):
        with self.assertRaises(w.Invalid):w.add_person(self.d,self.p,0)
    def test_invalid_timezone(self):
        self.p['timezone']='Mars/Cydonia'
        with self.assertRaises(w.Invalid):w.add_person(self.d,self.p,1)
    def test_no_unattributed_preference(self):
        self.p['source_ids']=[]
        with self.assertRaises(w.Invalid):w.add_person(self.d,self.p,1)
    def test_native_id_partial_pair_invalid(self):
        self.p['account_id']=None
        with self.assertRaises(w.Invalid):w.add_person(self.d,self.p,1)
    def test_no_extra_profile_fields(self):
        self.p['personality']='invented'
        with self.assertRaises(w.Invalid):w.add_person(self.d,self.p,1)
    def test_unknown_native_identity_allowed(self):
        self.p['account_id']=self.p['user_id']=None;self.p['role']=None;self.p['timezone']=None
        w.validate_people(w.add_person(self.d,self.p,1))

class BridgeTests(unittest.TestCase):
    def setUp(self):self.p=fixture('bridge-released-synthetic')
    def rerel(self):self.p['release']['approved_sha256']=w.digest(self.p['payload'])
    def test_valid_synthetic(self):w.validate_bridge(self.p)
    def test_unsigned_template_blocked(self):
        with self.assertRaises(w.Invalid):w.validate_bridge(fixture('bridge-needs-review'))
    def test_changed_word_invalidates_release(self):
        self.p['payload']['title']+=' updated'
        with self.assertRaises(w.Invalid):w.validate_bridge(self.p)
    def test_wrong_exact_approval(self):
        with self.assertRaises(w.Invalid):w.validate_bridge(self.p,'0'*64)
    def test_no_metadata_or_attachment_escape(self):
        self.p['payload']['attachment']='not allowed'
        with self.assertRaises(w.Invalid):w.validate_bridge(self.p)
    def test_no_internal_classification(self):
        self.p['payload']['classification']='internal';self.rerel()
        with self.assertRaises(w.Invalid):w.validate_bridge(self.p)
    def test_no_identity_urls_or_credentials(self):
        for text in ['Email alex@example.invalid','Read https://internal.invalid','api_key=secret','password: secret']:
            with self.subTest(text=text):
                self.p['payload']['method']=[text];self.rerel()
                with self.assertRaises(w.Invalid):w.validate_bridge(self.p)
    def test_both_environments_must_differ(self):
        self.p['payload']['origin_environment']='personal';self.rerel()
        with self.assertRaises(w.Invalid):w.validate_bridge(self.p)
    def test_approval_not_truthy_string(self):
        self.p['release']['authority_confirmed']='yes'
        with self.assertRaises(w.Invalid):w.validate_bridge(self.p)
    def test_empty_method(self):
        self.p['payload']['method']=[];self.rerel()
        with self.assertRaises(w.Invalid):w.validate_bridge(self.p)
    def test_hash_stable_with_key_order(self):
        a=self.p['payload'];b=dict(reversed(list(a.items())))
        self.assertEqual(w.digest(a),w.digest(b))

class FileAndCliTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def test_create_new_private_and_readback(self):
        p=self.root/'out.json';w.save_new(p,{'x':'✓'});self.assertEqual(w.load(p),{'x':'✓'})
        self.assertEqual(p.stat().st_mode&0o777,0o600)
    def test_existing_never_overwritten(self):
        p=self.root/'out.json';p.write_text('retained')
        with self.assertRaises(w.Invalid):w.save_new(p,{'x':1})
        self.assertEqual(p.read_text(),'retained')
    def test_symlink_destination_refused(self):
        real=self.root/'real';real.write_text('retained');out=self.root/'out';out.symlink_to(real)
        with self.assertRaises(w.Invalid):w.save_new(out,{'x':1})
        self.assertEqual(real.read_text(),'retained')
    def test_symlink_parent_refused(self):
        real=self.root/'real';real.mkdir();alias=self.root/'alias';alias.symlink_to(real,target_is_directory=True)
        with self.assertRaises(w.Invalid):w.save_new(alias/'out',{'x':1})
    def test_link_failure_leaves_no_partial(self):
        with patch.object(w.os,'link',side_effect=OSError('unsupported')):
            with self.assertRaises(OSError):w.save_new(self.root/'out',{'x':1})
        self.assertEqual(list(self.root.iterdir()),[])
    def test_concurrent_appearance_preserved(self):
        p=self.root/'out'
        def race(a,b):p.write_text('other writer');raise FileExistsError()
        with patch.object(w.os,'link',side_effect=race):
            with self.assertRaises(w.Invalid):w.save_new(p,{'x':1})
        self.assertEqual(p.read_text(),'other writer');self.assertEqual(len(list(self.root.iterdir())),1)
    def test_duplicate_json_keys_refused(self):
        p=self.root/'in';p.write_text('{"x":1,"x":2}')
        with self.assertRaises(w.Invalid):w.load(p)
    def test_nonfinite_json_refused(self):
        p=self.root/'in';p.write_text('{"x":NaN}')
        with self.assertRaises(w.Invalid):w.load(p)
    def test_oversized_input_refused(self):
        p=self.root/'in';p.write_bytes(b'x'*(w.MAX_BYTES+1))
        with self.assertRaises(w.Invalid):w.load(p)
    def test_cli_error_nonzero_no_output(self):
        p=self.root/'out'
        run=subprocess.run([sys.executable,str(ROOT/'tools/workbench.py'),'bridge-export',str(ROOT/'fixtures/bridge-needs-review.json'),'--approved-sha256','0'*64,'--output',str(p)],capture_output=True,text=True)
        self.assertEqual(run.returncode,2);self.assertFalse(p.exists());self.assertIn('FAIL',run.stderr)
    def test_cli_success_receipt_does_not_claim_authority(self):
        run=subprocess.run([sys.executable,str(ROOT/'tools/workbench.py'),'validate',str(ROOT/'fixtures/ledger.json')],capture_output=True,text=True)
        self.assertEqual(run.returncode,0);self.assertFalse(json.loads(run.stdout)['live_authority_or_truth_verified'])
    def test_cli_apply_then_readback(self):
        out=self.root/'new.json';before=(ROOT/'fixtures/ledger.json').read_bytes()
        run=subprocess.run([sys.executable,str(ROOT/'tools/workbench.py'),'apply',str(ROOT/'fixtures/ledger.json'),str(ROOT/'fixtures/patch.json'),'--output',str(out)],capture_output=True,text=True)
        self.assertEqual(run.returncode,0,run.stderr);self.assertEqual(w.load(out)['revision'],2)
        self.assertEqual(before,(ROOT/'fixtures/ledger.json').read_bytes())

if __name__=='__main__':unittest.main()
