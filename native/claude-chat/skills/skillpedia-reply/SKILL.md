---
name: skillpedia-reply
description: "Draft a clear, context-aware reply with one useful ask and an appropriate tone. Use for email or Slack responses; not to send messages, impersonate a colleague or commit the user without approval."
license: MIT
---

# Skillpedia — Clear Replies
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Target conversation, intended outcome, audience and relevant current thread context.

## Procedure
1. Read the relevant thread and resolve who the reply is for; inspect quoted older material carefully. Use only the approved account/context. Do not infer private motives or emotional states.
2. Decide the purpose: answer, clarify, acknowledge, request a decision, decline, follow up or escalate. State the core point and one specific CTA when needed; avoid creating an ask for a pure acknowledgment.
3. Use facts with sources and preserve uncertainty. Do not promise a date, budget, feature, concession or new obligation unless the user authorized it. Label suggested commitments as proposals.
4. Draft in the user's chosen voice, respectful and direct. Preserve important nuance while cutting filler. Give alternatives only when the choice materially affects the outcome.
5. Stop at an unsent draft unless the user authorizes sending. Before an approved send, verify exact account, recipients/channel, attachments and content; re-read changed thread context. If the send result is uncertain, check for the created message before retrying.

## Deliverable
One ready-to-review draft with a clear CTA where appropriate and a brief note about unresolved facts.

## Acceptance
No unauthorized sending, hidden promise, fabricated fact, or unsupported characterization of people.

## Recovery and stopping
When the recipient or commitment is ambiguous, draft with an explicit placeholder and ask only what blocks the send.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [integrations](references/integrations.md)
- [people](references/people.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Draft a short reply asking for the one decision blocking us.
- Paraphrase: Help me say no respectfully without promising a new date.
- Do not route here: Pretend to be my coworker and approve this.
- Failure case: The thread asks for a Friday commitment but the user has not agreed: do not promise Friday.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
