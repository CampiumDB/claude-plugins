# Campium Navigator

A Claude Cowork plugin that helps people find their way around Campium. Ask where a setting lives, how to do a task, which report answers a question, or why something is not working, and Claude answers from the official Campium help docs with the menu path, steps, and a docs link.

Built for camp admins using CampiumDB, and for the Campium team answering camp questions (ask for "a reply to send" and it drafts one).

## Skills

| Skill | Use it for | Try asking |
| --- | --- | --- |
| campium-navigator | "Where is" and "how do I" questions | "Where do I turn on waitlists?" |
| campium-walkthrough | Step-by-step checklists for bigger jobs, with an optional one-step-at-a-time mode | "Walk me through getting Summer 2027 ready for registration" |
| campium-troubleshoot | Error messages and things that are not working, plus a support email draft when the docs run out | "A parent says they can't see our medical form" |
| campium-find-report | Picking the right report and explaining its filters and columns | "Which report shows who still owes money?" |

## Connector

| Name | Type | URL | Auth |
| --- | --- | --- | --- |
| campium-docs | Streamable HTTP | https://docs.campium.com/_mcp | None (public docs) |

It exposes one read-only tool, `search_documentation`, which runs a hybrid semantic and keyword search over docs.campium.com and returns matching sections with links. No environment variables or accounts are needed.

The plugin only gives guidance. It cannot see or change anything in a Campium account.

## Maintenance

Two reference files are snapshots of the docs site and should be refreshed when pages are added or renamed:

- `skills/campium-navigator/references/docs-index.md`: generated from https://docs.campium.com/llms.txt by `scripts/refresh-docs-index.py` at the repo root.
- `skills/campium-find-report/references/report-catalog.md`: hand-curated grouping of reports by the question they answer.

Search stays the source of truth, so a stale snapshot only affects which page Claude checks first.

After editing, bump `version` in `.claude-plugin/plugin.json` so installed copies pick up the change.
