# Compatibility and research sources

Access/check date: **2026-09-30**. These are mutable live documentation pages,
not a claim that every underlying feature was released on this date or that
all accounts expose it. No model names, speculative SDKs or unverified APIs
are hard-coded. Retrieved facts are distinct from this package's design choices.

| Source | Verified fact used | Design consequence |
|---|---|---|
| [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) | Skills are reusable workflows; account/workspace controls and scans apply | Personal skills install through the actual Skills UI; no automatic install claim |
| [OpenAI: API skills guide](https://developers.openai.com/api/docs/guides/tools-skills) | SKILL.md with name/description and self-contained files; single-folder ZIP structure | Portable bundle structure only; this is not an API deployment or account entitlement |
| [Agent Skills specification](https://agentskills.io/specification) | Portable SKILL.md and progressive supporting resources | One independently usable skill per chat ZIP |
| [Anthropic: Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | Upload a skill from Customize/Skills; workspace controls govern use | Separate corporate Chat upload files and admin-first pilot |
| [Claude Code: Skills](https://code.claude.com/docs/en/skills) | Skills and plugin namespacing; disable-model-invocation; allowed-tools grants | Short Code names; bridge explicit-only; no tool auto-grants |
| [Claude Code: Plugin manifest](https://code.claude.com/docs/en/plugins-reference) | .claude-plugin/plugin.json, components outside metadata directory | Minimal native plugin, no invented plugin schema |
| [Claude Code: Create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces) | Named owner/plugins catalog, relative source, validation/install distinction | Local reviewed marketplace; native validation remains separate |
| [Claude Code: Discover plugins](https://code.claude.com/docs/en/discover-plugins) | Session-local --plugin-dir and install scopes | Start with a reversible one-session load |
| [Claude Code: Subagents](https://code.claude.com/docs/en/sub-agents) | Separate context, explicit tools, bounded turns | Optional local read-only evidence reviewer, no persistent worker |
| [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Focused instructions, examples, progressive disclosure and evaluation | Canonical contracts plus narrow adapters and test cases |
| [Anthropic: Equipping agents with skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Reusable instruction/resources packaging | Modular skills instead of a large always-loaded prompt |
| [Anthropic: Demystifying agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Evaluate outcomes and traces; different evidence levels matter | Deterministic helper tests are not claimed as native model evaluation |
| [Existing SkillPedia AI](https://skillpedia.ai/) | An unrelated product uses a similar name | Retain requested working name with Corgi-verse attribution and non-affiliation notice |
| [USPTO: Likelihood of confusion](https://www.uspto.gov/trademarks/search/likelihood-confusion) | Similar marks and related goods/services can matter | Plugin status is not trademark clearance; no legal assurance |

## Inherited authored techniques
The user's Corgi v1.0.1 packages and Project skill supply the lineage for
contract freeze, bounded implementation, evidence-preserving recovery,
Review/Masterwork separation, selective strong reasoning, and complete delivery.
The Attention Window adapts their human-judgment-centered workflow ideas to
work coordination. These are authored design methods, not proven comparative
benchmarks. No empirical productivity or wellbeing outcome is claimed.
