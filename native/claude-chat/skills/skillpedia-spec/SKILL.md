---
name: skillpedia-spec
description: "Turn intent into clear requirements, non-goals, invariants and observable acceptance criteria. Use for an implementable contract; not to redesign or build without authorization."
license: MIT
---

# Skillpedia — Requirements & Acceptance
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
User outcome, current behavior, constraints, supplied requirements and relevant source artifacts.

## Procedure
1. Read all material requirements and inspect source visuals or attached examples when they carry meaning. Reconcile the latest intent with current behavior; do not replace it with a generic feature list.
2. Define core journeys and necessary loading, empty, permission, error, recovery and no-configuration states. Preserve unusual but intentional capabilities.
3. Assign stable requirement/acceptance IDs with inputs, expected outcomes and checks. Define protected interfaces, data ownership, privacy boundaries and delivery authorization.
4. Resolve contradictions with explicit evidence or a focused question. Record reversible assumptions; do not label them user-approved. Separate required work from future options.
5. Freeze semantic promises when coherent enough to implement, using the existing project convention. Do not require ceremonial sign-off unless policy or material choice requires it. Map later deltas without silently weakening acceptance.

## Deliverable
A concise implementable contract and acceptance map, with unresolved material decisions clearly bounded.

## Acceptance
Every important promise is testable; no invented demand, approval or completed behavior.

## Recovery and stopping
Unread material stays an explicit gap; finish independent requirements rather than guessing what a missing attachment contains.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [delivery](references/delivery.md)
- [travel context](references/travel-context.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Turn this brief into testable requirements before implementation.
- Paraphrase: What must remain true across the migration?
- Do not route here: Deploy the service because the spec is complete.
- Failure case: A screenshot carries a missing error state: inspect it rather than relying only on parsed text.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
