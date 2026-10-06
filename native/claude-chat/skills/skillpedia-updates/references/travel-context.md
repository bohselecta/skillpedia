# Optional travel-platform delivery lens

These are **questions to investigate when the actual project warrants them**, not
claims about Expedia's systems, responsibilities, policies or current problems.
Do not load this lens for unrelated IT work. Use public/synthetic information in
the personal edition; real work evidence belongs in the approved corporate host.

For customer-facing change, ask which journey is affected: discovery/search,
availability or price display, booking/payment, confirmation, servicing or
cancellation/refund. Distinguish a blocked synthetic test from confirmed customer
impact. Ask what evidence would establish correctness and what safe rollback
exists; do not invent volume, revenue impact or incident severity.

For partner/service dependencies, identify the actual interface owner, tested
contract, environment, availability of fixtures, retry/idempotency assumptions,
reconciliation and fallback. Do not assume a supplier API, internal service,
runbook or release gate exists merely because it is common in software work.
Separate a partner's stated commitment from a proposed date or sales claim.

For distributed coordination, make timezone, local date, handover window and
accountable decision-maker explicit. Ask whether region/currency/locale,
accessibility, data handling or support communications materially change the
acceptance criteria. Unknown requirements stay questions until sourced.

A useful cross-team release brief has: the changed journey; protected behavior;
verified test environment/revision; dependency readiness with sources; unresolved
risks and decisions; rollout/rollback ownership; support/handover needs; and the
next go/no-go evidence check. A PM brief does not grant production authority.
Follow real employer release/security controls instead of inventing an
Expedia-branded process or certification.
