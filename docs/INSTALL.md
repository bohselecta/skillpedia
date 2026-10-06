# Install the edition for the environment

Compatibility documentation checked on 2026-09-30. Product controls can change;
see SOURCES.md. An archive is not proof of account entitlement or administrator
approval. No API key, paid service or application runtime is required by this pack.
Python 3.11+ is optional for local helpers/build/tests, not mandatory to use the
instruction workflows. ZoneInfo uses the OS timezone database; an absent database
blocks named-timezone validation rather than inventing an offset.

## Hoyt — personal ChatGPT
Unzip `hoyt-chatgpt-UNZIP-FIRST-v1.0.0.zip`. Open `UPLOAD_THESE_TO_CHATGPT/`.
In ChatGPT's Skills page choose **Add -> Upload from your computer** and upload
the individual `hoyt-*.zip` files. The outer archive is not one skill. Wait for
host scans and resolve any Needs Review/Blocked state before enabling a skill.
Start with `hoyt-start`, `hoyt-capture`, `hoyt-triage`, `hoyt-people` and
`hoyt-commitments`. Use the other skills when relevant, not all at once.

Select the skill or say: "Use hoyt-start. I have 30 minutes. Help organize this
personal brain dump; do not send or save anything." Verify the actual installed
name and loaded instructions in the host. Only personal/public/synthetic or
explicitly released information belongs in this edition. Do not connect employer
accounts to personal ChatGPT as part of installing this package.

## Skillpedia — corporate Claude Chat
Use an employer-approved Claude account/workspace. Owners/admins may need to
allow Skills, uploads and code execution; this package cannot grant them.
Unzip `skillpedia-claude-UNZIP-FIRST-v1.0.0.zip`. Under **Customize -> Skills ->
+ -> Create skill -> Upload a skill**, upload each individual ZIP inside
`UPLOAD_THESE_TO_CLAUDE/`, then enable it in the host. Start with
`skillpedia-start`, `skillpedia-triage`, `skillpedia-people` and
`skillpedia-commitments`. Do not upload the Code plugin folder as one Chat skill.

Select the skill or ask "Use skillpedia-triage on the supplied synthetic pilot
only. Read-only. Show coverage and confirmed versus proposed actions." Native
Chat/Code synchronization may vary by client/account; the two installations here
are explicit and do not depend on it. Avoid duplicate synced/standalone skills.

## Skillpedia — Claude Code, session-local first
From the extracted corporate archive, keep `claude-code-plugin/` intact. Review
its content. In a trusted work directory with an authorized installed Claude Code:

```sh
claude plugin validate /absolute/path/claude-code-plugin
claude --plugin-dir /absolute/path/claude-code-plugin
```

In the Claude Code prompt, use `/skillpedia:start`, `/skillpedia:triage`,
`/skillpedia:people`, `/skillpedia:research` or `/skillpedia:masterwork`.
The plugin is named `skillpedia`; its native short skill names supply the suffix.
The bridge is only explicitly invoked as `/skillpedia:bridge` and still requires
release authority/content review. Starting a session does not run all skills.

From the repository source the equivalent plugin path is `native/claude-code`.
`claude plugin validate .` also validates the repository's marketplace. Official
CLI validation and actual installation are separate checks; record both.

## Optional persistent Code marketplace installation
Only after review and authorization for the selected installation scope:

```sh
# Local reviewed repository; no public-directory submission is needed.
claude plugin marketplace add /absolute/path/skillpedia
claude plugin install skillpedia@corgi-verse --scope local
claude plugin list
claude plugin details skillpedia
```

For a hosted copy, use the exact reviewed repository revision/ref according to
current Claude Code marketplace controls, rather than following an unreviewed
moving branch. Local scope avoids silently making the plugin global. Respect
administrator marketplace restrictions. Restart/reload per the host after changes.
No command in this guide changes permissions to bypass an organization policy.

## Updates, rollback and removal
Keep the installed version and archive checksum. Update from a reviewed source,
rebuild/tests, and test a single skill in an isolated host before replacing the
set. Preserve any edited skill/roster separately; do not overwrite customizations
with generated files. There is no automatic updater. Chat updates/removal use the
host's skill controls; do not promise replacing a ZIP will deduplicate a rollout.
Code uninstall uses the host's plugin controls for the same installation scope.
For a session-local test, leave that session and restart without `--plugin-dir`.
Retain prior packages for rollback and remove only this package, not other skills.

## First-use and recovery checks
Use the synthetic pilot before real sources. Verify correct trigger, one actual
local reference read, declared coverage, no unauthorized actions, no personal
work-data request and a stable repeated-run result. If tools are unavailable,
organize supplied approved material and label coverage supplied-only. If a ZIP
is rejected, verify that it is an individual skill ZIP and inspect the host scan;
never strip safety instructions to bypass review. See EVALUATION.md in the archive
or ../evals/README.md in source for exact evidence to capture.
