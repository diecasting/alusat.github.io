# Schema Before / After Analysis — Phase 2.5 (Brand · UX · SEO · GEO)

**Site:** `alusat.com` (Hugo multilingual, EN/DE/JA/FR/ES)
**Branch:** `feature/alusat-brand-ux-seo-enhancement`
**Date:** 2026-08-27
**Scope:** Structured-data (`application/ld+json`) entities emitted across the site, before vs. after Phase 2.5.

---

## 1. Baseline (Before Phase 2.5)

The site emitted a **minimal, article-centric** schema set:

| Entity (`@type`) | Where | Notes |
|---|---|---|
| `Organization` | Homepage + every page (publisher) | Company identity only; no manufacturing specifics. |
| `Product` | Service / product pages | Thin — no manufacturing process, materials or geo context. |
| `WebSite` | Homepage | Sitelinks searchbox absent; alternateName only. |
| `BlogPosting` | Blog posts | Standard article schema. |

**Gaps in the baseline**
- No `LocalBusiness` / `ManufacturingCompany` → search engines could not infer the company is a *manufacturer* (die casting, CNC, extrusion, OEM).
- No `PostalAddress` / `GeoCoordinates` → no GEO / local-search signal for Dongguan, Guangdong, China.
- No `knowsAbout` / `areaServed` → weak entity/AI-search disambiguation.
- No `BreadcrumbList` → weaker internal hierarchy signal.
- No `FAQPage` on qualifying pages.

---

## 2. After Phase 2.5

| Entity (`@type`) | Where | New? | Why it matters |
|---|---|---|---|
| `Organization` | All pages | — | Rebranded to **YuanZhong Technology Co., Limited**; `legalName`, `url`, `logo` from `config/branding/schema.toml`. |
| `LocalBusiness` | Homepage | ✅ | Explicit local-business entity; distinct `@id #local-business` from `#organization`. |
| `ManufacturingCompany` | Homepage | ✅ | Tells Google/Bing the entity *manufactures* — unlocks manufacturer knowledge-panel eligibility. |
| `ManufacturingBusiness` | Homepage | ✅ | Additional manufacturer subtype from `manufacturing.html` for redundancy/coverage. |
| `WebSite` | Homepage | — | `alternateName: "YuanZhong"`, `publisher` → `#organization`. |
| `Service` | Service pages (`/services/*`) | — | Service offering with `areaServed` / `provider`. |
| `Product` | Product pages | — | Retained. |
| `BlogPosting` | Blog posts | — | Retained. |
| `BreadcrumbList` | All non-homepage pages | ✅ | Clear URL hierarchy for crawlers and rich results. |
| `FAQPage` | Pages with `schema.faq` (e.g. Contact) | ✅ | Eligible for FAQ rich results. |
| `Place` + `PostalAddress` + `GeoCoordinates` | Homepage (geo-entity) | ✅ | **GEO signal**: `addressLocality: Dongguan`, `addressRegion: Guangdong`, `addressCountry: CN`, `streetAddress: No.238 Guanbi Street`. |
| `ItemList` / `ListItem` | Homepage | ✅ | Service/capability enumeration. |

### Homepage `LocalBusiness` / `ManufacturingCompany` key fields
```json
{
  "@type": ["LocalBusiness", "ManufacturingCompany"],
  "@id": "https://alusat.com/#local-business",
  "name": "YuanZhong Technology Co., Limited",
  "legalName": "YuanZhong Technology Co., Limited",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "No.238 Guanbi Street",
    "addressLocality": "Dongguan",
    "addressRegion": "Guangdong",
    "addressCountry": "CN"
  },
  "knowsAbout": [
    "Aluminum Die Casting", "CNC Machining", "Aluminum Extrusion",
    "Surface Finishing", "OEM Manufacturing", "Precision Metal Components"
  ],
  "areaServed": ["Worldwide", "North America", "Europe", "Asia"],
  "parentOrganization": { "@id": "https://alusat.com/#organization" }
}
```

---

## 3. SEO / GEO / AI-Search Benefits

| Benefit | Mechanism | Impact |
|---|---|---|
| **Manufacturer entity clarity** | `ManufacturingCompany` + `knowsAbout` (die casting, CNC, OEM) | Higher chance of manufacturer knowledge panel; better query intent match for "aluminum die casting manufacturer / OEM supplier". |
| **Local & GEO discovery** | `PostalAddress` (Dongguan/Guangdong/CN) + `GeoCoordinates` | Eligible for local/map and regional ("near Dongguan") queries; stronger China + export signal. |
| **AI-answer grounding** | Explicit `knowsAbout`, `areaServed`, `description` with "YuanZhong … Dongguan, Guangdong, China" | LLM/AI-overview retrievers get clean, disambiguated entity facts. |
| **Crawl hierarchy** | `BreadcrumbList` on every subpage | Better internal linking comprehension; breadcrumb rich results. |
| **Rich-result eligibility** | `FAQPage` + `BreadcrumbList` + `LocalBusiness` | FAQ snippets, breadcrumb snippets, local business panel. |
| **Brand consistency** | Single source of truth in `config/branding/*.toml` → `params.toml` | Every page's `Organization`/`LocalBusiness` shares identical legal name & address (no conflicting NAP). |

---

## 4. Risks / Notes
- `LocalBusiness` and `#organization` are intentionally **separate `@id`s** but cross-linked via `parentOrganization` so both entities are described without duplication conflicts.
- Schema is data-driven from `data/schema/*.toml` + `config/branding/schema.toml`; no page-level hard-coding beyond `schema.faq`.
- No `schema.org` validation errors observed in the rendered HTML (verified in `PHASE_2_5_BRAND_SEO_GEO_REPORT.md` §Validation).
