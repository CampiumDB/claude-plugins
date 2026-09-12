---
name: campium-walkthrough
description: Builds a step-by-step checklist for a multi-part Campium task from the official help docs, and can guide someone through it one step at a time. Use when someone wants to be walked through setting something up end to end ("walk me through setting up summer registration", "step by step, how do I launch a registration form", "help me set up payment plans", "get my season ready for families", "onboarding checklist for our camp", "how do I start taking donations").
---

# Campium Walkthrough

Turn a bigger Campium job into an ordered checklist the person can follow, built only from the official help docs at docs.campium.com. Follow the ground rules, answer format, and style of the campium-navigator skill: search with `search_documentation` before stating any step, never guess menu paths, and link every step to its docs section (drop the trailing `.md` from result URLs).

## Workflow

1. **Understand the goal.** Confirm what "done" looks like (for example "families can register and pay for Summer 2027 sessions"). Ask at most one question, and only if the answer changes the plan, such as "Is this a brand-new camp or are you copying last season?"
2. **Find the main guide first.** Search for an end-to-end guide before the individual steps. Check the anchor guides table below. Fetch the full page from the result's `parent_url` with a web fetch tool when available, because walkthrough pages rely on step order.
3. **Fill in each step.** For every step the main guide mentions only briefly, search for its own page or section so the checklist has the real field names and choices.
4. **Build the checklist** in the format below.
5. **Offer to go one step at a time.** After showing the overview, offer to guide them through it. In that mode, give one step, wait for them to say it is done or ask a question, then give the next. When they hit a problem, switch to the campium-troubleshoot approach for that step, then continue.

## Checklist format

```
## Goal: <what will be true when finished>

### Before you start
- Decisions to make up front (dates, prices, deposits, who can register, etc.)
- Anything that must already be on (modules in Site Settings, payment processor approved, permissions)

### Step 1: <short name>
**Where:** Menu → Path
1. Action with the exact **Button** or **Field** label
2. ...
Why it matters / what to pick, only if the docs give guidance.
Docs: [Page: Section](link)

### Step 2: ...

### Check that it worked
- How to confirm from the docs, such as previewing a form with Test Mode or viewing the parent portal as a family would.
```

Keep each step to what the docs support. Mark steps that depend on earlier ones ("do this after the season exists"). When the docs give a recommended order, keep it.

If the person asks for a copy to print or share with their team, write the checklist to a document file.

## Anchor guides

Start with these pages, then search for each step's details.

| Goal | Start with | Then usually |
| --- | --- | --- |
| Get a season ready for registration | Guided Season Setup, Quickstart for Campium Admins | Seasons and sessions, Subproducts, Forms, Payment Plans, Discounts, Test Mode |
| Copy last season forward | Manage Seasons, Seasons and sessions (copy a session) | Guided Season Setup, Transfer Season Balances |
| Take payments | Payment Processors, Payment Methods | Payment Plans, Tiered pricing, Cancellation Fees |
| Launch a form | Forms, Who can access a form | Profile Fields, Digital Signatures, Test Mode, Email users that have not completed a form |
| Hire staff | Staff Applications, Staff Hub | References, Manage contracts, Sex Offender Registry Check, CampiumDB Users |
| Give staff admin access | CampiumDB Users, Roles & Permissions | Allow a staff user to see a report |
| First day of camp | Attendance, Attendance Kiosk | My Groups, Pickup Privileges Report, Transportation, Bunk Assignments |
| Health and medications | Medications & health | Health Report, Profile Fields |
| Communicate with families | Email in Campium, Mass Emails | Email Templates, SMS, Send push notifications, Manage portal news |
| Accept donations | Donations and fundraising, Donation pages | Manage donors |
| Camp store or canteen | Canteen | Adding canteen funds for a user, Product Quantities, Food & Per-Day Ordering |
| Set up the parent portal | Portal Settings, Business Info & Logo | Site Settings, FAQ, Legal Documents |
| End of season cleanup | Season Recap, Transfer Season Balances | Zero Out Season Credits, Combined Season Invoices |

## Style

Speak to the reader as "you" and refer to "your camp". Never call a camp an "agency". Use hyphens, commas, or colons instead of em dashes. Do not estimate how long steps take.
