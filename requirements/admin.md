# Admin portal requirements

**Role label in UI:** Admin  
**Sources:** `raw/feature-book.md`, `raw/user-manual.md`, `raw/landing.html`, `raw/login.html`  
**Logged-in verification:** None (Cloudflare Turnstile). Items marked **PREVIEW** unless noted.

---

## Sign In (shared entry)

| Field | Type | Required | Options / notes | Verification |
|-------|------|----------|-----------------|--------------|
| Email address (`#email`, `name=email`) | email | yes | autocomplete=email | PREVIEW (`login.html`) |
| Password (`#password`) | password | yes | Show password (`#togglePw`) | PREVIEW |
| Remember me (`#rememberMe`) | checkbox | no | default checked in snapshot | PREVIEW |
| Continue with Google | button | no | OAuth | PREVIEW |
| Sign In → (`#kt_sign_in_submit`) | submit | — | POST `/Account/Login` | PREVIEW |
| Forgot password? | link | — | contact administrator | PREVIEW |
| Create an account | link | — | javascript placeholder | PREVIEW |
| `__RequestVerificationToken` | hidden | yes | anti-forgery | PREVIEW |
| `cf-turnstile-response` | hidden | — | Cloudflare Turnstile | PREVIEW |
| `returnUrl`, `form_render_ts`, `user_website_hp` | hidden | — | honeypot/timing | PREVIEW |

Validation (help text only): red inline message on invalid field; “Fill required fields” (`user-manual.md`).

---

## Sidebar tree (route paths not exposed publicly)

Top bar groups (horizontal in mockup): **Dashboards**, **Institute**, **People**, **Online Lectures**, **Finance**, **Teacher Salary**, **Academic** (badge `7`), **Messages**.

| Menu path | Route path | Verification |
|-----------|------------|--------------|
| Dashboards → Main Dashboard | UNKNOWN | PREVIEW |
| Dashboards → Salary Dashboard | UNKNOWN | PREVIEW |
| Dashboards → Lectures Dashboard | UNKNOWN | PREVIEW |
| Dashboards → Challan Dashboard | UNKNOWN | PREVIEW |
| Institute → Campus | UNKNOWN | PREVIEW (Feature book lists “Campus”; manual “Campus / Branch”) |
| Institute → Classes | UNKNOWN | PREVIEW |
| Institute → Batches | UNKNOWN | PREVIEW |
| Institute → Subjects | UNKNOWN | PREVIEW |
| Institute → Fee Plans | UNKNOWN | PREVIEW |
| People → All Students | UNKNOWN | PREVIEW |
| People → Enrol Student | UNKNOWN | PREVIEW |
| People → Bulk Upload | UNKNOWN | PREVIEW |
| People → Student Attendance History | UNKNOWN | PREVIEW |
| People → Portal Access | UNKNOWN | PREVIEW |
| People → All Teachers | UNKNOWN | PREVIEW |
| People → Add Teacher | UNKNOWN | PREVIEW |
| People → Teacher Lecture History | UNKNOWN | PREVIEW |
| Online Lectures → All Lectures | UNKNOWN | PREVIEW |
| Online Lectures → Add Lecture | UNKNOWN | PREVIEW |
| Online Lectures → Recurring Schedules | UNKNOWN | PREVIEW |
| Online Lectures → Master Meeting | UNKNOWN | PREVIEW |
| Finance → Generate Challan | UNKNOWN | PREVIEW |
| Finance → Challan Records | UNKNOWN | PREVIEW |
| Finance → Process Payment | UNKNOWN | PREVIEW |
| Finance → Receipt Inbox | UNKNOWN | PREVIEW |
| Finance → Daily Report | UNKNOWN | PREVIEW |
| Finance → Monthly Report | UNKNOWN | PREVIEW |
| Finance → Yearly Report | UNKNOWN | PREVIEW |
| Finance → Fee Defaulters | UNKNOWN | PREVIEW |
| Teacher Salary → Salary Plans | UNKNOWN | PREVIEW |
| Teacher Salary → Plan Assignments | UNKNOWN | PREVIEW |
| Teacher Salary → Payroll | UNKNOWN | PREVIEW |
| Teacher Salary → Payment Status | UNKNOWN | PREVIEW |
| Teacher Salary → Payment History | UNKNOWN | PREVIEW |
| Teacher Salary → Advance Salary | UNKNOWN | PREVIEW |
| Teacher Salary → Salary Reports | UNKNOWN | PREVIEW |
| Academic → Course Documents | UNKNOWN | PREVIEW |
| Academic → Homework Approval | UNKNOWN | PREVIEW |
| Academic → Lesson Plan Approval | UNKNOWN | PREVIEW |
| Academic → Quizzes & Exams | UNKNOWN | PREVIEW |
| Academic → Reports Received | UNKNOWN | PREVIEW |
| Academic → Student Leave Approval | UNKNOWN | PREVIEW |
| Academic → Teacher Leave Approval | UNKNOWN | PREVIEW |
| Messages → Inbox | UNKNOWN | PREVIEW |
| Messages → Send Message | UNKNOWN | PREVIEW |
| Messages → Message Monitor | UNKNOWN | PREVIEW |

**Profile / account menu (not sidebar):** Switch Account, Default Portal, Account Settings, Toolbar Settings, Manage Users, Manage Permissions, Manage Zoom API, Google Drive, Select Currency, Appearance (Light / Dark / Auto), Sign Out — PREVIEW (`user-manual.md`).

**Account settings switches (mockup):** Extra helper staff, Alert bell, Your own Zoom, Sign in with Google, On the phone like an app, Your Google Drive — PREVIEW (`feature-book.md`).

---

## Page: Main Dashboard

| Element | Detail | Verification |
|---------|--------|--------------|
| Title / breadcrumb | `Home › Dashboard` | PREVIEW |
| Clock | `Asia/Karachi` (live time in mockup) | PREVIEW |
| Campus hero | `LMS Demo`, `Learning Management System · Admin Portal`, role pill `Admin` | PREVIEW |
| Stat cards | `52` Students (`30 active`); `5` Teachers (`5 active`); `8` Batches (`8 running`); `0` Today (`lectures scheduled`) | PREVIEW |
| Quick actions | Enrol Student, New Lecture, Generate Challan, Live Lecture Monitor | PREVIEW |
| Section 01 Students | Total `52`; chips `30 active` / `22 inactive`; ring `58%`; list rows with avatar, name, `STU-###`, status | PREVIEW |
| Section 02 Teachers | Total `5`; active/inactive; `Add New Teacher` | PREVIEW |
| Row actions | View All (students/teachers) | PREVIEW |
| Filters | Not shown on dashboard | — |

**Student list status badges:** `Active` (on), `Inactive` (off) — PREVIEW.

---

## Page: Receipt Inbox (working example)

| Element | Detail | Verification |
|---------|--------|--------------|
| Title | Receipt inbox; count `2 waiting` | PREVIEW |
| Table rows | Easypaisa photo — Ali Hassan · PKR 5,500; Bank transfer — Raza Family · PKR 8,000 | PREVIEW |
| Row actions | Approve, Reject | PREVIEW |
| Flow hint | Photo → You check → Approve | PREVIEW |

---

## Page: Generate challans (demo block)

| Element | Detail | Verification |
|---------|--------|--------------|
| Form fields | Class (e.g. Grade 9 · Batch A); Fee plan (PKR 8,000 / month); student count | PREVIEW |
| Button | Create 24 fee bills | PREVIEW |
| Summary stats | Collected PKR 4.2M; Still unpaid 142K; Discounts 28K | PREVIEW |

---

## Page: Payroll (demo block)

| Element | Detail | Verification |
|---------|--------|--------------|
| Title | Payroll · Sara Ahmed · August 2026 | PREVIEW |
| Plan toggles | Fixed, Per lecture, Student, Hourly, %, Hybrid | PREVIEW |
| Lines | 18 lectures × PKR 4,500; Advance −10,000; Net PKR 71,000 | PREVIEW |

---

## Page: Messages (mailbox mockup)

| Element | Detail | Verification |
|---------|--------|--------------|
| Folders | Inbox `4`, Sent, Starred, Drafts, Broadcast, Monitor | PREVIEW |
| Actions | Compose, Search messages | PREVIEW |
| Thread list | Ahmad Khan, Sara Teacher, Raza Family, Institute broadcast | PREVIEW |
| Row badges | Student, Teacher, Parent, Broadcast | PREVIEW |
| Compose area | Write a reply… | PREVIEW |

---

## Form: Enrol Student

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Student Name | text | yes | PREVIEW |
| Father Name | text | no | PREVIEW |
| CNIC | text | no | PREVIEW |
| Date of birth | date | no | PREVIEW |
| Gender | select | no | PREVIEW |
| Class | select | no | optional label | PREVIEW |
| Batches | multi-checkbox | yes | PREVIEW |
| Subjects per Batch | per-batch multi | yes | PREVIEW |
| Fee plans | multi | yes | discount optional | PREVIEW |
| Monthly Fee | summary read-only | — | PREVIEW |
| Phones, address, city | text | no | PREVIEW |
| Record status | Active | — | PREVIEW |
| Guardian email / password | login | yes | PREVIEW |
| Student email / password | login | yes | PREVIEW |
| Zoom email | text | no | if institute uses Zoom | PREVIEW |
| Save / Cancel | buttons | — | red validation | PREVIEW |

---

## Form: Add / Edit Teacher

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Name, login | text | yes | PREVIEW |
| Batches | multi | yes | PREVIEW |
| Assign Subjects per Batch | per-batch | yes | PREVIEW |

---

## Form: Add Lecture

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Title, date, time, duration | — | yes | PREVIEW |
| Teacher, batch, subjects | selects | yes | PREVIEW |
| Delivery | Zoom API / Manual Link / In-Person | yes | PREVIEW |

---

## Form: Generate Challan

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Students | multi | yes | PREVIEW |
| Month | — | yes | PREVIEW |
| Due date | date | yes | PREVIEW |
| Generate | button | — | Print optional | PREVIEW |

---

## Form: Process Payment

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Challan lookup | — | yes | PREVIEW |
| Amount, date, method | — | yes | PREVIEW |

---

## Form: Campus / Branch

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Name, address, contact, logo | — | yes | PREVIEW |

---

## Status values & badge colors (observed)

| Status | Context | Color / class | Verification |
|--------|---------|---------------|--------------|
| Active | student/teacher row | `ap-st on` (teal family) | PREVIEW |
| Inactive | student row | `ap-st off` (gray) | PREVIEW |
| Present / Partial / Late / Absent | attendance table | text labels | PREVIEW |
| Approve / Reject | receipt inbox | green/red buttons `ok` / `no` | PREVIEW |
| Unpaid / Paid | fee slip mockups | text | PREVIEW |
| Pending / Approved / Rejected | leave (manual) | not colored in source | PREVIEW |

---

## Notifications & email (described)

- In-app bell on admin nav — PREVIEW.
- Badge on **Academic** menu: `7` — PREVIEW.
- Alerts for lectures, assignments, fee challans, admin updates (landing) — PREVIEW.
- Alert bell can quiet fee/class alerts (account settings) — PREVIEW.
- WhatsApp for passwords/reminders when enabled — PREVIEW (`user-manual.md`).
- Email: Set Portal Password via email/WhatsApp link — PREVIEW; no admin email templates listed.

---

## PDF layouts

| Document | Observed content | Verification |
|----------|------------------|--------------|
| Fee challan | Print after generate; line items not shown | PREVIEW |
| Finance reports | Print/Export with date range | PREVIEW |
| Salary slip | Line items in payroll mockup only | PREVIEW |
| Certificate | Not shown | UNKNOWN |
