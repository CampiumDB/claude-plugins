# Campium plugins for Claude

Plugins that help camps get more out of [Campium](https://campium.com) with Claude, in Cowork or Claude Code.

## Plugins

| Plugin | What it does |
| --- | --- |
| [campium-navigator](plugins/campium-navigator) | Answers "where is" and "how do I" questions, walks you through bigger setup jobs, picks the right report, and helps fix common problems, all from the official [Campium help docs](https://docs.campium.com). |

## Install

### Claude Cowork

1. In the sidebar, open **Customize**, then **Plugins**.
2. Select **Add marketplace** and enter `campiumdb/claude-plugins`.
3. Select **Browse plugins**, find **campium-navigator**, and click **Install**.

To get new versions later, click **Update** on the Campium marketplace.

### Claude Code

Run these in the Claude Code terminal (they don't work in Cowork):

```
/plugin marketplace add campiumdb/claude-plugins
/plugin install campium-navigator@campium
```

No account or API key is needed. The plugin connects to the public Campium docs search at `https://docs.campium.com/_mcp`, and it only gives guidance. It cannot see or change anything in your Campium account.

## Questions

Email support@campium.com.

## Maintaining this repo

- Each plugin lives in `plugins/<name>/` and is listed in `.claude-plugin/marketplace.json`.
- Bump `version` in the plugin's `.claude-plugin/plugin.json` whenever you change it, so installed copies update.
- Refresh the navigator's page list after docs pages are added or renamed: `python3 scripts/refresh-docs-index.py`. The report catalog (`plugins/campium-navigator/skills/campium-find-report/references/report-catalog.md`) is curated by hand.
- Check everything before pushing: `claude plugin validate .`
