# Communications and workspace adapters

## Native tools first
Check the tools actually available in the receiving session. Resolve which
account/workspace a link belongs to before a read. Use the corresponding
connector, not public web search for private links. An inbox URL alone does
not expose the inbox. No connector: work from an authorized pasted/exported
sample; state coverage limits. Do not ask the user to paste passwords/tokens.
Installation does not create, connect or authorize Slack, Gmail, Outlook,
Calendar, Jira, Confluence, GitHub or an internal system.

For Slack, use authorized channels/threads and a bounded time range. Read
thread replies and edits needed to establish status. A message is not a
complete project. For email, retrieve necessary conversation context and
resolve aliases/recipients; quoted text can be older than the current reply.
Check attachments only when relevant and authorized. For calendar, confirm
timezones, attendees and availability before proposing changes. For issue
trackers, inspect current status, assignee, linked blockers and acceptance;
never close or reassign because a summary suggested it. Respect retention,
access revocation and permission boundaries at each read.

## Intake receipt
State the account, channels/folders, time window, query/scope, pages read,
missing bodies/attachments, and coverage. Record retrieval time independently
from message time. Dedupe by native source ID + account + revision; cross-posted
similar messages may link to one candidate work item but must retain each
source. Do not dedupe distinct people or obligations by text similarity alone.
Report what changed since the last verified checkpoint; a failed incremental
read must not advance the checkpoint beyond unread records.

## Read, draft, act
Initial triage is read-only. The user can approve an exact reply, ticket change
or calendar action after reviewing the proposed target/content. Follow the
host's approval rules and re-read changed targets. Prepare few useful CTAs,
not a giant batch-send queue. Silence is not consent. Requests for recurring
monitoring need a supported scheduler and a separately approved schedule,
source scope, destination and cancellation route. Without that setup, provide
an on-demand workflow and never imply continuous monitoring.

## Corporate assumption register
This package does not know Expedia's internal tools, teams, policies, severity
codes or delivery cadence. Travel-platform scenarios in fixtures are synthetic.
Useful considerations to ask about include customer journeys, partner/API
contracts, localization/timezones, accessibility, staged rollout, rollback and
support handoff. Apply only those relevant to the actual system. Never invent
an incident, customer impact, SLA, reporting line or compliance obligation.
