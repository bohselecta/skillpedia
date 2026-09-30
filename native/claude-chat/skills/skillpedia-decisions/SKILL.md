---
name: skillpedia-decisions
description: "Prepare a decision-ready brief or record a verified decision with rationale and consequences. Use for trade-offs, unresolved choices or decision history; not to treat an AI recommendation as human approval."
license: MIT
---

# Skillpedia — Decision Briefs & Log
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Decision question, goal, constraints, accountable decider when known and source evidence.

## Procedure
1. State the exact decision and when it is needed. Distinguish reversible choices from changes that affect security, data, spending or public behavior. Confirm who has authority when consequential.
2. Compare a small set of materially different options, including doing less or deferring. Use relevant evidence, dependencies, costs and failure modes; label assumptions and uncertain estimates.
3. Propose a recommendation only when appropriate and supported. State what evidence would change it and the smallest useful experiment for a consequential unknown. Do not conceal competing evidence.
4. Produce a short decision card: question, options, recommendation/proposal, decider, deadline basis and next action. A recommendation remains proposed until an authorized person decides.
5. When recording a decision, retain source, date, owner, rationale, consequences and superseded decision ID. Update affected work only within authorization and never erase the prior rationale.

## Deliverable
A decision card or append-only decision history update with explicit proposed/decided state.

## Acceptance
Authority and evidence are visible; trade-offs are not fabricated; a model opinion is never stored as an approved decision.

## Recovery and stopping
For missing authority or conflicting statements, preserve the unresolved question and continue analysis that does not depend on it.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [records](references/records.md)
- [delivery](references/delivery.md)
- [travel context](references/travel-context.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Prepare the trade-off between a staged rollout and a full release.
- Paraphrase: What decision do we actually need, and what would change the recommendation?
- Do not route here: Publish the decision because you prefer option A.
- Failure case: The meeting says “leaning toward A”: keep the decision proposed.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
