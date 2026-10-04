# Sub-admin / Helper portal requirements

**Role labels in UI:** Helper / Sub-admin, “same role · only what you allow” (Feature book role desk).  
**Sources:** `raw/feature-book.md`, `raw/user-manual.md`  
**Logged-in verification:** None.

Sub-admin uses the **same portal shell as Admin** with menus restricted via **Manage Permissions** (`user-manual.md` § Extra / Sub-admin).

---

## Sign In

Same form as Admin — see `requirements/admin.md` (Sign In). **PREVIEW**

---

## Sidebar tree

Identical menu **labels** to Admin (`requirements/admin.md` sidebar table).  
**Route paths:** UNKNOWN for all items. **PREVIEW**

**Difference:** Only ticked menus appear. Examples from manual:

- Finance allowed, Salary hidden.
- People allowed, Permissions hidden.

**Verification:** PREVIEW (documentation only; no permission matrix captured).

---

## Pages

Inherit page specs from **Admin** for any menu that remains visible. No separate mockup.

| Page | Notes | Verification |
|------|-------|--------------|
| Manage Users | Profile → add email + password | PREVIEW |
| Manage Permissions | Tick menus for helper | PREVIEW |

---

## Forms

### Manage Users

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Email | email | yes | PREVIEW |
| Password | password | yes | PREVIEW |

### Manage Permissions

| Field | Type | Required | Verification |
|-------|------|----------|--------------|
| Menu toggles | checkbox per menu | — | PREVIEW |

---

## Status, notifications, PDF

Same as Admin where applicable. Sub-admin cannot access unticked modules (expected missing menu — help text). **PREVIEW**
