#!/usr/bin/env python3
"""Regenerate the campium-navigator docs index from https://docs.campium.com/llms.txt.

Run from the repo root:  python3 scripts/refresh-docs-index.py
"""
import re
import urllib.request
from datetime import date
from pathlib import Path

SOURCE = "https://docs.campium.com/llms.txt"
TARGET = Path(__file__).resolve().parent.parent / "plugins/campium-navigator/skills/campium-navigator/references/docs-index.md"


def clean(text: str) -> str:
    # House style: no em or en dashes.
    em, en = "\u2014", "\u2013"
    text = text.replace(f" {em} ", ": ", 1).replace(f" {em} ", ", ").replace(em, "-")
    return text.replace(f" {en} ", " - ").replace(en, "-")


def main() -> None:
    with urllib.request.urlopen(SOURCE, timeout=30) as resp:
        src = resp.read().decode("utf-8")

    out = [
        "# Campium help docs index",
        "",
        f"Snapshot of every page on docs.campium.com ({date.today():%B %Y}), taken from {SOURCE}.",
        "Use it to find which page covers a feature when search results miss. It is a map, not the answer:",
        "always confirm steps with `search_documentation` or by fetching the page, because pages change.",
        "Page links below are the human-readable URLs. Add `.md` to any of them to get the markdown version.",
    ]
    pages = 0
    for line in src.splitlines():
        if line.startswith("## "):
            out += ["", line, ""]
            continue
        m = re.match(r"- \[(.+?)\]\((.+?)\.md\):\s*(.*)", line)
        if not m:
            continue
        title, url, desc = m.groups()
        desc = "" if desc.strip() == "No description found" else clean(desc)
        out.append(f"- [{clean(title)}]({url})" + (f": {desc}" if desc else ""))
        pages += 1

    TARGET.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {pages} pages to {TARGET}")


if __name__ == "__main__":
    main()
