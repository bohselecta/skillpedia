#!/usr/bin/env python3
"""Offline structural validation. Not a replacement for native platform validation."""
from __future__ import annotations
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile
import build

NAME=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
LINK=re.compile(r'\]\(([^)\s]+)\)')

def frontmatter(raw):
    text=raw.decode('utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]: raise ValueError('missing YAML frontmatter')
    header,body=text[4:].split('\n---\n',1);result={}
    for line in header.splitlines():
        key,sep,value=line.partition(':')
        if not sep or key in result: raise ValueError('bad/duplicate frontmatter key')
        value=value.strip()
        if key=='description': value=json.loads(value)
        elif value=='true': value=True
        result[key]=value
    if set(result)-{'name','description','license','disable-model-invocation'}: raise ValueError('unsupported frontmatter')
    if not NAME.fullmatch(result.get('name','')) or len(result['name'])>64: raise ValueError('invalid name')
    if not isinstance(result.get('description'),str) or not 20<=len(result['description'])<=1024: raise ValueError('invalid description')
    if result.get('license')!='MIT': raise ValueError('license missing')
    if len(body.splitlines())>=500: raise ValueError('skill too long')
    return result,body

def validate_skill(entries,expected_name=None):
    paths=[PurePosixPath(p) for p in entries]
    if not paths or any(p.is_absolute() or '..' in p.parts or '\\' in str(p) for p in paths): raise ValueError('unsafe archive path')
    roots={p.parts[0] for p in paths}
    if len(roots)!=1: raise ValueError('one top-level skill folder required')
    root=next(iter(roots));m=[p for p in paths if p.name=='SKILL.md']
    if len(m)!=1 or str(m[0])!=f'{root}/SKILL.md': raise ValueError('exactly one root SKILL.md required')
    meta,body=frontmatter(entries[str(m[0])])
    if meta['name']!=root or (expected_name and root!=expected_name): raise ValueError('name/folder mismatch')
    for name,data in entries.items():
        if name.endswith('.md'):
            for target in LINK.findall(data.decode()):
                if re.match(r'^(https?://|#)',target): continue
                target=target.split('#')[0]
                candidate=PurePosixPath(name).parent/target
                if '..' in candidate.parts or str(candidate) not in entries: raise ValueError(f'broken/nonlocal reference: {name} -> {target}')
    if 'allowed-tools:' in body or '!`' in body: raise ValueError('unexpected dynamic tool grant/execution')
    if sum(map(len,entries.values()))>25_000_000: raise ValueError('bundle exceeds conservative 25 MB bound')
    return meta

def validate_zip(raw):
    if len(raw)>25_000_000: raise ValueError('archive exceeds upload bound')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        infos=z.infolist()
        if len(infos)!=len({i.filename for i in infos}): raise ValueError('duplicate ZIP member')
        if any((i.external_attr>>16)&0o170000==0o120000 for i in infos): raise ValueError('symlink ZIP entry')
        if sum(i.file_size for i in infos)>25_000_000: raise ValueError('uncompressed bound exceeded')
        return validate_skill({i.filename:z.read(i) for i in infos if not i.is_dir()})

def validate_all():
    native=build.build(check=True)
    total=0
    for host in build.HOSTS:
        prefix=f'native/{host}/skills/'
        names={p[len(prefix):].split('/')[0] for p in native if p.startswith(prefix)}
        if len(names)!=(16 if host=='chatgpt' else 20): raise ValueError('wrong target count')
        for name in names:
            entries={p[len(prefix):]:b for p,b in native.items() if p.startswith(prefix+name+'/')}
            meta=validate_skill(entries,name)
            if host=='claude-code' and name=='bridge' and meta.get('disable-model-invocation') is not True: raise ValueError('bridge auto-invocation guard missing')
            total+=1
    zips=list((build.ROOT/'dist').glob('*/UPLOAD*/*.zip'))
    if len(zips)!=36: raise ValueError('wrong upload ZIP count')
    for p in zips: validate_zip(p.read_bytes())
    plugin=json.loads(native['native/claude-code/.claude-plugin/plugin.json'])
    if set(plugin)-{'name','version','description','author','repository','license'} or plugin['name']!='skillpedia': raise ValueError('invalid plugin manifest')
    market=json.loads((build.ROOT/'.claude-plugin/marketplace.json').read_text())
    if market['plugins'][0]['name']!=plugin['name'] or market['plugins'][0]['source']!='./native/claude-code': raise ValueError('marketplace source mismatch')
    if not (build.ROOT/market['plugins'][0]['source']).is_dir(): raise ValueError('missing plugin source')
    if (build.ROOT/'native/claude-code/hooks').exists() or (build.ROOT/'native/claude-code/.mcp.json').exists(): raise ValueError('unexpected execution/connector extension')
    return {'status':'PASS','native_skills':total,'individual_upload_zips':len(zips),'native_platform_validation':'NOT_RUN','model_behavior':'NOT_RUN'}
if __name__=='__main__':
    try: print(json.dumps(validate_all(),indent=2))
    except (ValueError,OSError,KeyError,zipfile.BadZipFile) as exc: print(f'FAIL: {exc}',file=sys.stderr);raise SystemExit(2)
