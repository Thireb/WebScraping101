# Guardian (parent) portal requirements

**Demo identity:** `guardiandemo@gmail.com`, child **Steve** `STU-054`  
**Sources:** `raw/landing.html` (guardian panel), `raw/user-manual.md`, `raw/feature-book.md` (Fee Pay mockup)  
**Logged-in verification:** None.

---

## Sign In

Same form as Admin — use **guardian/parent email** from enrolment. **PREVIEW**

---

## Sidebar tree

| Menu label | Route path | Verification |
|------------|------------|--------------|
| Dashboard | UNKNOWN | PREVIEW |
| **Academics** → Lectures Schedule | UNKNOWN | PREVIEW |
| Homework | UNKNOWN | PREVIEW |
| Lesson Plans | UNKNOWN | PREVIEW |
| Quizzes & Exams | UNKNOWN | PREVIEW |
| Class Attendance | UNKNOWN | PREVIEW |
| **Finance** → Fee & Challans | UNKNOWN | PREVIEW |
| Fee Pay | UNKNOWN | PREVIEW |
| **Communication** → Messages | UNKNOWN | PREVIEW |
| **Account** → Student Profile | UNKNOWN | PREVIEW |
| Account Settings | UNKNOWN | PREVIEW |
| Sign Out | UNKNOWN | PREVIEW |

---

## Page: Dashboard

| Element | Detail | Verification |
|---------|--------|--------------|
| Header | Title Dashboard; institute `LMS DEMO`; child switcher `Steve` | PREVIEW |
| Role | Guardian | PREVIEW |
| Greeting | `Good afternoon !` | PREVIEW |
| Timezone | `(UTC+05:00) Islamabad, Karachi (Asia/Karachi)` | PREVIEW |
| Chips | Steve; STU-054 | PREVIEW |
| Quick actions | Lectures, Homework, Lesson Plans, Quizzes, Attendance, Fees | PREVIEW |
| Stat: Total Billed | Rs 600; 0% paid; progress bar | PREVIEW |
| Stat: Amount Paid | Rs 0; Cleared | PREVIEW |
| Stat: Outstanding | Rs 600; 1 pending challan | PREVIEW |
| Stat: Upcoming Classes | 3 in the schedule | PREVIEW |
| Homework Progress | 8 assigned; Submitted `1`; Pending `5`; Overdue `2` | PREVIEW |
| Chart | Monthly Homework Trend (last 6 months) | PREVIEW |

---

## Page: Fee Pay

| Element | Detail | Verification |
|---------|--------|--------------|
| Child selector | top of flow | PREVIEW |
| Bill lines | August fee PKR 8,000; Due date; Status Unpaid | PREVIEW |
| CTA | Pay now / Easypaisa or bank photo | PREVIEW |

---

## Page: Fee & Challans

| Element | Detail | Verification |
|---------|--------|--------------|
| Content | Bills, due dates, paid/unpaid | PREVIEW |

---

## Page: Lectures Schedule / Homework / Attendance / Quizzes

| Element | Detail | Verification |
|---------|--------|--------------|
| Lectures Schedule | Timetable and teacher | PREVIEW (manual menu blurbs) |
| Quizzes & Exams | View scores; student sits exam on student login | PREVIEW |
| Class Attendance | Present/absent for selected child | PREVIEW |

---

## Forms

### Fee Pay — Submit Receipt

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Child | select | yes | PREVIEW |
| Months / year paid for | multi | yes | PREVIEW |
| Amount paid | number | yes | PREVIEW |
| Reference | text | no | office-requested | PREVIEW |
| Payment Receipts | file | yes | JPG, PNG, WEBP, PDF | PREVIEW |
| Submit Receipt | button | — | PREVIEW |

Validation: clear photo; include child name on slip if possible — PREVIEW (manual).

---

## Status values & badges

| Status | Context | Color hint | Verification |
|--------|---------|------------|--------------|
| Unpaid | fee slip | text | PREVIEW |
| Waiting | receipt after submit | manual EN | PREVIEW |
| Approved / Paid | after office action | manual EN | PREVIEW |
| Accepted / Sent back | receipt (Urdu manual) | text | PREVIEW |
| Submitted / Pending / Overdue | homework donut | `ok`, `inf`, `due` classes | PREVIEW |
| 0% paid | billing bar | red/sky stat cards | PREVIEW |

---

## Notifications & email

- Bell icon in header (no count in guardian mockup) — PREVIEW.
- Fee reminder on landing mobile example — PREVIEW.
- WhatsApp notices when institute connected — PREVIEW.

---

## PDF layouts

- Uploaded receipt photo/PDF (guardian-supplied), not a generated challan PDF — PREVIEW.
- Official challan print layout — UNKNOWN.
