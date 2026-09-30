# Contract freeze, execution cadence and release

Freeze the meaning before a substantial build: user outcome, non-goals,
protected behavior/data, interfaces, error recovery, authorization and
observable acceptance IDs. Test the core interaction or riskiest assumption
before building a shell. Reuse existing contracts/status files. A small change
needs a small contract, not a program of paperwork. A later valid change
records its delta and invalidates only affected evidence.

Use stronger reasoning for architecture, uncertainty, sensitive migrations,
security and final integration; use an adequate faster tier for mechanical,
well-specified work when the host actually offers one. Model names and effort
controls are capabilities to verify, not policy to hard-code. A useful manual
switch first saves the goal, revision, dirty paths, evidence, current hypothesis
and exact next step. Two independent failed repair hypotheses trigger a
reassessment, not weaker assertions or unbounded calls. No new API bill.

Delegation is optional. Assign disjoint bounded work, inputs, expected output,
checks and a known revision. Give only the context needed. One integration
owner reconciles results and authorizes shared-state changes. A delegated
reviewer must see requirements/source evidence, not just the builder's story.
The same model context checking itself is explicitly self-review.

For code, inspect the repository and applicable AGENTS.md/CLAUDE.md hierarchy,
retain data and migrations, implement real user/error paths, and test interfaces
in the appropriate environment. A PM's planning request is not authorization
to code. For authorized implementation, finish tested vertical slices rather
than stopping at a plan. No feature pruning to make tests pass.

Release packet: exact commit/artifact; accepted scope; observed checks and
limits; affected systems/data; owner; rollout/rollback; dependency readiness;
monitoring and support handoff; explicit release authority. No invented
Expedia gate names. No automatic deployment. A rollback plan is not proof it
was exercised. A successful deploy is not proof of the customer journey.

Acceptance labels: PASS, FAIL, NOT_RUN, NOT_APPLICABLE (reason). Record revision,
environment, command or inspection, observation and evidence. Distinguish
source review, tests, synthetic fixtures, browser inspection, provider calls,
physical hardware and human acceptance. Masterwork edits and finishes;
Review reports defects without silently changing the work.
