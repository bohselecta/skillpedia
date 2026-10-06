# Minimal work records

Use the organization's existing authoritative tracker where available. The
portable JSON files are an optional local snapshot/exchange format, not a
new required project management system. Start with one file rather than
several overlapping trackers. Keep real records out of this public repository.

A work item carries stable id; item_version; kind (task, issue, risk, decision,
note); summary; state (proposed, needs_action, waiting, blocked, decided, done,
cancelled); owner_id or null; owner_status (unknown, proposed, confirmed);
due_at/follow_up_at or null; critical flag; source_ids; next_action; checked_at;
and resolution_source_ids for decided/done states. Critical is a source-backed
exception, not the same as unread. Unconfirmed assignments stay proposed.
A decision records the decider and rationale in the approved tracker; a
recommendation is not a decision. Reopened work gets a new item_version.

Each source records id, account, URI, timestamp and classification. Use an
actual supplied locator or a clearly identified user-capture record, never
fabricated links. Store minimal excerpts only where policy allows. Evidence
may disagree; retain contradictory assertions until resolved by an accountable
owner or authoritative source. Do not discard a conflict merely because one
message is newer. Coverage stores the examined interval, scope, completion
status and limitations. A baseline revision and item versions make conflicts
visible; they are not a multi-user database lock.

## Portable artifacts
- `work-ledger.json`: compact private work state and source coverage.
- `people.json`: explicit work relationships, not a personality dossier.
- `action-receipt.json`: requested mutation, approved target/content hash,
  returned ID, verified state and any uncertain outcome. Never a password.
- `bridge-packet.json`: public/released method only, never a work-ledger export.

The optional `scripts/workbench.py` is standard-library, local-only tooling.
It validates normalized records, renders a brief, applies explicit versioned
patches to a new output, adds people with collision checks, and validates or
exports a bridge packet. It does not read Slack/email, classify raw language,
send messages, verify someone's identity or prove information is public.
Run `python scripts/workbench.py --help`. Use a supplied absolute skill path
when the host mounts skills elsewhere; never invent that path.

For an update, read current revision; prepare the exact diff; validate; write
to an approved location; read back; retain the prior revision per policy.
The helper refuses to replace an existing output. Choose a new filename; do
not delete the old one to circumvent conflict handling. In hosted chat, file
outputs may be ephemeral: explicitly save/export through an approved host
mechanism and verify its destination before promising persistence.
