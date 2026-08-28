# Blog Multilingual Gap Report

**Repository:** diecasting/alusat.github.io
**Date:** 2026-08-28
**Phase:** 2.7 — Task 4 (Blog language handling — report only, no translation)
**Mode:** READ-ONLY analysis

---

## 1. Current State

| URL | Status | Notes |
|---|---|---|
| `https://alusat.com/blog/` | ✅ 200 | English blog index renders (≈17 KB) |
| `https://alusat.com/de/blog/` | ❌ 404 | No German blog posts / index |
| `https://alusat.com/ja/blog/` | ❌ 404 | No Japanese blog posts / index |
| `https://alusat.com/fr/blog/` | ❌ 404 | No French blog posts / index |
| `https://alusat.com/es/blog/` | ❌ 404 | No Spanish blog posts / index |

The English blog is generated from `content/posts/` (or equivalent EN blog source). Hugo only emits a
per-language blog index (`/de/blog/`, etc.) when at least one blog post exists for that language. Because
no translated blog posts exist, the localized blog URLs return 404.

## 2. Root Cause

- Blog posts are English-only.
- The four language menu files (`menus.de/es/fr/ja.toml`) do **not** link to `/<lang>/blog/`, so the 404s
  are not triggered by menu navigation — they occur only on direct access or future internal links.
- This is an expected content gap, not a structural/configuration defect.

## 3. Impact

- Low. The blog is not referenced from any multilingual menu, so end users following the navigation will
  not hit these 404s.
- SEO risk: if internal links or sitemaps ever expose `/<lang>/blog/`, crawlers would see 404s. Currently
  the per-language sitemaps do **not** include blog indexes, so no crawl penalty is expected.

## 4. Recommendations (out of scope for Phase 2.7)

| Option | Effort | Effect |
|---|---|---|
| **A. Translate blog posts** | High | Full multilingual blog; localized indexes auto-generated. Proper but content-heavy. |
| **B. Generate empty language blog indexes** | Low | Create `content/posts/_index.<lang>.md` stubs so `/<lang>/blog/` returns 200 with a localized "coming soon" message. Avoids 404s without full translation. |
| **C. Leave as-is** | None | Accept the gap; ensure no internal/menu links point to `/<lang>/blog/`. |

**Recommended:** Option B if 404 avoidance is desired before a full blog translation program (Option A).
Phase 2.7 deliberately does **not** translate the blog; this gap is deferred to a dedicated blog-localization phase.

## 5. Verification

- `hugo --environment production --gc --minify` → exit 0.
- Confirmed `/blog/` 200; `/de|ja|fr|es/blog/` 404 in built `public/`.
- No changes made to blog configuration, DNS, Cloudflare, redirects, or canonical/sitemap strategy.
