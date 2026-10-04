# Spec: IGNITE LMS Demo Clone (No Integrations)

## Objective

Build a **self-contained demo** that reproduces the look, navigation, and core workflows of [IGNITE LMS](https://lms.ignitesol.net/) for sales, training, and UI prototyping. The clone must **not** depend on production third-party services (Zoom, Google OAuth/Drive, WhatsApp, payment gateways, Cloudflare Turnstile, or live email).

**Primary users of this document:** coding agents and engineers implementing the demo.

**Success looks like:** A visitor can open the marketing site, sign in as Admin / Teacher / Student / Guardian with demo credentials, walk through the same menus and screens as the reference, and see believable seeded data—with buttons that would call external APIs either **simulated** (toast + local state) or **disabled with “Demo mode”** labels.

---

## Source audit (how this spec was produced)

| Source | URL | Notes |
|--------|-----|--------|
| Marketing landing | `https://lms.ignitesol.net/` | Hero, features, portal previews, pricing, contact |
| Feature book | `/Account/FeatureBook` | Full admin menu tree, module descriptions, UI mockups |
| User manual | `/Account/UserManual` | Step-by-step flows per role (EN + Urdu) |
| Sign-in | `/Account/Login` | Email/password, Google button, Remember me, PWA install |
| Legal | `/Home/Privacy`, `/Home/Terms` | Footer links |
| PWA | `/manifest.json` | Brand colors, icons, standalone display |

**Browse scan limitations:** Automated login from cloud browsers is blocked by **Cloudflare Turnstile** (`cf-turnstile-response` on the login form). Portal interiors were captured from the **public marketing/feature-book previews** and the **user manual**, which mirror authenticated UI. Validate layouts manually with the demo credentials below.

**Reference video (behavior):** [YouTube playlist](https://youtube.com/playlist?list=PLV87tnUqwMzu2hIZc6roOCOPoY5B2DSzP)

---

## Demo credentials (local / staging only)

| Role | Email | Password |
|------|-------|----------|
| Admin | `ignitelms@gmail.com` | `123@` |
| Teacher | `teacherdemo@gmail.com` | `123@` |
| Student | `studentdemo@gmail.com` | `123@` |
| Guardian | `guardiandemo@gmail.com` | `123@` |

**Do not** commit these to production secrets managers; they are public demo accounts on the vendor site.

---

## Product boundaries

### In scope (demo)

- Public marketing site (home, features, portals section, pricing, contact form UI).
- Static **Feature book** and **User manual** pages (can be simplified markdown/HTML copies).
- Four authenticated **portals** with side navigation, dashboards, list/detail patterns, and forms.
- **Seeded relational data** aligned with reference copy (≈52 students, 5 teachers, 8 batches, sample lectures, challans, messages).
- **Mock integrations:** “Join Zoom” opens a modal or `#demo-zoom` placeholder; Google sign-in shows “Demo only”; receipt upload stores file in local/blob storage; payroll/challan “generate” updates in-memory DB.
- **PWA shell:** manifest, theme color, install prompt UI (no real push until backend exists).
- **Role permissions:** Admin vs Sub-admin (helper) menu visibility.
- **Multi-child guardian** switcher on guardian portal.
- **Switch account** when one user has admin + teacher roles (session flag only).

### Out of scope (explicit non-goals)

- Real Zoom / Google Meet / Teams APIs, OAuth, or webhooks.
- Real Google Drive document storage (use uploaded files in demo storage or static PDFs).
- WhatsApp Business API, SMS, or email delivery (log to console / show “sent” toast).
- Payment processing (cards, Easypaisa API); Fee Pay = upload + admin approve workflow only.
- Cloudflare Turnstile / bot protection on demo login (use simple rate limit or none).
- Multi-tenant SaaS billing, super-admin panel, or institute onboarding pipelines.
- Production-grade security audit, PCI, or FERPA compliance.

### Always do (agents)

- Match **navigation labels** and hierarchy to the reference manual.
- Use **role-based routing** so each portal only exposes allowed menus.
- Keep **demo data** consistent across portals (same student names, challan amounts, lecture times).
- Show **Asia/Karachi** timezone on dashboards where the reference does.
- Run lint/build before claiming a milestone done.

### Ask first

- Changing the chosen web stack or auth library.
- Adding real external API keys.
- Storing uploaded files outside the demo environment.

### Never do

- Ship vendor demo passwords in client-side bundles for non-demo environments.
- Call `lms.ignitesol.net` APIs from the clone (no coupling to vendor backend).

---

## Brand and UX system

Extracted from live site / PWA:

| Token | Value |
|-------|--------|
| Theme color | `#005e78` |
| Background (PWA) | `#083A3D` |
| Product name | IGNITE LMS |
| Tagline | Online Learning Management System |
| Typography / layout | KeenThemes Metronic-style bundles (`/assets/plugins/global/plugins.bundle.js`, `/assets/js/scripts.bundle.js`) |

**UI patterns (repeat everywhere):**

1. **Left sidebar** — collapsible on mobile (hamburger); section groups with badges for pending counts.
2. **Top bar** — institute name (“LMS Demo”), breadcrumb (`Home › Dashboard`), date/time, profile menu.
3. **Stat cards** — large number + subtitle (e.g. `52` Students, `30 active`).
4. **Quick actions** — pill buttons: Enrol Student, New Lecture, Generate Challan, Live Lecture Monitor.
5. **Tables** — search, filters (class, batch, date, status), pagination.
6. **Forms** — required field validation with red inline errors; Save / Cancel.
7. **Empty states** — friendly copy when lists are empty (demo should rarely show empty main lists).

**Languages:** Reference manual is bilingual EN + Urdu. Demo v1 can be **English-only** with optional i18n hooks.

---

## Public site map

| Route | Purpose |
|-------|---------|
| `/` | Landing: hero, feature grid, portal screenshots, pricing, testimonials, contact |
| `/Account/Login` | Sign-in |
| `/Account/FeatureBook` | Long-form feature tour (can be static) |
| `/Account/UserManual` | Role-based help (can be static) |
| `/Home/Privacy` | Privacy policy |
| `/Home/Terms` | Terms of service |

**Landing CTAs:** Sign In, Get Started (scroll to contact), Feature book, User manual, WhatsApp link (`+92 302 4884029`).

**Contact form fields:** Full name*, Institute name*, Phone*, Email, Website, Message* → in demo, POST to local endpoint and show success banner (no email).

---

## Authentication (demo implementation)

**Reference behavior:**

- Email + password form (`#email`, `#password`, Remember me, Show password).
- Optional **Continue with Google** (hide or stub in demo).
- Forgot password → message to contact administrator (no self-service).
- First-time **Set Portal Password** flow for some users (wizard: password + confirm).
- After login → redirect to role default dashboard.

**Suggested demo approach:**

- Session cookie or JWT with claims: `{ userId, role, instituteId, linkedRoles[] }`.
- Hard-coded user table matching demo emails above.
- **No Turnstile** on demo login.
- `Switch Account` toggles `activeRole` in session (admin ↔ teacher).

---

## Roles and personas

| Role | Internal key | Default landing |
|------|----------------|-----------------|
| Institute admin | `admin` | Main dashboard |
| Sub-admin / Helper | `subadmin` | Same as admin with restricted menus |
| Teacher | `teacher` | Teacher dashboard |
| Student | `student` | Student dashboard |
| Guardian / Parent | `guardian` | Guardian dashboard |

**Sub-admin:** Same UI as admin; `Manage Permissions` defines visible menu IDs (demo: one preconfigured helper with fees hidden).

**Guardian:** Must use **guardian email**, not student email. **Child switcher** in header drives all child-scoped pages.

---

## Navigation trees (authoritative menu structure)

### Admin / Sub-admin sidebar

Grouped as on reference Feature book:

**Dashboards**

- Main Dashboard
- Salary Dashboard
- Lectures Dashboard
- Challan Dashboard

**Institute**

- Campus / Branch
- Classes (names only)
- Batches (names only)
- Subjects (names only)
- Fee Plans

**People**

- All Students
- Enrol Student
- Bulk Upload
- Student Attendance History
- Portal Access
- All Teachers
- Add Teacher
- Teacher Lecture History

**Online Lectures**

- All Lectures
- Add Lecture
- Recurring Schedules
- Master Meeting (demo: “connected” badge only)

**Finance**

- Generate Challan
- Challan Records
- Process Payment
- Receipt Inbox
- Daily / Monthly / Yearly Reports
- Fee Defaulters

**Teacher Salary**

- Salary Plans
- Plan Assignments
- Payroll
- Payment Status
- Payment History
- Advance Salary
- Salary Reports

**Academic / Approvals**

- Course Documents
- Homework Approval
- Lesson Plan Approval
- Quizzes & Exams (admin view)
- Reports Received
- Student Leave Approval
- Teacher Leave Approval

**Messages**

- Inbox
- Send Message
- Message Monitor
- Broadcast (optional demo)

**Account menu (profile)**

- Switch Account, Default Portal, Account Settings, Toolbar Settings
- Manage Users, Manage Permissions
- Manage Zoom API (demo stub), Google Drive (demo stub)
- Select Currency, Appearance (Light/Dark/Auto), Sign Out

### Teacher sidebar

- Dashboard
- **Academics:** My Lectures, Create Lecture, Schedule Recurring, Schedule, Lecture History
- **Documents**
- **Planning:** Lesson Plans, Homework, Submit Report
- **Assignments**
- **Quizzes & Exams**
- **Messages** (badge count)
- **People:** My Students
- **Leave:** Apply Leave
- **Finance:** My Salary
- **Account:** My Profile, Account Settings, Sign Out

**Teacher dashboard widgets:** Welcome banner, upcoming class countdown, stats (lectures, students, batches, subjects), quick actions (New Lecture, Schedule, Quizzes, Profile).

### Student sidebar

- Dashboard
- **Academics:** My Lectures, My Attendance, Leave Requests, Homework, Lesson Plans, Assignments, Quizzes & Exams, Documents
- **Messages**
- **Finance:** Fee Details
- **Account:** My Profile, Settings, Sign Out

**Student dashboard widgets:** Attendance %, homework completion %, upcoming lectures, fee summary (Total Billed / Paid / Due), pending challans.

### Guardian sidebar

- Dashboard
- **Academics:** Lectures Schedule, Homework, Lesson Plans, Quizzes & Exams, Class Attendance
- **Finance:** Fee & Challans, Fee Pay
- **Communication:** Messages
- **Account:** Student Profile, Account Settings, Sign Out

**Guardian dashboard:** Child selector, billed/paid/outstanding, homework progress (submitted/pending/overdue), upcoming classes count.

---

## Core domain model (demo seed)

Use these entities in a normalized schema (names illustrative):

```
Institute, Campus, ClassLabel, Batch, Subject
User (role flags), StudentProfile, TeacherProfile, GuardianProfile
StudentBatch, StudentBatchSubject, TeacherBatchSubject
FeePlan, StudentFeePlan, Challan, Payment, ReceiptSubmission
Lecture, RecurringSchedule, AttendanceRecord
Homework, HomeworkSubmission, LessonPlan, DailyReport
Assignment, Quiz, Question, QuizAttempt
SalaryPlan, PayrollRun, SalaryPayment, Advance
LeaveRequest (student|teacher)
MessageThread, Message
Document (metadata; file in blob store)
PortalAccessRule (block student portal if defaulter)
Notification (in-app bell)
```

**Reference demo numbers (marketing/admin preview):**

- Students: 52 total (30 active, 22 inactive)
- Teachers: 5 (all active)
- Batches: 8 running
- Sample student: Steve (STU-054), guardian-linked
- Sample teacher: Hassan Akram (TCH-001), `teacherdemo@gmail.com`
- Sample fees: Rs 600 billed, 0% paid, 1 pending challan (student/guardian views)

**Linking rule (critical business logic):** Classes, batches, and subjects are **independent lists**. Links are created only on **enrol student** / **add teacher** by selecting batches then subjects per batch.

---

## Screen inventory by workflow

### Admin — first-week setup (from user manual)

1. Campus / Branch — name, address, contact, logo
2. Classes / Batches / Subjects — CRUD name-only lists
3. Fee Plans — name + amount
4. Add Teacher → batches → subjects per batch → login
5. Enrol Student → personal info, optional class label, batches, subjects per batch, fee plans, contacts, guardian + student logins
6. Zoom stub + Master Meeting stub
7. Create test lecture + test challan

### Admin — daily operations

| Workflow | Key screens | Demo behavior |
|----------|-------------|---------------|
| Dashboard | KPI cards, recent students/teachers, shortcuts | Read-only + links |
| Enrol student | Multi-step form | Creates DB rows |
| Schedule lecture | Add Lecture / Recurring | Creates lecture rows; Zoom link = `https://demo.zoom/...` |
| Live monitor | Lectures Dashboard | Shows “Live” badge on mock lecture |
| Generate challan | Pick month/class/students | Bulk insert challans |
| Receipt inbox | Approve/Reject photos | State machine: Waiting → Approved/Rejected |
| Process payment | Office cash entry | Marks challan paid |
| Approvals | Homework, lesson plans, leave, reports | Approve/reject with comment |
| Payroll | Run payroll | Computes from seed rules; PDF = generated stub |
| Portal access | Block/unblock student | Toggle flag; student sees blocked page |
| Messages | Inbox, compose, monitor | Threaded UI; no external send |

### Teacher workflows

| Workflow | Steps |
|----------|--------|
| Start class | My Lectures → Start Class Now → mock Zoom modal |
| Whiteboard | Open Whiteboard → static canvas or third-party lib |
| Attendance | Auto from mock Zoom + manual override |
| Homework | Create → students submit → review |
| Quiz | Question bank → assign → auto-grade MCQ |
| Leave | Apply → pending until admin approves |

### Student workflows

| Workflow | Steps |
|----------|--------|
| Join class | My Lectures → Join Class (enabled when host “started”) |
| Homework / assignments | Submit files before due date |
| Quiz | Timed UI; warn on tab leave in “exam mode” |
| Fees | View only; payment via guardian |
| Blocked portal | Full-page message when `portalAccess=false` |

### Guardian workflows

| Workflow | Steps |
|----------|--------|
| Child switch | Header dropdown changes `activeStudentId` |
| Fee pay | Select challan → amount → upload receipt → Waiting |
| View academics | Read-only mirrors student data for selected child |

---

## Messages module (all roles)

Mailbox folders: **Inbox, Sent, Starred, Drafts, Trash** (+ **Broadcast** / **Monitor** for admin).

Compose: select recipient, body, optional attachment (demo storage).

**Demo:** no real email; admin “Monitor” can list all threads.

---

## Integrations → demo stubs

| Integration | Reference UI | Demo replacement |
|-------------|--------------|------------------|
| Zoom API | Start/join lecture, attendance sync | `window.open('#')` or embedded “Demo meeting” page; attendance button seeds records |
| Google Sign-In | Login button | Toast: “Google sign-in disabled in demo” |
| Google Drive | Course documents | Local `/uploads` or S3-compatible bucket |
| WhatsApp invites | Enrolment | Copy link modal only |
| Cloudflare Turnstile | Login | Omit |
| Push notifications | PWA | In-app bell only |
| Stripe/cards | N/A on vendor Fee Pay | Not needed |

---

## Suggested tech stack (agent default)

Pick one stack and stay consistent:

**Option A — Full-stack TypeScript (recommended for agents)**

- Next.js 15 App Router (marketing + portals via route groups)
- Auth: Auth.js / Lucia with credentials provider
- DB: SQLite (dev) or PostgreSQL via Prisma
- UI: Tailwind + shadcn/ui (theme tuned to `#005e78`)
- File uploads: local disk or MinIO

**Option B — SPA + API**

- Vite + React Router
- FastAPI or NestJS backend
- Same data model as above

**Commands (example Option A):**

```bash
npm install
npm run dev          # http://localhost:3000
npm run build
npm run lint
npx prisma migrate dev
npm run db:seed      # load demo fixtures
```

---

## Project structure (example)

```
apps/web/
  app/
    (marketing)/          # public pages
    (auth)/login/
    (portals)/
      admin/[...]/
      teacher/[...]/
      student/[...]/
      guardian/[...]/
  components/             # shared UI
  lib/auth/
  lib/demo/               # mock zoom, receipts
packages/database/
  prisma/schema.prisma
  seed.ts                 # 52 students, etc.
docs/
  ignite-lms-demo-rebuild-spec.md   # this file
```

---

## Implementation phases (agent tasks)

### Phase 0 — Scaffold

- [ ] Repo, lint, env example, README with demo logins
- [ ] DB schema + seed script matching demo counts
- [ ] Auth + role guards

### Phase 1 — Marketing shell

- [ ] Landing page sections paralleling reference
- [ ] Login page (no Turnstile)
- [ ] Static Feature book + User manual (or markdown render)

### Phase 2 — Admin portal

- [ ] Sidebar + main dashboard
- [ ] Institute CRUD (campus, class, batch, subject, fee plan)
- [ ] People: enrol student, add teacher, list views
- [ ] Lectures: add + list + recurring (UI only)
- [ ] Finance: generate challan, receipt inbox, process payment

### Phase 3 — Teacher portal

- [ ] Dashboard + My Lectures + start class mock
- [ ] Homework, lesson plans, quizzes (CRUD + student visibility rules)

### Phase 4 — Student + Guardian

- [ ] Student dashboard + join lecture + submissions
- [ ] Guardian child switcher + fee pay upload + attendance views

### Phase 5 — Cross-cutting

- [ ] Messages
- [ ] Notifications bell
- [ ] Portal block page
- [ ] Switch account (admin/teacher)
- [ ] PWA manifest + icons
- [ ] Dark mode toggle

### Phase 6 — Polish

- [ ] Responsive pass (mobile sidebar)
- [ ] Empty/error states
- [ ] Demo banner: “Integration simulated”

---

## Testing strategy

| Level | What to verify |
|-------|----------------|
| Manual smoke | Each role login → open every sidebar link → no 404 |
| E2E (Playwright) | Admin enrol student → guardian sees fee → upload receipt → admin approves |
| Visual | Spot-check dashboards against reference screenshots on marketing site |
| Data | Seed totals match dashboard KPIs |

---

## Success criteria (acceptance)

1. All four demo accounts sign in and land on the correct dashboard.
2. Admin sidebar contains **all menu groups** listed in this spec (sub-admin variant hides configured items).
3. Enrol student flow persists and appears in All Students; guardian linked student shows on guardian dashboard.
4. Generate challan creates records visible on student Fee Details and guardian Fee & Challans.
5. Teacher can create homework; student can submit; teacher sees submission.
6. Lecture join/start uses **mock** meeting (no external network requirement).
7. Receipt inbox approve/reject updates challan/payment state.
8. No outbound calls to Zoom, Google, or `lms.ignitesol.net` during normal demo use.
9. Marketing home + login visually align with reference (colors, layout hierarchy, portal previews).

---

## Open questions

1. Should the clone include **Urdu** copy in v1 or English-only?
2. Is **Sub-admin** required in the first milestone or can it wait until admin permissions UI exists?
3. Should Feature book / User manual be **verbatim copies** (legal/branding) or rewritten summaries?
4. Target deployment: local Docker only, or a public demo URL?

---

## Appendix A — Reference contact & links

- Demo site: https://lms.ignitesol.net/
- Vendor: https://www.ignitesol.net/
- Support phone: 0302-4884029
- Email: info@ignitesol.net
- Pricing shown on site: Basic Rs 5,000/mo, Premium Rs 8,000/mo (marketing only for clone)

---

## Appendix B — Agent browsing notes

When re-scanning the live site:

```bash
export PATH="$HOME/.local/bin:$PATH"
browse open https://lms.ignitesol.net/Account/Login --session ignite --remote
browse snapshot --session ignite
```

Use `--local` only if Chrome is installed. Login automation may fail on Turnstile; use manual headed session or vendor credentials in a real browser for portal screenshots.

**Public scrape without login:**

```bash
browse cloud fetch https://lms.ignitesol.net/Account/FeatureBook
```

---

*Document version: 2026-10-04 — generated from live site scan + Feature book + User manual.*
