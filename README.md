# Campium plugins for Claude

Plugins that help camps get more out of [Campium](https://campium.com) with Claude, in Cowork or Claude Code.

## Plugins

| Plugin | What it does |
| --- | --- |
| [campium-navigator](plugins/campium-navigator) | Answers "where is" and "how do I" questions, walks you through bigger setup jobs, picks the right report, and helps fix common problems, all from the official [Campium help docs](https://docs.campium.com). |

## Install

### Claude Cowork

Add this marketplace in your plugin settings using the repository `campiumdb/claude-plugins`, then install **campium-navigator**.

### Claude Code

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
