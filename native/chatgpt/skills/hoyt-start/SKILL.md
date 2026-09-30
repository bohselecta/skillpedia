---
name: hoyt-start
description: "Orient an overloaded work session and show a small, evidence-backed next-action window. Use for a daily reset, handover or choosing what needs attention; not for every isolated question."
license: MIT
---

# Hoyt — Attention Window
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Current goal, available time, selected environment and any supplied work snapshot. Retrieve an authorized existing checkpoint before asking the user to repeat it.

## Procedure
1. Start from the supplied situation; let an unstructured brain dump count as input. Establish the account/environment before connector reads. Do not demand a full project dossier. Offer capture when the work is still only in the user's head.
2. Read the current approved ledger and the evidence needed for the next decisions. Reconcile changes, missing ownership, stale status, conflicts and unread sources. Treat a previous summary as a pointer, not fresh evidence.
3. Create the Attention Window: at most three ordinary actions with one verb, source, why now, owner status and next check. Separately display every critical exception. Keep the remaining work in Waiting, Needs decision, Watch and Done with counts and accessible IDs.
4. Route a bounded subtask to a relevant installed skill only when helpful; otherwise perform the same procedure directly. Do not start a cascade of twenty skills. Use stronger reasoning where ambiguity or consequence warrants it, not for clerical reformatting.
5. Close with what changed, what can safely wait, and the next resume point. Offer a private checkpoint when persistence is useful; obtain the destination before a write. Do not claim a recurring daily briefing was scheduled.

## Deliverable
A calm, source-backed next-action window and a small resumable checkpoint; not a second full project plan.

## Acceptance
Every action is traceable; critical exceptions remain visible; partial coverage is explicit; no unauthorized mutation or invented obligation.

## Recovery and stopping
Without source access, label a supplied-input-only snapshot and organize what is available. Empty state is a valid result.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [records](references/records.md)
- [integrations](references/integrations.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Help me reset: I have forty minutes and too many open loops.
- Paraphrase: What deserves my attention before I leave today?
- Do not route here: Explain what a DNS record is.
- Failure case: A prior checkpoint says all work is done but one source is inaccessible: do not report all clear.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
