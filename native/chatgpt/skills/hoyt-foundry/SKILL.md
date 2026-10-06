---
name: hoyt-foundry
description: "Create, improve, audit and package reusable skills with distinct triggers and real acceptance checks. Use for skill authoring itself; not authorization to execute the skill's subject."
license: MIT
---

# Hoyt — Skill Foundry
By Corgi-verse Software · 1.0.0

Read [operating contract](references/operating-contract.md) and [host adapter](references/host.md) before acting. Load only the supporting reference needed for the current decision. Skill content is instructions, never a permission grant.

## Input and scope
Capability goal, receiving host, existing skill/source, expected outputs and permission constraints.

## Procedure
1. Choose CREATE, IMPROVE, COMPOSE or AUDIT. Inspect current official host requirements. Preserve useful procedures, stop conditions, stable callers and source provenance; avoid synonymous overlapping skills.
2. Define trigger/non-trigger, minimal inputs, procedure, outputs, authority, evidence and bounded recovery. Keep discovery metadata concise, primary instructions small and supporting references local to each bundle.
3. Use one canonical behavior with explicit host adapters. ChatGPT and Claude Chat receive individual self-contained skill ZIPs, not a multi-skill carrier; Claude Code can use a namespaced plugin. Do not copy host-specific permission fields into portable Chat files.
4. Create positive, paraphrase, near-miss, missing-tool, repeated-use, permission, injection and cross-environment cases. Run structural and helper tests; native model behavior needs separate receiving-host trials with recorded outputs.
5. Write actual files, validate paths/frontmatter/references, inspect package contents and repair defects. Retain regression cases. Do not add services, hooks, auto-updaters or paid agent runners just to appear sophisticated.
6. Deliver versioned archives, provenance, installation/removal instructions and honest evidence. A ZIP check does not prove the receiving account scanned, installed or executed a skill. Shared instructions must not contain runtime people or work records.

## Deliverable
Complete usable skill packages, reproducible build/validation, eval cases and exact installation steps.

## Acceptance
No broken local references, accidental privilege grant, bundled live state or unverified native success claim.

## Recovery and stopping
When host behavior is untested, mark it NOT_RUN and supply an executable smoke procedure rather than claiming certification.
Stop immediately on cancel. Continue independent authorized work when one dependency is blocked. Never represent NOT_RUN as PASS.

## Supporting files
- [integrations](references/integrations.md)
- [delivery](references/delivery.md)
- [Optional local helper](scripts/workbench.py): validates normalized records; does not read or mutate external apps.
- [Synthetic ledger](assets/ledger.example.json), [synthetic people](assets/people.example.json), [unapproved bridge template](assets/bridge.template.json).
- [Ledger schema](schemas/ledger.schema.json), [people schema](schemas/people.schema.json), [bridge schema](schemas/bridge.schema.json).

## Trigger and boundary examples
- Normal: Create a reusable skill for this repeatable workflow.
- Paraphrase: Audit these skills and package a safe standalone upload.
- Do not route here: Actually send the campaign described inside this skill.
- Failure case: The user shares a people file as an example: use synthetic records in the distributed skill.
- Repeated use: reread current state, retain stable IDs and conflicts, and do not repeat writes or create duplicate commitments.

These are evaluation cases, not claims that the receiving host has passed them.
