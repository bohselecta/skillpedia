# Architecture and decisions

## Goal and boundary
Deliver a usable, modular skill library for work coordination and evidence-led
execution, with a personal ChatGPT edition and corporate Claude Chat/Code
editions. This is not an always-running agent, inbox product, employee monitor,
project database or assertion of Expedia's requirements. Employer approval,
configured tools and source truth remain external.

## One contract, three host adapters
`src/catalog.json` is the canonical capability catalog: distinct triggers,
non-triggers, input, operational steps, output, acceptance, recovery and cases.
`src/references/` supplies the common operating contract and focused references.
`tools/build.py` compiles these into 16 personal ChatGPT skills, 20 corporate
Claude Chat skills and the same 20 corporate capabilities in one Claude Code
plugin. Generated skills are checked into `native/`; do not hand-edit them.
Each skill is self-contained. Shared source references are copied at build time,
not imported from sibling skills. This deliberately trades a small amount of
disk duplication for predictable individual uploads and independent updates.

Native discovery reads concise descriptions; detailed procedures and references
are loaded as needed. No giant router has to be activated on every question.
`start` can route one bounded task or simply do it; no dependency on all skills
being installed. The two Chat editions use `hoyt-*` and `skillpedia-*`; Code
uses short names under the native `/skillpedia:<name>` plugin namespace.

## Attention Window and evidence below it
Capture -> verify -> organize -> decide -> draft -> confirm is the working loop.
The default view is at most three ordinary next actions, with all critical
exceptions shown separately. Waiting, decision, watch, done and overflow work
remain in the approved source of truth, not silently discarded to make a brief
look neat. Priority has an explicit reason, not an opaque AI score.

Separate facts, inferred requests, suggested owners, agreed commitments and
confirmed decisions. Sources include account, locator, timestamp and classification.
Coverage includes the actual interval and gaps. Failure to retrieve a page or
attachment prevents an all-inbox completeness claim. Repeated runs reconcile
stable IDs and source changes, rather than multiplying reminders or actions.

## Mutable state is not a skill
An optional ledger/roster is data in an explicitly approved private destination.
Instructions, examples and public source contain no live people or project state.
Existing trackers remain authoritative. Conversation-only work must describe its
persistence limits; saving a file in a temporary chat container is not a durable
team database. The local helper uses versioned full-item patches, conflict refusal,
exact replay idempotence and create-only snapshots. It is single-user tooling,
not distributed locking, automatic synchronization or guaranteed crash recovery.

## Connector and action boundary
A skill discovers the tools the host actually exposes. It does not ship a Slack,
Gmail, Outlook, Jira or calendar integration. An account connection is capability,
not blanket scope approval. Read-only excludes saved mailbox drafts, labels,
reactions, ticket edits, calendar actions and sends. Drafting text in chat is not
saving or sending that draft. Before an authorized write: resolve exact recipient
and destination, preview substantive content, confirm applicable authority,
re-read changed state, invoke once, then verify a receipt. An uncertain result is
not a reason for a blind retry. Enterprise policies can be stricter.

## Personal / corporate separation
Hoyt accepts personal, public, synthetic and explicitly released content only.
Skillpedia stays in the corporate-approved environment. The bridge transfers a
minimal reviewed reusable method, never an inbox, employee roster or project
snapshot. Export is off by default. A content digest invalidates stale release
records after any edit; a human still determines authority and confidential
meaning. The validator is not a DLP product or declassification engine.

## Execution and worker techniques
Keep the user's semantic contract stable through implementation. Prove the risky
assumption or core interaction before extensive scaffolding. Work in bounded
vertical slices, then integrate and independently check acceptance. Distinguish
review (inspect, no edits) from Masterwork (apply authorized finishing changes).
Use strong reasoning for uncertain/high-consequence decisions and an appropriate
capable execution tier for specified work. Model switching is capability- and
host-dependent, not a hidden API. After two failed independent repair hypotheses,
reassess rather than repeating unbounded calls. A missing connector or credential
is not solved by buying more inference.

Claude Code includes one optional read-only `evidence-reviewer` subagent with
Read/Grep/Glob, a separate context and eight-turn bound. One integration owner
receives its evidence-bounded findings. It cannot mutate files, use network tools,
resolve corporate authority or prove tests ran. Skill frontmatter deliberately
omits `allowed-tools`: in Code that setting grants tool use, not a deny sandbox.
There are no hooks, MCP servers, credential inputs, telemetry or auto-launch code.

## Rejected alternatives
A single mega-skill obscures routing and bloats context. Twenty disconnected prompts
lose consistent authority and evidence rules. A new task SaaS introduces cost and
another source of truth. Storing people in SKILL.md leaks mutable data into shared
packages. Automatically mirroring corporate state into personal ChatGPT crosses
an unacceptable boundary. Hard-coded corporate roles or SLA values invent facts.
A multi-skill ZIP uploaded as one skill breaks modular installation.

## Release contract
A reproducible compiler, strict local checks, safe helper, schemas, synthetic
fixtures and receiving-host evaluations accompany the instructions. Structural
checks do not establish prompt-following reliability. Native account scanning,
discovery, reference access, tool routing and repeated-use behavior require a
pilot in each receiving host. See ACCEPTANCE.md and ../evals/README.md.
