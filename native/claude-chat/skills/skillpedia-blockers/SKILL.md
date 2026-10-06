---
name: skillpedia-blockers
description: "Find evidence-backed issues, risks and dependency blockers and prepare an escalation packet. Use when delivery is stuck or customer impact is suspected; not to invent incident severity or run production fixes."
license: MIT
---

# Skillpedia — Blockers & Escalation
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Observed symptom, affected journey/dependency, known owner and relevant authorized logs or threads.

## Procedure
1. Separate an observed issue from a future risk, assumption or unanswered question. Establish first/last observed time, source, scope of impact and what remains unverified.
2. Map the dependency: what is blocked, what can continue, who can resolve it and what exact decision or evidence is needed. Do not blame an individual or infer intent.
3. Inspect authoritative incident/runbook and escalation rules when supplied. Never invent Expedia severity labels, SLAs or reporting routes. Potential active security/customer harm warrants immediate attention under the real policy, not a routine triage queue.
4. Test a bounded hypothesis only within authorized non-destructive scope. Keep production access, deployment, data changes and broad log collection separate from analysis.
5. Prepare an escalation packet: impact evidence, current mitigation, owner status, decision/ask, deadline basis, safe next check and rollback relevance. Draft routing, do not send without explicit authorization.

## Deliverable
A concise issue/risk record and actionable escalation draft with source evidence and unresolved questions.

## Acceptance
Observed impact is distinguished from possibility; independent work can continue; no invented policy or unauthorized production action.

## Recovery and stopping
Without enough evidence, label the hypothesis and propose the cheapest safe discriminating check.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [records](references/records.md)
- [integrations](references/integrations.md)
- [delivery](references/delivery.md)
- [travel context](references/travel-context.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: This dependency is holding up the release. Identify what to escalate and to whom.
- Paraphrase: Turn these incident notes into a factual blocker brief.
- Do not route here: Guarantee that the outage is fixed from a green build.
- Failure case: The status message and dashboard disagree: retain the conflict and do not declare recovery.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
