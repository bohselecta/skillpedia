---
name: hoyt-capture
description: "Turn a brain dump or rough notes into a few clear candidate actions, questions and ideas. Use to get work out of the user's head; not to invent commitments or force every thought into a task."
license: MIT
---

# Hoyt — Capture & Clarify
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Text, authorized transcript or rough notes, plus any explicit goal. Do not require polished input.

## Procedure
1. Preserve the original meaning and uncertainty. Separate observations, ideas, worries, questions, candidate actions and explicit promises. Keep non-actionable thoughts as notes.
2. Group related ideas without losing a distinction that changes the user's intent. Propose one next physical or communicative action per actionable group. Mark inferred actions as proposed.
3. Extract people, dates and dependencies only when stated. Unknown owner/date stays unknown; resolve relative dates only with a reference date and timezone. Do not turn “maybe” or “someone should” into an assignment.
4. Ask no more than the decision-changing clarification needed to proceed; leave other questions visible. Offer a small now/later/parking-lot view rather than a giant checklist.
5. When asked to save, propose the state changes and use the approved private store or deliver a file. Do not edit the installed skill to remember the contents.

## Deliverable
A compact organized capture, proposed next actions, unresolved questions and retained parking lot.

## Acceptance
No source idea is silently lost; thoughts are not fabricated tasks; proposals and promises remain distinct.

## Recovery and stopping
For unclear audio or missing context, retain an uncertainty marker rather than guessing names or dates.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [records](references/records.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Here is everything in my head. Help me turn it into something manageable.
- Paraphrase: Untangle these notes without making a task out of every sentence.
- Do not route here: Send these ten tasks to the team now.
- Failure case: The note says “maybe ask Lee Friday”; keep this proposed and do not assign Lee.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
