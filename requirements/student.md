# Student portal requirements

**Demo identity in mockup:** Steve, roll `N/A`, student login separate from guardian  
**Sources:** `raw/landing.html` (student panel), `raw/user-manual.md`  
**Logged-in verification:** None.

---

## Sign In

Same form as Admin — use **student email** (not guardian). **PREVIEW**

---

## Sidebar tree

| Menu label | Route path | Verification |
|------------|------------|--------------|
| Dashboard | UNKNOWN | PREVIEW |
| **Academics** → My Lectures | UNKNOWN | PREVIEW |
| My Attendance | UNKNOWN | PREVIEW |
| Leave Requests | UNKNOWN | PREVIEW |
| Homework | UNKNOWN | PREVIEW |
| Lesson Plans | UNKNOWN | PREVIEW |
| Assignments | UNKNOWN | PREVIEW |
| Quizzes & Exams | UNKNOWN | PREVIEW |
| Documents | UNKNOWN | PREVIEW |
| Messages | UNKNOWN | PREVIEW |
| **Finance** → Fee Details | UNKNOWN | PREVIEW |
| **Account** → My Profile | UNKNOWN | PREVIEW |
| Settings | UNKNOWN | PREVIEW |
| Sign Out | UNKNOWN | PREVIEW |

---

## Page: Dashboard

| Element | Detail | Verification |
|---------|--------|--------------|
| Title | Student Dashboard | PREVIEW |
| Welcome | `Welcome back, Steve!` | PREVIEW |
| Meta | Roll: N/A; Rs; Asia/Karachi - UTC +5 | PREVIEW |
| Quick actions | Lectures, Homework, Quizzes, Fees | PREVIEW |
| Tiles | Attend. `36%`; HW Done `12%`; Upcoming `1`; Fee Paid `0%` | PREVIEW |
| Strip | Upcoming `1`; Pending HW `7`; Due `Rs 600`; Attendance `36%`; UTC+5 Karachi | PREVIEW |
| Upcoming lecture | ID `998877`; Computer; Hassan Akram; Tomorrow 03:00 PM – 04:00 PM; Online class | PREVIEW |
| Actions | Join open soon, Details | PREVIEW |
| Fee KPIs | Total Billed Rs 600 (0% paid); Total Paid Rs 0; Amount Due Rs 600; Pending Challans `1` | PREVIEW |

---

## Page: My Lectures

| Element | Detail | Verification |
|---------|--------|--------------|
| Tabs | Today, Upcoming, Past, All | PREVIEW |
| Filter | By subject | PREVIEW |
| Actions | Join Class, Join Now, Board / Open Whiteboard | PREVIEW |
| State | Waiting for Host | PREVIEW |

---

## Page: Homework / Assignments / Quizzes

| Element | Detail | Verification |
|---------|--------|--------------|
| Homework | Submit + attachments before Due | PREVIEW |
| Assignments | Filters: pending, submitted, graded, missed | PREVIEW |
| Quiz | Start/Resume; Time left; Come back later; Submit; exam mode warnings | PREVIEW |

---

## Page: Fee Details

| Element | Detail | Verification |
|---------|--------|--------------|
| Content | Bills view-only; payment via guardian portal | PREVIEW |

---

## Page: Portal blocked

| Element | Detail | Verification |
|---------|--------|--------------|
| Trigger | Unpaid fees / Portal Access | PREVIEW (manual) |
| Message | blocked message (text not quoted in source) | PREVIEW |

---

## Forms

### Homework submit

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Answer text | textarea | no | PREVIEW |
| Files / photos | file | yes | PREVIEW |
| Submit | button | before Due | PREVIEW |

### Leave Requests

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Start / end dates | date | yes | PREVIEW |
| Reason | text | yes | PREVIEW |

---

## Status values & badges

| Status | Context | Verification |
|--------|---------|--------------|
| Cleared / Due | fee KPI labels `ok`, `due` | PREVIEW |
| Join open soon | lecture CTA disabled state | PREVIEW |
| Pending / graded / missed | assignments | PREVIEW |

---

## Notifications & email

- Bell badge `1` in mockup header — PREVIEW.
- Fee reminders mentioned on landing mobile cards — PREVIEW.
- Set Portal Password via email/WhatsApp — PREVIEW.

---

## PDF layouts

- Download course PDFs when allowed — PREVIEW.
- Certificate (marketing journey) — UNKNOWN layout.
