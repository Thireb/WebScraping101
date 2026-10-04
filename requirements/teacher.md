# Teacher portal requirements

**Demo identity in mockup:** Hassan Akram, `TCH-001`, `teacherdemo@gmail.com`  
**Sources:** `raw/landing.html` (teacher panel), `raw/user-manual.md`  
**Logged-in verification:** None.

---

## Sign In

Same as Admin — `requirements/admin.md`. **PREVIEW**

---

## Sidebar tree

| Menu label | Route path | Verification |
|------------|------------|--------------|
| Dashboard | UNKNOWN | PREVIEW |
| **Academics** → My Lectures | UNKNOWN | PREVIEW |
| Create Lecture | UNKNOWN | PREVIEW |
| Schedule Recurring | UNKNOWN | PREVIEW |
| Schedule | UNKNOWN | PREVIEW |
| Lecture History | UNKNOWN | PREVIEW |
| Documents | UNKNOWN | PREVIEW |
| **Planning** → Lesson Plans | UNKNOWN | PREVIEW |
| Homework | UNKNOWN | PREVIEW |
| Submit Report | UNKNOWN | PREVIEW |
| **Assignments** → Assignments | UNKNOWN | PREVIEW |
| **Quizzes & Exams** → Quizzes & Exams | UNKNOWN | PREVIEW |
| **Messages** → Messages | UNKNOWN | PREVIEW (badge `2` in mockup) |
| **People** → My Students | UNKNOWN | PREVIEW |
| **Leave** → Apply Leave | UNKNOWN | PREVIEW |
| **Finance** → My Salary | UNKNOWN | PREVIEW |
| **Account** → My Profile | UNKNOWN | PREVIEW |
| Account Settings | UNKNOWN | PREVIEW |
| Sign Out | UNKNOWN | PREVIEW |

---

## Page: Dashboard

| Element | Detail | Verification |
|---------|--------|--------------|
| Header clock | e.g. `Sun, 16 Aug · 02:00 PM` | PREVIEW |
| Notifications | Bell badge `2` | PREVIEW |
| Welcome | `Welcome back, Hassan!` + `Active` pill | PREVIEW |
| Meta | `TCH-001`, `teacherdemo@gmail.com` | PREVIEW |
| Subject/batch chips | Math, Computer, Python learning, Computer-Morning, Math-Evening, Physics, `+1 more` | PREVIEW |
| Timezone block | Date/time `GMT+5`, `Asia/Karachi` | PREVIEW |
| Quick actions | New Lecture, Schedule, Quizzes, Profile | PREVIEW |
| Upcoming class card | ID `998877`; countdown; Computer / Computer-Morning; Tomorrow 03:00 PM – 04:00 PM; 60 min; Zoom | PREVIEW |
| Card actions | Open lecture, Details, Schedule | PREVIEW |
| Stat cards | Total Lectures `12` (1 today · 3 upcoming); My Students `48` (4 batches); Batches `4`; Subjects `6` | PREVIEW |

---

## Page: My Lectures (behavior)

| Element | Detail | Verification |
|---------|--------|--------------|
| Tabs | Today, Upcoming (manual also Past, All) | PREVIEW |
| Lecture card actions | Start Class Now, Open Whiteboard, Take Manual Attendance | PREVIEW |
| States | Starting soon; You are the host; Waiting for Host (student-facing) | PREVIEW |

---

## Page: Create Lecture / Schedule

| Element | Detail | Verification |
|---------|--------|--------------|
| Fields | Title, date, time, duration, batch, subjects | PREVIEW |
| Delivery | Zoom API, Manual Link, In-Person | PREVIEW |
| Recurring | Schedule Recurring for weekly timetable | PREVIEW |
| Calendar | Schedule page shows calendar | PREVIEW |

---

## Page: Homework / Assignments / Quizzes

| Element | Detail | Verification |
|---------|--------|--------------|
| Homework | New Homework; submissions list | PREVIEW |
| Assignments | Create; grade + feedback | PREVIEW |
| Quizzes | Saved questions; New quiz; Live now; auto-grade MCQ | PREVIEW |

---

## Page: My Salary

| Element | Detail | Verification |
|---------|--------|--------------|
| Content | Pay slips / history (manual) | PREVIEW |

---

## Forms

### New Homework

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Title, instructions | text | yes | PREVIEW |
| Subject, batch | select | yes | PREVIEW |
| Specific students | optional | no | PREVIEW |
| Due date | date | yes | PREVIEW |
| Worksheet | file | no | PREVIEW |

### Apply Leave

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Dates | date range | yes | PREVIEW |
| Reason | text | yes | PREVIEW |
| Submit | button | — | PREVIEW |

### Create Lecture

Same fields as Admin Add Lecture — PREVIEW.

---

## Status values & badges

| Status | Context | Verification |
|--------|---------|--------------|
| Active | teacher hero pill `tpv-active` | PREVIEW |
| Pending / Approved / Rejected | leave | PREVIEW (manual) |
| Submitted / Pending | homework submissions | PREVIEW (feature book) |
| Live now | quiz | PREVIEW |

---

## Notifications & email

- Bell count `2` on dashboard — PREVIEW.
- Messages badge on menu — PREVIEW.
- No teacher-specific email templates listed — UNKNOWN.

---

## PDF layouts

- Whiteboard export PDF — PREVIEW (manual).
- My Salary slip print layout — UNKNOWN (not shown).
