# Skillpedia / corporate environment adapter

Use only the organization's approved account, configured connectors, selected
sources and permitted data classes. The package does not know Expedia's real
teams, policies, severity levels, systems or approval process. Discover those
from authorized sources rather than inventing them. No Expedia affiliation,
endorsement, procurement or security approval is implied.

Respect employer policy even when a tool is technically callable. Never route
work data into personal Hoyt/ChatGPT as a workaround for missing access. Keep
work records in the approved work system or explicitly selected private local
workspace, never in this public package repository. The bridge moves reviewed,
releasable methods only and does not synchronize state.

This is a Claude Code plugin. Its skills are invoked as /skillpedia:triage,
/skillpedia:people, /skillpedia:project and so on. The short folder name matches
the native SKILL.md name; the plugin supplies the skillpedia namespace. Do not
install duplicate standalone copies alongside the plugin in the same scope.

Read applicable CLAUDE.md and AGENTS.md instructions and live repository state.
Use current host tools/approvals. This plugin has no hooks, MCP servers, shell
interpolation, tool auto-approval or hidden telemetry. It does not change host
permissions. The bridge is user-invoked only; invocation still does not authorize
export. Never add allowed-tools expecting it to act as a denial policy.

An optional evidence-reviewer subagent reads only supplied local files with
Read/Grep/Glob in a separate context. Use it only when supported, useful and
within the authorized workload. Give exact paths, revision, requirements and
checks. It has no authority to edit, contact people, approve a release or assert
live tool results it did not see. The integrator owns final acceptance. Delegation
uses the host's quota; there is no free background agent or model API here.
