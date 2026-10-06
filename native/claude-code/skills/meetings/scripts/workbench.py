#!/usr/bin/env python3
"""Local, standard-library helpers. No network, model calls or connector mutations.

Checks prove format/consistency, not truth, identity, authorization or declassification.
All file writes are explicit, private-mode and create-only; existing output is refused.
"""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timedelta
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

MAX_BYTES = 2_000_000
STATES = {'proposed', 'needs_action', 'waiting', 'blocked', 'decided', 'done', 'cancelled'}
KINDS = {'task', 'issue', 'risk', 'decision', 'note'}
CLASSES = {'public', 'personal', 'internal', 'restricted', 'synthetic'}
CLOSED = {'done', 'decided', 'cancelled'}
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_.:-]{0,79}$')
class Invalid(ValueError):
    """Invalid or unsafe local input; callers should not silently repair it."""

def fail(message: str) -> None:
    raise Invalid(message)

def keys(obj: Any, required: set[str], optional: set[str] | None = None, label: str = 'object') -> None:
    if not isinstance(obj, dict): fail(f'{label}: expected object')
    missing = required - obj.keys()
    extra = obj.keys() - required - (optional or set())
    if missing: fail(f'{label}: missing fields {sorted(missing)}')
    if extra: fail(f'{label}: unsupported fields {sorted(extra)}')

def text(value: Any, label: str, limit: int = 2000, empty: bool = False) -> str:
    if not isinstance(value, str) or len(value) > limit or (not empty and not value.strip()):
        fail(f'{label}: expected nonempty text up to {limit} characters')
    if any(ord(c) < 32 and c not in '\n\t' for c in value): fail(f'{label}: control characters')
    return value

def ident(value: Any, label: str) -> str:
    if not isinstance(value, str) or not ID.fullmatch(value): fail(f'{label}: invalid identifier')
    return value

def integer(value: Any, label: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum: fail(f'{label}: expected integer >= {minimum}')
    return value

def stamp(value: Any, label: str = 'timestamp') -> datetime:
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})', value):
        fail(f'{label}: RFC3339 timestamp with timezone/offset required')
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        fail(f'{label}: invalid ISO timestamp')
    if parsed.tzinfo is None or parsed.utcoffset() is None: fail(f'{label}: timezone/offset required')
    return parsed

def array(value: Any, label: str, limit: int = 10000) -> list:
    if not isinstance(value, list) or len(value) > limit: fail(f'{label}: expected bounded list')
    return value

def source_list(value: Any, known: set[str], label: str, nonempty: bool = False) -> None:
    v = array(value, label)
    for item in v: ident(item, label)
    if len(set(v)) != len(v): fail(f'{label}: duplicate source ID')
    if set(v) - known: fail(f'{label}: unknown source ID')
    if nonempty and not v: fail(f'{label}: evidence required')

def _unique_pairs(pairs: list[tuple[str, Any]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        if key in result: fail('JSON contains a duplicate key')
        result[key] = value
    return result

def load(path: str | Path) -> Any:
    p = Path(path)
    if p.stat().st_size > MAX_BYTES: fail('input exceeds 2 MB local helper limit')
    raw = p.read_bytes()
    if len(raw) > MAX_BYTES: fail('input exceeds 2 MB local helper limit')
    try:
        return json.loads(raw.decode('utf-8'), object_pairs_hook=_unique_pairs,
                          parse_constant=lambda _: fail('non-finite JSON number'))
    except (UnicodeError, json.JSONDecodeError) as exc:
        fail(f'invalid UTF-8 JSON: {type(exc).__name__}')

def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode('utf-8')

def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()

def save_new(path: str | Path, value: Any) -> None:
    """Atomic no-clobber publication using a same-directory hard link.

    Refuses symlink destinations/parents. Not a sandbox against hostile races.
    Does not create directories or replace existing state. Unsupported hard links
    cause a safe failure rather than falling back to an overwrite.
    """
    p = Path(path).absolute()
    if any(q.is_symlink() for q in [p, *p.parents]): fail('symlink output path refused')
    if not p.parent.is_dir(): fail('output parent must already exist')
    if p.exists(): fail('output exists; choose a new path and retain prior state')
    raw = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False).encode('utf-8') + b'\n'
    if len(raw) > MAX_BYTES: fail('output exceeds 2 MB local helper limit')
    fd, temporary = tempfile.mkstemp(prefix='.skillpedia-', dir=p.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        try: os.link(temporary, p)
        except FileExistsError: fail('output appeared concurrently; no replacement performed')
    finally:
        if os.path.exists(temporary): os.unlink(temporary)

def validate_sources(sources: Any, environment: str) -> set[str]:
    known: set[str] = set()
    for i, source in enumerate(array(sources, 'sources')):
        lab = f'sources[{i}]'
        keys(source, {'id','account','uri','timestamp','classification'}, label=lab)
        sid = ident(source['id'], lab)
        if sid in known: fail('duplicate source ID')
        known.add(sid)
        text(source['account'], lab, 200)
        uri = text(source['uri'], lab, 2000)
        if not re.match(r'^(https://|urn:|user:)', uri): fail(f'{lab}: unsupported source URI scheme')
        stamp(source['timestamp'], lab)
        if source['classification'] not in CLASSES: fail(f'{lab}: unknown classification')
        if environment == 'personal' and source['classification'] in {'internal','restricted'}:
            fail('corporate source is not permitted in a personal ledger')
    return known

def validate_item(item: Any, known: set[str]) -> None:
    fields = {'id','item_version','kind','summary','state','owner_id','owner_status','due_at',
              'follow_up_at','critical','source_ids','resolution_source_ids','next_action','checked_at'}
    keys(item, fields, label='work item')
    ident(item['id'], 'item.id'); integer(item['item_version'],'item_version',1)
    if item['kind'] not in KINDS: fail('unknown item kind')
    if item['state'] not in STATES: fail('unknown work state')
    text(item['summary'], 'summary', 500)
    text(item['next_action'], 'next_action', 500, empty=True)
    if item['owner_status'] not in {'unknown','proposed','confirmed'}: fail('unknown owner status')
    if item['owner_id'] is not None: ident(item['owner_id'], 'owner_id')
    if item['owner_status'] in {'proposed','confirmed'} and item['owner_id'] is None:
        fail('proposed/confirmed owner requires an ID')
    if item['owner_status'] == 'unknown' and item['owner_id'] is not None:
        fail('unknown ownership must not carry an assigned owner')
    if type(item['critical']) is not bool: fail('critical must be boolean')
    for field in ['due_at','follow_up_at']:
        if item[field] is not None: stamp(item[field], field)
    stamp(item['checked_at'], 'checked_at')
    source_list(item['source_ids'], known, 'source_ids', nonempty=True)
    source_list(item['resolution_source_ids'], known, 'resolution_source_ids', nonempty=item['state'] in {'done','decided'})
    if item['state'] == 'decided' and item['kind'] != 'decision': fail('only a decision may be decided')
    if item['kind'] == 'decision' and item['state'] == 'done': fail('use decided for a decision, with evidence')

def validate_ledger(data: Any) -> None:
    keys(data, {'schema_version','revision','environment','coverage','sources','items'})
    if type(data['schema_version']) is not int or data['schema_version'] != 1: fail('unsupported ledger schema')
    integer(data['revision'],'revision')
    if data['environment'] not in {'personal','corporate'}: fail('invalid environment')
    c = data['coverage']
    keys(c, {'status','scope','from','to','retrieved_at','limitations'}, label='coverage')
    if c['status'] not in {'complete','partial','supplied-only'}: fail('unknown coverage status')
    text(c['scope'],'coverage.scope',1000)
    start, end = stamp(c['from']), stamp(c['to'])
    if end < start: fail('coverage ends before it starts')
    stamp(c['retrieved_at'])
    for limitation in array(c['limitations'],'coverage.limitations',100): text(limitation,'limitation')
    if c['status'] == 'complete' and c['limitations']: fail('complete coverage cannot contain unaddressed limitations')
    if c['status'] != 'complete' and not c['limitations']: fail('partial coverage needs a limitation')
    known = validate_sources(data['sources'], data['environment'])
    ids = set()
    for item in array(data['items'],'items'):
        validate_item(item,known)
        if item['id'] in ids: fail('duplicate item ID')
        ids.add(item['id'])

def markdown(value: Any) -> str:
    s = str(value).replace('\n',' ').replace('\r',' ').replace('<','&lt;').replace('>','&gt;')
    return re.sub(r'([\\`*_{}\[\]()|#!])', r'\\\1', s)

def brief(data: dict, now: str, limit: int = 3) -> str:
    validate_ledger(data)
    current = stamp(now)
    integer(limit,'limit',1)
    if limit > 10: fail('ordinary attention window cannot exceed 10')
    counts = {'Waiting':0,'Needs decision':0,'Watch':0,'Done':0,'Cancelled':0}
    active, critical = [], []
    for item in data['items']:
        state = item['state']
        if state in CLOSED:
            counts['Cancelled' if state == 'cancelled' else 'Done'] += 1
            continue
        overdue = item['due_at'] is not None and stamp(item['due_at']) < current
        check_due = item['follow_up_at'] is not None and stamp(item['follow_up_at']) <= current
        if item['kind'] == 'decision': counts['Needs decision'] += 1
        if item['critical']:
            critical.append(item)
        elif item['kind'] == 'note': counts['Watch'] += 1
        elif state == 'waiting' and not check_due and not overdue: counts['Waiting'] += 1
        elif item['kind'] == 'risk' and not item['next_action']: counts['Watch'] += 1
        else: active.append(item)
    def order(item: dict) -> tuple:
        due = stamp(item['due_at']) if item['due_at'] else None
        overdue = due is not None and due < current
        soon = due is not None and due <= current + timedelta(hours=24)
        return (not overdue, item['state'] != 'blocked', item['kind'] != 'decision', not soon,
                due.timestamp() if due else float('inf'), item['id'])
    active.sort(key=order); critical.sort(key=order)
    c=data['coverage']
    out=['# Attention Window',f'As of {markdown(now)} · revision {data["revision"]} · {data["environment"]}',
         f'Coverage: **{c["status"].upper()}** — {markdown(c["scope"])}',
         f'Window examined: {markdown(c["from"])} to {markdown(c["to"])}. Retrieved: {markdown(c["retrieved_at"])}.']
    for gap in c['limitations']: out.append(f'Coverage gap: {markdown(gap)}')
    def row(item: dict) -> str:
        if item['due_at'] is None: date='date unknown'
        elif stamp(item['due_at']) < current: date=f'OVERDUE ({item["due_at"]})'
        else: date=f'due {item["due_at"]}'
        owner=f'{item["owner_id"] or "unassigned"} ({item["owner_status"]})'
        old= current - stamp(item['checked_at']) > timedelta(hours=48)
        stale=' · STALE—recheck source' if old else ''
        action=item['next_action'] or 'Clarify the next action'
        return f'- **{markdown(item["id"])} · {markdown(action)}** — {markdown(item["summary"])}; {markdown(owner)}; {markdown(date)}; sources {markdown(", ".join(item["source_ids"]))}{stale}'
    if critical:
        out.extend(['','## Critical exceptions — all shown'])
        out.extend(row(i) for i in critical)
    out.extend(['','## Next actions'])
    out.extend([row(i) for i in active[:limit]] or ['No ordinary next action is supported by the inspected records.'])
    out.append(f'\nOrdinary overflow: {max(0,len(active)-limit)}. Retained IDs: '+(', '.join(markdown(i['id']) for i in active[limit:]) or 'none')+'.')
    out.append(' · '.join(f'{k}: {v}' for k,v in counts.items()))
    out.append('\nRead-only brief. Nothing was sent, assigned, archived, scheduled or marked complete. Counts may overlap for unresolved decisions; completion applies only to inspected scope.')
    return '\n'.join(out)+'\n'

def apply_patch(data: dict, patch: dict) -> dict:
    validate_ledger(data)
    keys(patch, {'base_revision','changes'})
    base = integer(patch['base_revision'],'base_revision')
    changes=array(patch['changes'],'changes')
    if not changes: return copy.deepcopy(data) if data['revision']==base else fail('stale base revision')
    by_id={i['id']:i for i in data['items']}
    seen=set()
    for c in changes:
        keys(c,{'id','expected_version','after'},label='change')
        ident(c['id'],'change.id'); integer(c['expected_version'],'expected_version')
        if c['id'] in seen: fail('duplicate changed ID')
        seen.add(c['id'])
        validate_item(c['after'],{s['id'] for s in data['sources']})
        if c['after']['id']!=c['id']: fail('change ID mismatch')
        if c['after']['item_version']!=c['expected_version']+1: fail('item version must increment exactly once')
    # Exact replay of the immediately previous patch is a no-op, not a second update.
    if data['revision']==base+1 and all(by_id.get(c['id'])==c['after'] for c in changes):
        return copy.deepcopy(data)
    if data['revision']!=base: fail('stale base revision; reconcile concurrent work')
    result=copy.deepcopy(data)
    index={i['id']:n for n,i in enumerate(result['items'])}
    for c in changes:
        old=by_id.get(c['id'])
        if (old['item_version'] if old else 0)!=c['expected_version']: fail('item version conflict')
        if c['id'] in index: result['items'][index[c['id']]]=copy.deepcopy(c['after'])
        else: result['items'].append(copy.deepcopy(c['after']))
    result['revision']+=1
    validate_ledger(result)
    return result

def validate_people(data: Any) -> None:
    keys(data,{'schema_version','revision','environment','sources','people'})
    if type(data['schema_version']) is not int or data['schema_version']!=1: fail('unsupported people schema')
    integer(data['revision'],'revision')
    if data['environment'] not in {'personal','corporate'}: fail('invalid environment')
    known=validate_sources(data['sources'],data['environment'])
    ids, accounts=set(),set()
    for person in array(data['people'],'people'):
        keys(person,{'id','display_name','role','account_id','user_id','timezone','preferences','source_ids','reviewed_at'})
        pid=ident(person['id'],'person.id')
        if pid in ids: fail('duplicate person ID')
        ids.add(pid); text(person['display_name'],'display_name',100)
        if person['role'] is not None: text(person['role'],'role',200)
        account,user=person['account_id'],person['user_id']
        if (account is None)!=(user is None): fail('native identity needs both account_id and user_id')
        if account is not None:
            text(account,'account_id',200);text(user,'user_id',200)
            if (account,user) in accounts: fail('native identity collision; do not merge automatically')
            accounts.add((account,user))
        if person['timezone'] is not None:
            try: ZoneInfo(text(person['timezone'],'timezone',100))
            except ZoneInfoNotFoundError: fail('unknown timezone')
        for pref in array(person['preferences'],'preferences',20): text(pref,'preference',500)
        source_list(person['source_ids'],known,'person.source_ids',nonempty=True)
        stamp(person['reviewed_at'])

def add_person(data: dict, person: dict, expected_revision: int) -> dict:
    validate_people(data); integer(expected_revision,'expected_revision')
    existing=next((p for p in data['people'] if p['id']==person.get('id')),None)
    if data['revision']==expected_revision+1 and existing==person: return copy.deepcopy(data)
    if data['revision']!=expected_revision: fail('people revision conflict')
    if existing is not None: fail('person ID exists; prepare an explicit reviewed correction')
    result=copy.deepcopy(data);result['people'].append(copy.deepcopy(person));result['revision']+=1
    validate_people(result)
    return result

def validate_bridge(packet: Any, approved_sha256: str | None = None) -> None:
    keys(packet,{'payload','release'})
    p=packet['payload']; r=packet['release']
    keys(p,{'schema_version','kind','title','method','classification','origin_environment','destination_environment'}, label='bridge payload')
    if type(p['schema_version']) is not int or p['schema_version']!=1 or p['kind']!='reusable-method': fail('unsupported bridge format')
    if p['classification']!='public': fail('only explicitly released public methods may bridge')
    if {p['origin_environment'],p['destination_environment']}!={'personal','corporate'}: fail('bridge requires distinct personal/corporate environments')
    text(p['title'],'title',160)
    methods=array(p['method'],'method',12)
    if not methods: fail('method must not be empty')
    for step in methods: text(step,'method step',600)
    combined=' '.join([p['title'],*methods])
    if re.search(r'https?://|www\.|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|(?:password|api[_ -]?key|access[_ -]?token)\s*[:=]\s*\S+',combined,re.I):
        fail('obvious identifier/URL/credential pattern; generic methods only')
    keys(r,{'reviewed','authority_confirmed','approved_sha256','reviewed_at'},label='release')
    if r['reviewed'] is not True or r['authority_confirmed'] is not True: fail('explicit human release review and authority required')
    stamp(r['reviewed_at'])
    if r['approved_sha256']!=digest(p): fail('payload changed or digest mismatch; review again')
    if approved_sha256 is not None and approved_sha256!=digest(p): fail('supplied approval digest mismatch')

def cli() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    for name in ['validate','people-validate','bridge-check','bridge-digest']:
        cmd=sub.add_parser(name);cmd.add_argument('input')
    cmd=sub.add_parser('brief');cmd.add_argument('input');cmd.add_argument('--now',required=True);cmd.add_argument('--limit',type=int,default=3)
    cmd=sub.add_parser('apply');cmd.add_argument('input');cmd.add_argument('patch');cmd.add_argument('--output',required=True)
    cmd=sub.add_parser('people-add');cmd.add_argument('input');cmd.add_argument('person');cmd.add_argument('--expected-revision',type=int,required=True);cmd.add_argument('--output',required=True)
    cmd=sub.add_parser('bridge-export');cmd.add_argument('input');cmd.add_argument('--approved-sha256',required=True);cmd.add_argument('--output',required=True)
    args=parser.parse_args()
    try:
        data=load(args.input)
        if args.command=='validate': validate_ledger(data)
        elif args.command=='people-validate': validate_people(data)
        elif args.command=='bridge-check': validate_bridge(data)
        elif args.command=='bridge-digest':
            keys(data,{'payload','release'});print(digest(data['payload']));return 0
        elif args.command=='brief': print(brief(data,args.now,args.limit),end='');return 0
        elif args.command=='apply': save_new(args.output,apply_patch(data,load(args.patch)))
        elif args.command=='people-add': save_new(args.output,add_person(data,load(args.person),args.expected_revision))
        elif args.command=='bridge-export': validate_bridge(data,args.approved_sha256);save_new(args.output,data)
        print(json.dumps({'status':'PASS','check':'local format/consistency only','command':args.command,'live_authority_or_truth_verified':False}))
        return 0
    except (Invalid,OSError,TypeError,KeyError,ValueError) as exc:
        print(json.dumps({'status':'FAIL','error':str(exc)}),file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(cli())
