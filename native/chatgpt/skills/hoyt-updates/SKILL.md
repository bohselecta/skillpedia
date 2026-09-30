---
name: hoyt-updates
description: "Write a source-backed status update or shift handover with changes, risks and specific asks. Use for stakeholder updates; not a green-status narrative detached from evidence."
license: MIT
---

# Hoyt — Status & Handover
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Audience, reporting interval, actual milestone/issue state and relevant sources. Use the organization's format when supplied.

## Procedure
1. Identify what changed since the last verified update. Distinguish delivered behavior, ongoing work, planned work and unresolved evidence; do not repeat an old status as current.
2. Trace each consequential claim to implementation, owner confirmation or authoritative tracker state. Flag late, missing or contradictory sources and avoid invented percentage complete.
3. Write outcome first, then changes, risks/blockers, decisions/asks and next checkpoint. Use explicit owner/date status and impact. Apply real RAG or severity rules only when provided; otherwise use plain language.
4. Tailor detail to the reader without changing the factual claim. Remove process theater and unsupported optimism. Keep private details within the intended audience.
5. Prepare the message or handover artifact. Sending/publishing is a distinct approved action with resolved recipients and readback; a drafted update is not a delivered update.

## Deliverable
A concise update or handover, source-to-claim trail and exact asks.

## Acceptance
No unsupported green status, invented progress metric or silent removal of material risk; draft versus sent is explicit.

## Recovery and stopping
With incomplete evidence, publish only an accurately bounded draft and identify the smallest missing confirmation.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [records](references/records.md)
- [integrations](references/integrations.md)
- [travel context](references/travel-context.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Write a weekly stakeholder update from this verified work state.
- Paraphrase: Prepare a handover so the next person knows the decisions and blockers.
- Do not route here: Announce that all checks passed even though provider testing is missing.
- Failure case: A stale dashboard is green but the new error report is unresolved: include the conflict.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
