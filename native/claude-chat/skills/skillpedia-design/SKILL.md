---
name: skillpedia-design
description: "Design coherent architecture, user flows, interface states and visual direction from real requirements. Use for an implementable design; not an unsolicited redesign or proof of working software."
license: MIT
---

# Skillpedia — Architecture & Experience
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Acceptance contract, existing implementation, constraints and authorized references.

## Procedure
1. Inspect current boundaries and reusable patterns. Map primary journeys and information architecture while preserving identity and working contracts.
2. Define state ownership, data flow, APIs, validation, trust boundaries, concurrency and recovery. Compare consequential options and choose the simplest one that meets the contract.
3. For interfaces, specify hierarchy, typography, spacing, narrow/wide layouts, keyboard/focus, reduced motion and loading/error states. Identify actual asset requirements, rights/provenance and responsive crops.
4. For travel-adjacent systems, consider relevant timezones, partner contracts and customer-journey failure points only as questions grounded in the actual scope; never invent internal Expedia architecture.
5. Hand off component/data maps, decisions, asset briefs and acceptance implications. A mockup is not an implementation; generation prompts are not finished integrated assets.

## Deliverable
An implementable architecture/experience blueprint with trade-offs, state coverage and visual requirements.

## Acceptance
No needless stack replacement, missing recovery state or unverified claim of implementation.

## Recovery and stopping
Unavailable references or provider capabilities remain explicit assumptions/gaps, not fabricated design facts.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [delivery](references/delivery.md)
- [travel context](references/travel-context.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Design the state and recovery flow for this approved feature.
- Paraphrase: Map ownership and data movement before we build.
- Do not route here: Only correct the grammar of this sentence.
- Failure case: The reference is inaccessible: retain the limitation and do not claim a faithful match.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
