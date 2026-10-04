# Unknowns (not confirmed from sources)

## Authentication & routes

- Exact URL paths for authenticated portal pages (sidebar items are labels only in public HTML).
- Post-login redirect URL per role.
- Whether admin/teacher/student/guardian use separate host paths or shared controller routes.
- **VERIFIED** blocked: could not complete login (Cloudflare Turnstile on `/Account/Login`).

## UI detail gaps

- Table column sets for **All Students**, **All Teachers**, **Challan Records**, **Payroll**, quiz lists, etc.
- Pagination, sort, and export formats beyond “Print or Export” on finance reports.
- Full field lists for **Add Teacher**, **Add Lecture**, **Generate Challan**, **Process Payment**, **Salary Plans**, quiz builder, homework builder (only partial fields in User manual).
- Exact validation message strings (only generic “red message” / required fields).
- Badge color hex for every status (only partial from mockup CSS classes).
- **Certificate** PDF layout and issue rules.
- Full **challan** and **salary slip** PDF templates (only line-item mockups).
- **Broadcast** / **Message Monitor** screen layout.
- **Master Meeting**, **Manage Zoom API**, **Google Drive** connection screens.
- **Bulk Upload** Excel template column list (manual: do not change headings; columns not listed).
- **Toolbar Settings**, **Default Portal**, **Appearance** option lists beyond Light/Dark/Auto.

## Status vocabulary

- Mapping between EN (**Waiting**, **Approved**, **Reject**) and Urdu manual (**Accepted**, **Sent back**, **Mark invalid**) for receipts.
- Full enum for challan payment states, homework approval states, quiz attempt states.
- Whether **Receipt still Submitted** (help table) equals **Waiting**.

## Notifications & email

- Email templates, triggers, and subjects (not documented).
- Push notification payload and settings UI (only mentioned on landing).

## Integrations

- Zoom attendance sync edge cases, Meet/Teams behavior.
- Automatic receipt approval toggle (mentioned as optional; UI not shown).
- Fee reminder automation content and schedule.

## Sub-admin

- Whether sub-admin is a distinct role flag or permission-only; no separate portal mockup (same as admin with fewer menus).

## Demo vs production

- Whether preview stats (52 students, Hassan Akram, Steve, Rs 600) match logged-in demo data.
