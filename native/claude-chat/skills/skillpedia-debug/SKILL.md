---
name: skillpedia-debug
description: "Diagnose a reproducible failure and repair its root cause within authorized scope. Use for failed checks or broken behavior; not speculative refactoring or production access by implication."
license: MIT
---

# Skillpedia — Evidence-driven Debugging
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Expected behavior, symptoms, current revision/environment and available reproduction/logs.

## Procedure
1. Reproduce or tightly bound the failure. Inspect real assertions, logs and invalid-condition results; a zero exit code is not semantic success. Distinguish a pre-existing failure from a regression using a baseline.
2. Form a few falsifiable hypotheses and choose the cheapest discriminating check. Change one consequential variable at a time where practical. Preserve privacy in logs and avoid destructive production experiments.
3. Locate the cause across inputs, state, configuration, dependencies and code. Apply the smallest root-cause repair and retain the failing case as a regression.
4. Rerun the original reproduction and affected acceptance. Do not hide failure with skipped tests, broad catches or relaxed checks. Correct a demonstrably wrong test only with independent evidence and a recorded reason.
5. After two distinct repair hypotheses fail, reassess assumptions or reasoning depth. Missing credentials/tools is an explicit blocker. Return evidence, actual changes and bounded remaining uncertainty.

## Deliverable
An evidence-backed diagnosis and verified repair, or a precisely bounded hypothesis with the next check.

## Acceptance
The original failure is retested; assertions are not weakened; source versus executed evidence stays distinct.

## Recovery and stopping
Without reproduction/access, label hypotheses and ask for the minimal missing evidence instead of inventing a fix.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [delivery](references/delivery.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Find why this test fails and repair the cause.
- Paraphrase: Explain why the empty configuration path breaks.
- Do not route here: Rewrite working code just because it looks old.
- Failure case: A helper exits zero but reports failed checks in JSON: treat the checks as failed.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
