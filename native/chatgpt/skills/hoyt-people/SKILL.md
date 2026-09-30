---
name: hoyt-people
description: "Add or update explicit people records and working agreements for coordination. Use for stakeholder context or one-to-one preparation; not personality profiling, surveillance, invitations or automatic assignment."
license: MIT
---

# Hoyt — People & Working Agreements
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
A purpose, authorized people file or supplied facts, and a private storage destination only when persistence is requested.

## Procedure
1. Read the approved roster. Establish identity from a native account/user ID or explicit user confirmation; identical display names can be different people. Ask only when ambiguity affects a target or commitment.
2. Add the minimal work context: role, stated timezone, explicit communication preference, relationship to the work, source and review date. Separate observed facts from proposed corrections. Do not infer temperament, health, politics, motivations or performance.
3. Link a person to confirmed commitments and accountable decisions without converting proposed ownership into agreement. Distinguish requester, owner, reviewer and decider; do not invent a reporting line.
4. Preview add/update/remove changes. Save to the user-selected private location only when authorized, preserving stable IDs and versions. Adding a person does not contact them or give access.
5. For meeting prep, produce shared goals, last agreed commitments, open questions and one respectful draft. Allow corrections/removal and apply the organization's retention rules; do not modify global model memory.

## Deliverable
A minimal roster change or source-backed relationship brief, with unresolved identities clearly marked.

## Acceptance
No name-only identity merge, sensitive inference, private data baked into a shareable skill, or invented agreement.

## Recovery and stopping
Without a durable store, deliver an explicitly unsaved roster file; say that later sessions need it or an approved connection.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [people](references/people.md)
- [records](references/records.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Add Morgan as the release reviewer, based on this confirmed directory entry.
- Paraphrase: Help me prepare for a one-to-one using our actual commitments.
- Do not route here: Rank who on my team is least reliable from their writing style.
- Failure case: Two people share a name: retain separate IDs and resolve the intended recipient before any action.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
