---
name: masterwork
description: "Finish, simplify, integrate and verify existing work while preserving meaning, identity and capabilities. Use for final mastering; not review-only, feature pruning or generic stylistic replacement."
license: MIT
---

# Skillpedia — Masterwork
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Existing document, design, code or deliverable; purpose/audience; preserved meaning and acceptance.

## Procedure
1. Inspect the real artifact and establish what must remain: factual meaning, voice, user intent, useful detail, working behavior, data and public contracts.
2. Remove identifiable repetition, empty claims, generic praise, process narration and unnecessary abstraction. Preserve useful examples, nuance and distinctive character. No arbitrary percentage cut.
3. Finish in-scope placeholders, broken links/interactions, inconsistent states, unclear CTAs, missing context and stale documentation. Preserve security, validation, accessibility and recovery.
4. Prove code/content is unused before removing it, including dynamic consumers. Keep the project's identity and stack; purposeful simplicity is not a redesign by default.
5. Apply changes to the actual authorized deliverable, inspect the final diff/output and rerun affected checks. Return the finished work, not just recommendations. Good work can remain unchanged.

## Deliverable
The actual revised deliverable or justified no-change result, plus a minimal evidence-based handoff.

## Acceptance
No silent scope loss, altered meaning or false completion; changed behavior is rechecked.

## Recovery and stopping
Without write access, deliver an explicitly unapplied patch or revised copy and say what remains unapplied.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [delivery](references/delivery.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Master this stakeholder brief: remove filler without hiding the risks.
- Paraphrase: Make the finished project coherent and verify the changes.
- Do not route here: Only list issues; do not alter the artifact.
- Failure case: Shortening a report would remove a material caveat: preserve the caveat.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
