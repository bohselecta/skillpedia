---
name: plan
description: "Turn agreed outcomes into a realistic, dependency-aware plan or rebalance overloaded work. Use for milestones, prioritization and trade-offs; not to assume capacity or schedule people without agreement."
license: MIT
---

# Skillpedia — Plan & Rebalance
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Goal, non-goals, known constraints, available capacity if supplied and current commitments.

## Procedure
1. Separate fixed constraints from preferences and estimates. Establish the smallest useful outcome and what must be preserved. Recover existing decisions and accepted scope before redesigning the plan.
2. Break work into complete, bounded increments with inputs, dependencies, owner status, acceptance and next check. Identify the riskiest assumption or core interaction to test first.
3. Compare scope/capacity/date trade-offs, including a simpler option. Do not manufacture duration, velocity or percent confidence. Label provisional estimates and unknown capacity.
4. For overload, identify what must happen now, what can wait and which commitment needs renegotiation. Keep a small active window rather than presenting every backlog item as urgent.
5. Produce a plan and explicit decision/approval needs. A plan does not assign teammates, move calendar events, authorize spending or launch a build. Authorized implementation routes to Project with the actual contract.

## Deliverable
A bounded delivery or personal work plan with dependencies, acceptance and explicit trade-offs.

## Acceptance
No invented capacity or agreement; protected scope remains; every increment has a check and owner status.

## Recovery and stopping
For missing capacity, provide a sequence and decision points rather than false precision in dates.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [records](references/records.md)
- [delivery](references/delivery.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Help me rebalance these commitments for this week.
- Paraphrase: Give me the smallest complete sequence that meets this goal.
- Do not route here: Reschedule everyone and cut requirements without consulting the owner.
- Failure case: A due date conflicts with known dependencies: flag the trade-off instead of hiding it.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
