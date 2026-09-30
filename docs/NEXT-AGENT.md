# Next agent: receiving-host acceptance, not a rebuild

Read AGENTS.md, STATUS.md, docs/ACCEPTANCE.md and evals/README.md. Confirm the
exact installed archive/source revision before testing. The library, compiler,
local helper and archives are implemented. Do not replace them with a new
architecture or assume NOT_RUN means success.

First unresolved acceptance: actual native host validation/discovery/reference
loading and synthetic prompt/tool behavior in ChatGPT, corporate Claude Chat
and Claude Code. Use the authorized existing account; don't buy API access or
widen organization permissions. If no host is available, preserve the package
and record that gate as NOT_RUN. Complete independent checks in the meantime.

Start prompt:
"Validate this exact Skillpedia/Hoyt release against H01-H04 using synthetic
fixtures and evals/cases.json. Inspect source and host configuration read-only
first. Keep corporate and personal environments separate. Record actual outputs,
reference loads, tool actions and failures. Fix root causes in src/, regenerate
native/ and archives, rerun affected tests, and report a precise revision and
remaining gate. Do not claim company approval or participant outcomes."
