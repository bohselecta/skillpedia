---
name: skillpedia-review
description: "Inspect actual work for evidence-backed defects and requirement gaps without silently editing it. Use for review-only audits; not final mastering or a guarantee of security."
license: MIT
---

# Skillpedia — Independent-minded Review
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Actual artifact/diff, original requirements, relevant context, revision and available test evidence.

## Procedure
1. Read the real artifact and trace important requirements through implementation, tests, documentation and behavior. Do not review only the author's summary.
2. Check relevant correctness, data handling, authorization, source freshness, concurrency, accessibility, failure recovery and factual claims. Examine missing evidence and contradictory outputs.
3. Report findings with severity, exact location, evidence, consequence and a reproducible check or focused repair. Separate defects from hypotheses and preferences; do not manufacture findings.
4. Check that claimed success matches the tested revision and environment. Flag disabled tests, placeholders, inappropriate imagery and untested live boundaries. No findings is not security certification.
5. Stay read-only unless changes are separately authorized. Label same-context inspection as self-review. A supported fresh reviewer gets requirements and independent evidence, not just the builder's success story.

## Deliverable
Prioritized findings or an evidence-bounded no-findings result, coverage limits and a precise repair handoff.

## Acceptance
No unapproved edits or fabricated issues; review independence and coverage are honestly labeled.

## Recovery and stopping
Without source access, restrict the review to supplied material and state what could not be inspected.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [delivery](references/delivery.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Review this delivery against the agreed criteria; do not edit it.
- Paraphrase: Which claims are not supported by the actual evidence?
- Do not route here: Finish and rewrite the actual document for me.
- Failure case: The same session did the build: label the review self-review, not independent.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
