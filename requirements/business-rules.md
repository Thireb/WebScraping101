# Business rules (extracted)

Sources: `raw/feature-book.md`, `raw/user-manual.md`, `raw/landing.html` mockups.  
**Verification:** All rules below are **PREVIEW** (public docs/mockups). None confirmed on a logged-in session.

## Institute data model

| ID | Rule |
|----|------|
| BR-01 | `Classes`, `Batches`, and `Subjects` are independent name lists under **Institute**. |
| BR-02 | Class/batch/subject links are created on **Enrol Student** or **Add/Edit Teacher** via batch selection then **Subjects per Batch** (or **Assign Subjects per Batch**). |
| BR-03 | **Class** on enrolment is an optional label (e.g. Grade 9); it does not attach batches. |
| BR-04 | One campus per institute (Feature book setup copy). |

## Portal access & blocking

| ID | Rule |
|----|------|
| BR-10 | **Portal Access** can block a student from the student portal (e.g. unpaid fees). |
| BR-11 | Automatic blocking of fee defaulters can be turned on/off; individual students can be exempted. |
| BR-12 | Blocked student sees a blocked message until access is restored (manual/help text). |
| BR-13 | Guardian must sign in with **guardian email** from enrolment, not student email. |
| BR-14 | Guardian with multiple children must select child at top; pages are scoped to selected child. |
| BR-15 | Student and parent emails must stay separate (different portals). |
| BR-16 | **Sub-admin / Helper** sees only menus ticked in **Manage Permissions** (e.g. Finance without Salary). |

## Fees & receipts

| ID | Rule |
|----|------|
| BR-20 | **Generate Challan**: pick students, month, due date → generates bills (bulk). |
| BR-21 | **Process Payment**: office records cash/transfer against a challan (amount, date, method). |
| BR-22 | **Fee Pay** (guardian): pay outside the site (bank/Easypaisa, etc.), then upload proof; no in-site card payment described. |
| BR-23 | Receipt submission initial status: **Waiting** (EN); office uses **Receipt Inbox** → **Approve** or **Reject** (optional message). |
| BR-24 | Urdu manual also names guardian outcomes **Accepted** / **Sent back** (and **Mark invalid** in one admin step list). |
| BR-25 | After approval, **Fee & Challans** should show **Paid** (EN manual). |
| BR-26 | Fee plans attach at enrolment; discounts on student; **Monthly Fee** shown in summary. |
| BR-27 | **Select Currency** (profile menu) controls amount symbol. |

## Lectures & attendance

| ID | Rule |
|----|------|
| BR-30 | Lecture delivery modes: **Zoom API**, **Manual Link**, **In-Person**. |
| BR-31 | Zoom API requires **Manage Zoom API** + **Master Meeting** setup. |
| BR-32 | **Recurring Schedules** create weekly (or custom) series; single **Add Lecture** for one-off. |
| BR-33 | Teacher **Start Class Now** opens Zoom; attendance tracked by LMS, not Zoom email. |
| BR-34 | Student may use any Zoom account; attendance tied to student login. |
| BR-35 | After Zoom, attendance auto-fills: **Present**, **Partial**, **Late**, **Absent** (by time in room). |
| BR-36 | Unknown Zoom display names require **Match** (or **Ignore**) to a student. |
| BR-37 | **Take Manual Attendance** when auto sync misses someone. |
| BR-38 | Student **Join Class** / **Join Now** when host started; **Waiting for Host** until teacher starts. |
| BR-39 | **Live Lecture Monitor** / **Lectures Dashboard** shows live/upcoming classes. |

## Academic workflows

| ID | Rule |
|----|------|
| BR-40 | **Lesson Plans**: teacher submits; students see after office approval if institute requires it. |
| BR-41 | **Homework**: teacher sets; student submits before **Due** date; teacher reviews submissions. |
| BR-42 | **Submit Report** (daily): office approves under **Report Approval** / **Reports Received**. |
| BR-43 | **Assignments**: longer work; filters pending/submitted/graded/missed. |
| BR-44 | Quizzes: saved question bank; **Live now** status lets students start; MCQ auto-mark; written answers teacher-marked. |
| BR-45 | Exam mode: leaving page may be reported; some exams require full screen. |
| BR-46 | **Course Documents**: institute Google Drive; optional download lock (preview only). |

## Leave

| ID | Rule |
|----|------|
| BR-50 | Student/teacher **Apply Leave** with dates + reason → **Pending** until **Approved** or **Rejected**. |
| BR-51 | Teacher leave shows days used vs allowance (example: 2 of 12). |
| BR-52 | On teacher leave approval, clashing classes listed: **Reschedule**, **Reassign** (salary follows new teacher), or **Cancel**. |

## Payroll

| ID | Rule |
|----|------|
| BR-60 | Salary plan types shown: **Fixed** (Monthly), **Per lecture**, **Student** (Enrolment), **Hourly**, **%** (Fee share), **Hybrid**. |
| BR-61 | Example calculation: `lectures × rate − advance = net payable` (18 × PKR 4,500 − 10,000 = PKR 71,000 in mockup). |
| BR-62 | Flow: **Salary Plans** → assign → **Payroll** → **Advance Salary** → **Payment Status** → **Salary Reports** (print). |

## Messaging & notifications

| ID | Rule |
|----|------|
| BR-70 | In-app **bell**; badge counts on **Messages**, **Approvals**, **Receipts**, **Academic** (admin mockup badge `7`). |
| BR-71 | Mailbox folders: **Inbox**, **Sent**, **Starred**, **Drafts**, **Trash**; admin also **Broadcast**, **Monitor**. |
| BR-72 | Alerts described for lectures, assignments, fee challans, admin updates (landing copy); fee/class alerts can be quieted (account settings mockup). |
| BR-73 | WhatsApp: optional institute integration for passwords/reminders; requires correct phone on records + enablement. |
| BR-74 | No specific transactional email templates observed in sources (only “email or WhatsApp” for Set Portal Password). |

## Account / roles

| ID | Rule |
|----|------|
| BR-80 | **Switch Account** for users with both office and teacher roles without re-login. |
| BR-81 | **Forgot password?** → contact administrator; no self-reset for most users. |
| BR-82 | **Set Portal Password** flow for some new users (password + confirm). |
| BR-83 | First-time office setup checklist order: Campus → Classes → Batches → Subjects → Fee Plans → Teachers → Students → Zoom → test lecture + challan. |

## PDF / print

| ID | Rule |
|----|------|
| BR-90 | Challans: **Print** after generate (manual). |
| BR-91 | Finance reports: **Print** or **Export** with date range. |
| BR-92 | Salary: **Salary Reports** print; payroll mockup shows slip lines (not full PDF layout). |
| BR-93 | Whiteboard: export **PDF**; course files may be PDF with download allowed/locked. |
| BR-94 | **Certificate** mentioned on marketing journey; no certificate PDF layout in Feature book / User manual. |
