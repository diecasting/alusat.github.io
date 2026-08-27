# WordPress vs Hugo — Visual Design Audit

**Phase:** 1C — Visual Design → Hugo Theme Replication
**Date:** 2026-08-27
**Reference site:** https://alusat.com/ (live WordPress — Astra theme + Elementor)
**Hugo repo:** `diecasting/alusat.github.io` (branch `migration/alusat-wordpress-to-hugo`)

**Method:** Live WP was behind Cloudflare bot-protection (HTTP 403 to `curl`). Design
tokens were extracted from (a) a `WebFetch` of the rendered homepage (structure,
section order, copy) and (b) the Wayback Machine snapshot
`web.archive.org/web/20250328103345/https://www.alusat.com/` (raw HTML + combined CSS),
which exposed Astra's global color variables and Elementor font assignment.

> **Key finding:** The WordPress site uses an **orange industrial brand** (`#fe7239`),
> not the blue the Hugo template currently ships with. To "visually match the WordPress
> site as closely as practical," the Hugo design tokens must shift from blue → orange
> and from `Inter` → `Poppins` / `Source Sans 3`. This is the single biggest visual gap.

---

## 1. Structural comparison (Hugo already mirrors WP section order)

| Area | WordPress (alusat.com) | Current Hugo | Match? |
|---|---|---|---|
| Header | Sticky white bar, logo left, primary menu right, language switch | Sticky white bar, logo mark + wordmark left, menu right, `EN/DE/JA/FR/ES` switch | ✅ structure |
| Nav | Horizontal dropdown menu | Horizontal dropdown menu (`nav-item-has-children`) | ✅ |
| Hero | Eyebrow + H1 + intro + CTA + 4 stat badges; light gradient bg | Eyebrow + H1 + intro + dual CTA; light gradient bg; no stat badges | ⚠️ missing stat badges |
| Service sections | "Manufacturing Services" 5 cards; "Capability" 4 numbered steps; "Process" 4 steps | `capabilities` (cards) `process` (steps) | ✅ |
| Industries | 6 cards (Automotive, Industrial, Architecture, Electronics, Solar, Consumer) | `industries` 6 cards | ✅ |
| Quality | Inspection list + 3 sub-cards | `certifications` | ⚠️ label differs |
| Trust | "Global OEM Partner" 3 cards | `resources` / not explicit | ⚠️ |
| Knowledge | 4 article links | `resources` | ✅ |
| FAQ | Accordion | `faq` accordion | ✅ |
| Inquiry CTA | RFQ form / contact CTA | `cta-band` + `rfq` | ✅ |
| Footer | Dark, multi-column (brand / nav / resources / contact / legal) | Dark, multi-column (brand / nav / resources / contact / legal) | ✅ structure |

The **HTML structure is already WP-faithful**. The visual gap is almost entirely
**color, type, radius, and spacing** — i.e. the CSS design-token layer. No template
restructure is required for SEO safety; changes are confined to `assets/css/main.css`
plus a font `<link>` in `head.html`.

---

## 2. Design token table

| token | wordpress_reference | current_hugo | recommended_hugo |
|---|---|---|---|
| Primary / brand | `#fe7239` (orange) | `#0c4a8e` (industrial blue) | `#fe7239` |
| Brand hover (600) | `#f25617` (red-orange) | `#0a3c73` | `#f25617` |
| Brand active (700) | `#d94a0c` (derived) | `#082f5b` | `#d9440c` |
| Brand tint (050) | `#fdeee3` (derived light orange) | `#eaf2fb` (light blue) | `#fdeee3` |
| Accent | `#f25617` | `#f5a623` (amber) | `#f25617` |
| Body text | `#3c3c3c` | `#16202b` | `#3c3c3c` |
| Secondary text | `#4f4f4f` (derived) | `#2b3744` | `#4f4f4f` |
| Muted text | `#767676` | `#5b6b7b` | `#767676` |
| Border | `#e2e2e2` (≈ WP `#cdcdcd`) | `#e3e8ee` | `#e2e2e2` |
| Border strong | `#d4d4d4` | `#d4dce5` | `#d4d4d4` |
| Page background | `#ffffff` | `#ffffff` | `#ffffff` |
| Alt background | `#f6f6f6` | `#f5f7fa` | `#f6f6f6` |
| Dark (footer/CTA) | `#1f1a16` (warm near-black, WP `#170a06` vibe) | `#0b1b2c` (dark blue) | `#1f1a16` |
| Heading font | `Poppins` | `Inter` | `Poppins` |
| Body font | `Source Sans 3` | `Inter` (fallback stack) | `Source Sans 3` |
| Base font-size | 16–18px (Astra ~16–17px body) | 18px | 17px |
| Line-height (body) | ~1.7 | 1.8 | 1.7 |
| H1 size | ~38–44px | clamp 34–54px | clamp 2.2–3.2rem (~35–51px) |
| H2 size | ~28–32px | clamp 26–34px | clamp 1.7–2.1rem (~27–34px) |
| Container width | 1200px (Astra default) | 1200px | 1200px |
| Content width (posts) | 768px (Astra) | 900px | 820px |
| Header height | ~70px | 72px | 72px |
| Button radius | 2px (Astra default, near-square) | 999px (pill) | 4px (squared, close to WP) |
| Card radius | 0–3px (Astra) | 12px | 6px |
| Large radius | — | 18px | 10px |
| Shadow | subtle (Astra ~`0 1px 3px rgba(0,0,0,.08)`) | layered, stronger | keep subtle |
| Section padding | ~70–90px vertical | clamp 56–96px | clamp 60–90px |
| CTA band | dark, centered text + button | dark, text left + button right | keep (functional) |
| Hover state | color darken + slight lift | color darken + lift | color darken + lift (recolored) |
| Logo | text wordmark "ALUSAT" + tagline | mark "AL" + wordmark + tagline | keep mark (recolor gradient) |

---

## 3. Element-level gaps to close

| Element | WP reference | Current Hugo | Action |
|---|---|---|---|
| Buttons | squared (2px), orange fill, white text | pill, blue fill | set `--radius` small; recolor to orange |
| Headings | Poppins 600–700 | Inter 700 | load Poppins, set `--font-head` |
| Body | Source Sans 3 | Inter | load Source Sans 3, set `--font` |
| Eyebrow chips | orange tint pill | blue tint pill | recolor to `--brand-050` |
| Cards | light border, subtle shadow, orange title | blue title | recolor titles to `--brand` |
| Stat badges (home hero) | 4 orange-accented stats | absent | optional add (reuses existing copy) |
| Footer | warm dark `#170a06` | dark blue `#0b1b2c` | recolor to warm near-black |
| Table header | brand fill | brand fill (blue) | recolor to orange |
| Links | orange on hover | blue on hover | recolor to orange |
| Focus ring | brand tint | brand tint (blue) | recolor to orange tint |

---

## 4. Conclusion of audit

The Hugo template is structurally WP-faithful (sections, nav, footer, blog, schema).
The dominant visual divergence is the **brand color (blue → orange)** and **typeface
(Inter → Poppins + Source Sans 3)**, followed by **radius (pill → squared)** and
**footer hue (blue → warm black)**. All of these are expressible as CSS design tokens
with **zero changes to HTML structure, URLs, or SEO output**.

**Recommended implementation (SEO-safe):** edit `assets/css/main.css` token block +
selective rules, and add a Google Fonts `<link>` (Poppins + Source Sans 3) to
`layouts/partials/head.html`. No template markup, routing, canonical, hreflang,
schema, or GA4 changes.
