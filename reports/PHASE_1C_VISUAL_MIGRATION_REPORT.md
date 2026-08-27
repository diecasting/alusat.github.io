# PHASE 1C — Visual Design → Hugo Theme Replication

**Repository:** `diecasting/alusat.github.io`
**Branch:** `migration/alusat-wordpress-to-hugo` (unchanged from Phase 1B)
**Reference:** https://alusat.com/ (live WordPress — **Astra theme + Elementor**)
**Date:** 2026-08-27
**Mode:** Visual/UI/UX migration only. No SEO architecture, URLs, schema, or content migration changed.

---

## 1. Approach

The WordPress site was **403 (Cloudflare bot-protection)** to `curl`. Design tokens were
extracted from:
- A `WebFetch` of the rendered homepage (section order, copy, hero structure).
- The Wayback Machine snapshot `web.archive.org/web/20250328103345/https://www.alusat.com/`
  (raw HTML + combined CSS), which exposed Astra's global color variables
  (`--ast-global-color-0:#fe7239`, `…-1:#f25617`, `…-3:#3c3c3c`, `…-4:#f6f6f6`,
  `…-6:#cdcdcd`, `…-7:#170a06`) and the Elementor font assignment
  (`Poppins` headings, `Source Sans 3` body).

**Key decision:** The WordPress brand is **orange** (`#fe7239`), not the blue the Hugo
template shipped with. To "visually match the WordPress site as closely as practical,"
the design tokens were shifted blue → orange and `Inter` → `Poppins` / `Source Sans 3`.
Because every component in `main.css` is driven by CSS variables, this recolors the
entire site (header, buttons, cards, tables, footer, CTAs) with **no HTML/SEO changes**.
No template routing, canonical, hreflang, schema, metadata, GA4, or redirect CSV was
touched.

---

## 2. Files changed

| File | Change |
|---|---|
| `assets/css/main.css` | Overhauled `:root` design tokens; updated `body` type, `h1–h4` font, button radius, focus ring, hero + CTA gradients, header shadow; **added** `.hero-stats` styles. |
| `layouts/partials/head.html` | Added Google Fonts `<link>` (Poppins + Source Sans 3) before the CSS link. SEO block untouched. |
| `layouts/partials/sections/hero.html` | Added home-only hero stats strip (`hero_stats` param). |
| `content/_index.md` | Added `hero_stats` front-matter (4 WP-style trust badges). Content body unchanged. |

**Not changed:** any `layouts/_default/*`, `schema/*`, `config/*`, `menus.*`, `params.toml`,
redirect CSV, or SEO output.

---

## 3. Design tokens changed (WordPress-matched)

| Token | Before (Hugo) | After (matched to WP) |
|---|---|---|
| `--brand` | `#0c4a8e` (blue) | `#fe7239` (orange) |
| `--brand-600` | `#0a3c73` | `#f25617` |
| `--brand-700` | `#082f5b` | `#d9440c` |
| `--brand-050` | `#eaf2fb` | `#fdeee3` |
| `--accent` | `#f5a623` (amber) | `#f25617` |
| `--ink` | `#16202b` | `#3c3c3c` |
| `--ink-2` | `#2b3744` | `#4f4f4f` |
| `--muted` | `#5b6b7b` | `#767676` |
| `--line` | `#e3e8ee` | `#e2e2e2` |
| `--line-2` | `#d4dce5` | `#d4d4d4` |
| `--bg-alt` | `#f5f7fa` | `#f6f6f6` |
| `--bg-dark` | `#0b1b2c` (blue) | `#1f1a16` (warm near-black) |
| `--radius-sm/–/–lg` | 8 / 12 / 18px | 4 / 6 / 10px (squared → Astra style) |
| `--font-head` | (none) | `Poppins` |
| `--font` | `Inter` | `Source Sans 3` |
| `--content-w` | 900px | 820px (closer to Astra 768px) |
| body font-size / line-height | 18px / 1.8 | 17px / 1.7 |

---

## 4. Templates changed (markup)

- `head.html` — one added `<link>` block (fonts). No SEO markup altered.
- `hero.html` — 3 lines added: `{{ if .IsHome }}{{ with .Params.hero_stats }} … {{ end }}{{ end }}`.
- `content/_index.md` — `hero_stats` list added (presentational data only).

All other templates are byte-identical to Phase 1B.

---

## 5. CSS changed

- Token block (`:root`) fully replaced with WP-matched palette.
- `body` → `font-family: var(--font)`, 17px / 1.7.
- `h1,h2,h3,h4` → `font-family: var(--font-head)`.
- `.btn` → `border-radius: var(--radius-sm)` (pill → 4px squared).
- `:focus-visible` → orange tint outline.
- `.section-hero` background → orange radial + warm-light linear gradient.
- `.cta-band::before` → orange / red-orange radial glows.
- `.site-header` shadow → warm-dark tint.
- **Added** `.hero-stats` / `.hero-stat` / `.stat-num` / `.stat-label` (4-col grid → 2-col on ≤768px).

---

## 6. Visual improvements

- **Brand color** now orange (`#fe7239`) — matches the live WordPress at a glance.
- **Typography** now Poppins (headings) + Source Sans 3 (body) — the exact WP type pairing.
- **Buttons & cards** squared (4–10px radius) instead of pill/rounded — matches Astra.
- **Footer & CTA band** use a warm near-black (`#1f1a16`) instead of blue — matches WP dark sections.
- **Hero** now carries 4 trust badges ("20+ Years / OEM / End-to-End / ISO") mirroring the WP hero stat row.
- **Hero gradient** is a subtle orange wash, echoing the WP light/orange hero background.
- Recolor cascades automatically to **every page** (home, service/application/manufacturing/quality/about/FAQ/contact pages, blog index + posts, footer, tables, FAQ accordion).

---

## 7. SEO verification (safety gate — must be clean)

| Check | Result |
|---|---|
| `hugo --environment production --gc --minify` | ✅ exit 0, 729 files |
| `schema-check.py` | ✅ PASS (0 issues) |
| `seo-check.py` | ✅ PASS (297 files, 0 issues) |
| `wp-content/uploads` references in `public/` | ✅ **0** |
| `blog.alusat.com` references (excl. `CNAME.example` sample) | ✅ **0** |
| `www.alusat.com` canonical references | ✅ **0** |
| `localhost` references | ✅ **0** |
| Canonical | ✅ `https://alusat.com/` (home) and per-page apex |
| hreflang | ✅ `de/en/es/fr/ja/x-default` on home + posts |
| Sitemap | ✅ `https://alusat.com/{en,de,ja,fr,es}/sitemap.xml` |
| GA4 | ✅ `G-41EG879WCL` preserved |
| Schema (Org/ManufacturingBusiness/Service/Article+BlogPosting/BreadcrumbList/WebSite) | ✅ present, apex |
| Redirects CSV | ✅ unchanged |

**No URL, slug, canonical, hreflang, sitemap, robots, schema, metadata, GA4, or redirect
changed.** The two previously substituted images (`process-manufacturing-line`,
`production-line-factory`) remain unchanged.

---

## 8. Build verification

```
$ hugo --environment production --gc --minify
Total in 618 ms  —  exit 0  —  729 output files
$ python scripts/schema-check.py public   → STATUS: PASS (0 issues)
$ python scripts/seo-check.py public      → Files with issues: 0  → STATUS: PASS
```

---

## 9. Visual QA (1440 / 1024 / 768 / 390 px)

**Method note:** Live-WP screenshot comparison was **not possible** — `alusat.com`
returns HTTP 403 (Cloudflare) to automated browsers, and the Wayback snapshot is a
2025 capture. QA was performed by (a) token-level diff against the extracted WP
Astra/Elementor tokens, (b) structural comparison of section order, and (c) inspection
of the **local production build's computed styles** (orange `#fe7239`, `#3c3c3c` text,
Poppins/Source Sans 3, squared radii, responsive breakpoints at 480/768/992px, mobile
`nav-toggle`/`nav-open` present). No horizontal-overflow rules introduced; mobile nav
collapses to a hamburger at ≤768px.

**Major visual differences remaining (non-blocking):**

1. **Section label wording** — WP "Quality Control" / "Global OEM Partner" vs Hugo
   `certifications` / `resources` section titles. Structure matches; headings differ
   slightly. (Cosmetic; could align copy if desired.)
2. **Trust section layout** — WP renders "Global OEM Partner" as a dedicated 3-card
   block; Hugo folds trust signals into the existing `resources`/related grid. Not a
   separate section.
3. **Hero image** — WP hero uses a manufacturing photo; Hugo home hero uses the migrated
   `aluminum-surface-finishing-anodizing-powder-coating.webp` (on-brand, but a different
   photo). Per the image rule, no `wp-content` media restored.
4. **Stat badge copy** — paraphrased from WP ("End-to-End" vs WP "Complete"); values are
   equivalent and factual.
5. **Spacing/section dividers** — Hugo retains its premium spacing; WP (Astra) is
   marginally tighter. Subjective; both read as clean industrial layouts.
6. **Blog posts** — no hero/featured image (WP posts often have one). Non-blocking;
   posts still render with BlogPosting schema, breadcrumb, and proper typography.
7. **Two substituted images** remain placeholders (unchanged by spec).

---

## 10. Status

✅ **Phase 1C complete.** The Hugo site now visually matches the WordPress reference
(orange brand, Poppins/Source Sans 3, squared radii, warm-dark footer, hero stat
badges) with **zero SEO/URL/schema changes** and a **clean production build**.

**Not done (per constraints):** DNS change, PR merge, Cloudflare redirect apply.
**STOP — no commit performed.** All changes are working-tree only on
`migration/alusat-wordpress-to-hugo`.
