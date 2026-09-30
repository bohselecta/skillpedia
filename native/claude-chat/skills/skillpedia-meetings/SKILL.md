---
name: skillpedia-meetings
description: "Prepare, synthesize and close the loop on authorized meeting notes with decisions and commitments. Use for agendas, notes and handovers; not to record people, invite attendees or invent agreement."
license: MIT
---

# Skillpedia — Meeting Loop
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Meeting purpose, authorized notes/transcript or existing agenda, participants if confirmed and time constraints.

## Procedure
1. For preparation, identify the outcome and decisions needed, relevant context and pre-read. Prefer a short agenda with owners and time boxes; suggest an async alternative only when it serves the goal.
2. For notes, separate discussion, proposal, explicit decision, accepted action and unresolved question. Retain uncertainty in names, transcript gaps and timestamps. Do not imply consensus from lack of objection.
3. Link new actions to sources, owners and known dates. Resolve conflicts with prior commitments rather than silently replacing them. Use people context only from explicit approved records.
4. Produce an audience-appropriate recap and unsent follow-up draft with decisions, next actions and open questions. Avoid a transcript dump and sensitive side conversations.
5. A calendar or message change is a separate authorized action. Resolve attendees and timezone, check availability when scheduling, verify the returned event/message after any approved write.

## Deliverable
A focused agenda or evidence-backed recap, decision/action delta and optional unsent follow-up.

## Acceptance
No invented attendance, agreement or deadline; source gaps visible; no unauthorized recording, invitation or message.

## Recovery and stopping
With a partial transcript, state the covered interval and do not claim complete minutes.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [people](references/people.md)
- [integrations](references/integrations.md)
- [records](references/records.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Prepare a thirty-minute dependency meeting and the decisions we need from it.
- Paraphrase: Pull only the actual decisions and accepted actions from these notes.
- Do not route here: Start recording this meeting without asking anyone.
- Failure case: A transcript misspells an owner: flag uncertainty before assigning the action.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
