---
name: skillpedia-research
description: "Investigate facts, APIs, constraints or alternatives with current traceable evidence. Use when a decision needs research; not as a substitute for implementation or a reason to expose private context publicly."
license: MIT
---

# Skillpedia — Evidence-led Research
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Decision question, scope, known evidence and changing facts that matter.

## Procedure
1. Frame the decision, population/time period, success criteria and material unknowns. Inspect supplied evidence first. Keep company/project identifiers out of public queries.
2. Use current primary documentation for changing product behavior, APIs, costs and policies. Record the access date and source revision/publication date where available. Do not call a source current merely because it was retrieved today.
3. Distinguish direct observations, documented claims, executed tests, inference and speculation. Examine contradictory evidence and alternative explanations; check consequential citations in context.
4. Compare only materially relevant options, including the simplest viable route. State what evidence would change the conclusion. Use a bounded experiment for a consequential unknown rather than an endless survey.
5. Deliver the decision brief with source-to-claim traceability, uncertainty and implications. Keep corporate research in the approved workspace; external tools receive only authorized, minimized context.

## Deliverable
A supported research brief with checked sources, access dates, limitations and the next decision or experiment.

## Acceptance
No fabricated citations, benchmark results or freshness; confidential queries are not sent to public search.

## Recovery and stopping
Without browsing, use dated supplied sources and explicitly state the freshness boundary.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [integrations](references/integrations.md)
- [travel context](references/travel-context.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Check the current supported skill format before we package it.
- Paraphrase: What evidence would make us choose a different integration approach?
- Do not route here: Apply this already-approved small code patch.
- Failure case: A vendor marketing page claims reliability without measurements: attribute the claim, do not adopt it as observed.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
