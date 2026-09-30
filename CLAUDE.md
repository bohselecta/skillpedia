# Skillpedia engineering entry

Read README.md, STATUS.md, docs/ARCHITECTURE.md, docs/ACCEPTANCE.md and
src/catalog.json before changes. This repository authors skills, not an
always-running agent or a company's internal project system.

Keep src/ canonical; tools/build.py creates native/ and dist/. Never edit a
native skill without changing its canonical source. Preserve names, explicit
write boundaries, partial-coverage warnings, source provenance, confirmed vs
proposed ownership, and the personal/corporate separation. Every skill must
work alone; no sibling filesystem dependency. No live data, credentials,
company logos, paid services, telemetry or automatic outbound actions.

Run python tools/build.py, python tools/validate.py and
python -m unittest discover -s tests -v. Check packages from a clean temporary
directory. Do not mistake local checks or a rendered demo for native model
behavior. Host smoke tests are in evals/README.md. Do not run billed evals or
change account permissions without authorization. Reviewable branches; no
force pushes. See docs/NEXT-AGENT.md for the next acceptance gate.
