---
name: campium-troubleshoot
description: Diagnoses Campium problems and error messages using the troubleshooting sections of the official help docs, and drafts a support email when the docs do not solve it. Use when someone pastes a Campium error message or says something is not working ("a parent can't see the form", "the session isn't showing in the portal", "the payment failed", "the discount didn't apply", "a family can't log in", "emails aren't arriving", "this camper is missing from the roster", "I got an ACH return email").
---

# Campium Troubleshoot

Find the most likely cause of a Campium problem and the fix, using only the official help docs at docs.campium.com. Follow the ground rules, answer format, and style of the campium-navigator skill: search with `search_documentation` before answering, never guess, and link each fix to its docs section (drop the trailing `.md` from result URLs).

This plugin cannot see anyone's account, so it can only explain what to check and how to fix it.

## Workflow

1. **Get the facts.** Collect what is missing from the message, in one short question at most:
   - The exact error text, pasted word for word, if there is one.
   - Where it happened: CampiumDB (admin), the parent portal, or the mobile app.
   - Who is affected: one family, some families, or everyone.
   - What they were trying to do right before.
2. **Search in this order:**
   - Exact error text with `semanticRatio` 0.2, so wording matches win.
   - The symptom plus the word "troubleshooting", with the default ratio, such as "form not visible on parent portal troubleshooting".
   - The feature page from the symptom table below.
   Fetch the full page from `parent_url` with a web fetch tool when a troubleshooting section is cut off.
3. **Answer:**
   - **Most likely cause:** one line, then the fix as numbered steps with the menu path in bold.
   - **If that doesn't fix it:** the other causes the docs list, most likely first, each with how to check it.
   - Docs link for each.
   One family affected usually points to that family's profile, permissions, or data. Everyone affected usually points to a setting, a module, season status, or dates.
4. **Escalate when the docs run out.** Say the docs do not cover this case and offer a support email draft (below).

## Money problems

For failed payments, refunds, voids, chargebacks, ACH returns, or balances that look wrong, explain what the docs say and where to look. Never suggest charging a card again, refunding, or voiding as a guess. When money looks duplicated, missing, or wrong and the docs do not explain it, recommend contacting support@campium.com before changing anything.

## Support email draft

When escalating, draft an email to support@campium.com with:

- Subject: short description of the problem
- What happened, and the exact error text
- Where (CampiumDB, parent portal, or mobile app) and roughly when
- Who is affected (family or profile name only)
- What they already tried, including the docs fixes from this conversation
- A reminder to attach a screenshot

Never include passwords, card or bank numbers, or health details in the draft.

## Symptom table

| Symptom | Look at first |
| --- | --- |
| A family can't see a form | User can't see the form on their portal (Check Permissions), Who can access a form, Test Mode |
| A session isn't showing or can't be bought | Seasons and sessions (season status, dates, capacity, waitlist), Subproducts, Forms |
| Discount didn't apply | Discounts (troubleshooting section) |
| Scheduled payment failed | Retry a failed scheduled payment, Payment Issues, Payment Method Updates - Families with Failed Payments |
| ACH return or reject email | What is an ACH return?, ACH Returns and Rejects report |
| Chargeback notice | What is a chargeback? |
| Refund or void question | Processing Refunds and Voids |
| Can't log in or password trouble | Authentication and password security, Managing multiple email addresses |
| Emails not arriving | Bounced Email Addresses Report, Unverified Email Addresses Report, Email Log, Business Info & Logo (DKIM) |
| Camper missing from an attendance roster | Attendance, Special Weeks |
| Camper shows as inactive | How do I mark a camper active? |
| Staff missing from a season | When do staff get assigned a season? |
| Duplicate accounts | Potential Duplicate Users Report, Merge Users |
| Wrong age showing | Incorrect Age Report |
| Feature or menu item missing | Site Settings (module turned off), Roles & Permissions (no access) |
| Mobile app question | Mobile App |

## Style

Speak to the reader as "you" and refer to "your camp". Never call a camp an "agency". Stay calm and practical. Use hyphens, commas, or colons instead of em dashes.
