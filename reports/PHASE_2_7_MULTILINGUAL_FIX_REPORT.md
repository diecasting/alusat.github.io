# PHASE 2.7 — Multilingual Repair (FIX) Report

**Repository:** diecasting/alusat.github.io
**Date:** 2026-08-28
**Branch:** `feature/alusat-brand-ux-seo-enhancement` (continuation; not yet committed)
**Mode:** IMPLEMENTATION
**Scope:** Multilingual page repair only. No DNS / Cloudflare / redirect / baseURL / canonical / sitemap / Schema / English-URL changes.

---

## 1. Key Engineering Decision (from PHASE 2.7A)

The PHASE 2.7A test revealed a Hugo behavior conflict:

- `translationKey` set **only** on translations → Hugo groups those translations by key but **excludes** the
  English source (keyed by path) → translated pages emit `hreflang` for each other language but **drop the
  reciprocal `en` link** → reciprocal-hreflang requirement FAILS.
- `translationKey` set on **both** EN source + translations → all 5 pages form one translation group →
  reciprocal `en` link is correctly emitted on every translated page.

**Resolution adopted:** `translationKey` is added to BOTH the English source page and its translations
(metadata-only addition; no content, URL, or structure change). This satisfies the explicit `translationKey`
requirement **and** the reciprocal-hreflang requirement. Validated on `industries` before mass-creation.

## 2. Files Created / Modified

### Task 1 — Section 404 repair (16 files)
`translationKey` values: `industries-section`, `materials-section`, `processes-section`, `resources-section`.

| Page | EN source (translationKey added) | Translations (de/ja/fr/es) |
|---|---|---|
| industries | `content/industries/_index.md` ✎ | `_index.{de,ja,fr,es}.md` ✚ |
| materials | `content/materials/_index.md` ✎ | `_index.{de,ja,fr,es}.md` ✚ |
| processes | `content/processes/_index.md` ✎ | `_index.{de,ja,fr,es}.md` ✚ |
| resources | `content/resources/_index.md` ✎ | `_index.{de,ja,fr,es}.md` ✚ |

✎ = existing file edited (translationKey added) · ✚ = new file

### Task 2 — Applications (5 files, new)
`translationKey: "applications"`. New EN page + 4 translations.

- `content/applications/index.md` ✚ (new, OEM-focused: die casting, CNC, precision components, automotive, industrial equipment, consumer products)
- `content/applications/index.{de,ja,fr,es}.md` ✚

### Task 3 — Missing leaf pages (15 files)
`translationKey` values: `manufacturing`, `design-guides`, `faq`. Each mapped to its existing EN source by path.

| Page (slug) | EN source (translationKey added) | Translations |
|---|---|---|
| manufacturing (`/aluminum-extrusion-manufacturing-process/`) | `content/aluminum-extrusion-manufacturing-process/index.md` ✎ | `index.{de,ja,fr,es}.md` ✚ |
| design-guides (`/aluminum-extrusion-design-guide/`) | `content/aluminum-extrusion-design-guide/index.md` ✎ | `index.{de,ja,fr,es}.md` ✚ |
| faq (`/aluminum-extrusion-faq/`) | `content/aluminum-extrusion-faq/index.md` ✎ | `index.{de,ja,fr,es}.md` ✚ |

All translations ≥ 300 characters (verified; Japanese expanded to clear the minimum).

### Task 4 — Blog gap (report only)
- `reports/blog-multilingual-gap.md` ✚ — documents `/de|ja|fr|es/blog/` 404s; blog NOT translated per spec.

## 3. Validation Results

| Check | Result |
|---|---|
| `hugo --environment production --gc --minify` | ✅ EXIT 0 |
| Created multilingual URLs HTTP 200 | ✅ 32/32 (8 page-types × 4 languages) |
| Canonical self-referential | ✅ all sampled pages correct |
| Reciprocal hreflang (translated ↔ en) | ✅ 0 failures (full pairwise) |
| Sitemap inclusion (per-language) | ✅ all 32 URLs present |
| `scripts/schema-check.py ./public` | ✅ PASS (587 files, 0 issues) |
| `scripts/seo-check.py ./public` | ✅ PASS (363 files, 0 issues) |

## 4. Constraints Honored

- ✅ No DNS / Cloudflare / redirect changes
- ✅ `baseURL` unchanged (`https://alusat.com/`)
- ✅ Canonical strategy unchanged (language-scoped, self-referential)
- ✅ Sitemap architecture unchanged (per-language index + root index)
- ✅ Schema architecture unchanged
- ✅ Existing English URLs unchanged (only `translationKey` metadata added)
- ✅ No English duplicate content (translations are native-language, not copies)
- ✅ No WordPress / URL-migration changes

## 5. Remaining Gap (deferred)

- Blog language indexes `/de|ja|fr|es/blog/` still 404 (no translated posts) — reported in
  `reports/blog-multilingual-gap.md`, deferred per Task 4.

## 6. Status

**COMPLETE — STOP before commit.** Awaiting approval to commit/push/PR.
