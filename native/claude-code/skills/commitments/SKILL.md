---
name: commitments
description: "Track explicit promises, requests and follow-ups with confirmed ownership and evidence. Use for open loops and waiting-on lists; not to assign people or mark work complete from silence."
license: MIT
---

# Skillpedia — Commitments & Follow-through
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Approved communications, existing commitments and the current reference time/timezone.

## Procedure
1. Extract who asked, what was promised, by whom, due when and what counts as done. Quote or link only the minimum necessary evidence in the approved environment.
2. Separate requested, proposed, accepted, in-progress, waiting and fulfilled states. An assignee field alone need not prove acceptance; record the organization's actual convention instead of guessing.
3. Reconcile versions and changed dates with their sources. Preserve contradictory commitments and ask the accountable owner when they cannot be resolved. Do not treat the newest message as automatically authoritative.
4. Show overdue only for a known date that is before the reference time. Unknown dates are undated. Add a next-check date only as a proposal unless agreed.
5. Prepare a small follow-up queue with a single clear ask, why it matters and a non-accusatory draft. Never send, nag repeatedly or reassign automatically. Close only with completion evidence or owner confirmation.

## Deliverable
A commitment ledger delta and bounded waiting-on/follow-up view, with unsent drafts when useful.

## Acceptance
Confirmed vs proposed ownership is preserved; dates are valid; no silent closure or duplicate follow-up after an uncertain send.

## Recovery and stopping
When a source cannot be read, retain the prior item as unverified and keep the unread source in the coverage gap.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [records](references/records.md)
- [integrations](references/integrations.md)
- [people](references/people.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: What did I promise, and what am I waiting for from others?
- Paraphrase: Prepare respectful follow-ups for these open loops.
- Do not route here: Assign everyone a new task based on their job titles.
- Failure case: A due date has passed with no reply: flag a follow-up, never mark the item done.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
