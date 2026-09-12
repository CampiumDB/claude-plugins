---
name: campium-find-report
description: Picks the right Campium report for a question and explains where to find it, which filters to set, and how to read it, using the official help docs. Use when someone asks which report shows something or wants data out of Campium ("who still owes money", "how much did we make this summer", "which campers are missing forms", "how full is each session", "who's on the waitlist", "list of campers with allergies for week 3", "what report shows our deposits", "compare this year to last year").
---

# Campium Find Report

Match a question to the best Campium report and explain how to run it. Campium has more than 70 built-in reports plus custom reports, and the names do not always say what they answer, so shortlist from the catalog first, then confirm with the docs. Follow the ground rules and style of the campium-navigator skill: confirm details with `search_documentation` before answering and link to the docs (drop the trailing `.md` from result URLs).

This plugin cannot run reports or see anyone's data. It tells the person which report to open and what to look for.

## Workflow

1. **Turn the question into a data request.** Who or what (families, campers, staff, sessions, payments), which season, what date range, and how it should be grouped. Ask one short question only if the answer changes which report to use, such as "For one season, or across all seasons?"
2. **Shortlist from `references/report-catalog.md`.** It groups every documented report by the question it answers. Pick the best match, plus one or two alternatives when they answer a different angle.
3. **Confirm with the docs.** Search for the chosen report by name to get where it lives, its filters, and its columns. Fetch the full page from `parent_url` with a web fetch tool when you need the column list.
4. **Nothing fits?** Point to custom reports (build one with filters and display fields) or the Matrix Report for counts across two fields. Search the Create and use custom reports page for how to set the filters they need.
5. **Answer** in the format below.

## Answer format

```
**Report:** <name>
**Where:** Menu → Path
**Set:** the filters to choose (season, dates, session, status...)
**Look at:** the columns that answer the question, and what they mean
**Then:** export, email, or other actions the docs mention, if useful
Docs: [Report name](link)

Also useful: <alternative> for <different angle>.
```

## Choosing between similar reports

Several money reports sound alike. When the question touches balances or revenue, say why the chosen one fits:

- **Account Balance**: what each family owes right now for one season, next to their scheduled payments.
- **Aging Account Balance**: how balances built up over a date range, for chasing older unpaid amounts.
- **Family Ledger**: every charge, payment, and credit for a family, as a running ledger.
- **Revenue Summary**: gross and net revenue and discounts for one season.
- **Revenue by Season**: all seasons side by side.
- **Rolling Revenue**: day-by-day revenue across seasons, to compare registration pace.

For enrollment, **Product Rollup** answers "how full is each session", while **Session Enrollee** lists the people in one session.

## Reports that change data

Transfer Season Balances and Zero Out Season Credits change family balances. When recommending one, tell the person to use the preview first, as the docs describe, and to contact support@campium.com if unsure.

## Style

Speak to the reader as "you" and refer to "your camp". Never call a camp an "agency". Use hyphens, commas, or colons instead of em dashes.
