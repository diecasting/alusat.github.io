#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate self-contained localized STUB pages for the 4 key subpages
(about / quality / capabilities / contact) in de, ja, fr, es.

Each stub:
  - localized front-matter (title, description, seo)
  - localized H1 + intro + bullet summary
  - a link to the full English page (so the page is a clean fallback, not a
    duplicate-content copy)
  - contact pages also carry the address + RFQ form

Because each file is placed as index.<lang>.md in the SAME content bundle as
the English index.md, Hugo automatically groups them as translations, producing
reciprocal hreflang with no broken alternates and no 404s.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# page key -> (content dir, is_contact)
PAGES = {
    "about":       ("about-aluminium-extrusion-manufacturer", False),
    "quality":     ("aluminum-extrusion-quality-certification", False),
    "capabilities":("aluminum-extrusion-capabilities", False),
    "contact":     ("contact", True),
}

COMPANY = "YuanZhong Technology Co., Limited"
ADDRESS = "No.238 Guanbi Street, Daling Mountain Town, Dongguan City, China"
EMAIL = "hank@alusat.com"

# localized content per language
L = {
  "de": {
    "contact_heading": "Direkte Kontaktaufnahme",
    "cta_label": "Angebot für kundenspezifische Strangpressung anfordern",
    "services_link": "/aluminum-extrusion-services/",
    "pages": {
      "about": {
        "title": "Über YuanZhong Technology Co., Limited — Aluminium-Strangpressen-Hersteller",
        "description": "YuanZhong Technology Co., Limited ist ein Aluminium-Strangpressen-Hersteller in Dongguan, China, der globale OEM-Kunden mit kundenspezifischen Profilen, CNC-Bearbeitung und Oberflächenveredelung beliefert.",
        "h1": "Über YuanZhong Technology Co., Limited",
        "intro": "YuanZhong Technology Co., Limited ist ein in Dongguan, Guangdong, China ansässiger Aluminium-Strangpressen-Hersteller, der kundenspezifische Aluminiumprofile und präzise Komponenten für OEM-Kunden in Nordamerika, Europa, Asien und weltweit entwickelt und fertigt.",
        "bullets": [
          "Einzelquelle für Werkzeugbau, Strangpressen, Wärmebehandlung, CNC-Bearbeitung, Veredelung und Prüfung",
          "Kundenspezifische Profile nach Zeichnung, Toleranz und Oberfläche",
          "Fertigung und Montage betriebsfertiger Baugruppen",
        ],
        "fullnote": "Die vollständige Seite ist auf Englisch verfügbar: [About (English)](/about-aluminium-extrusion-manufacturer/).",
      },
      "quality": {
        "title": "Aluminium-Strangpressen — Qualitätsmanagement & Prüfung",
        "description": "YuanZhong Technology Co., Limited wendet professionelle Qualitätsmanagement- und Prüfverfahren für Aluminium-Strangpressungen mit Werkstoffprüfung, Maßkontrolle und Rückverfolgbarkeit an.",
        "h1": "Qualitätsmanagement & Prüfung",
        "intro": "Zuverlässige Aluminium-Strangpressung erfordert mehr als Produktionskapazität. Zertifizierung, Prüfsysteme und Prozesskontrolle sichern eine gleichbleibende Leistung für globale OEM-Kunden.",
        "bullets": [
          "Werkstoffverifikation und Legierungsprüfung",
          "Maßkontrolle mit CMM und geometrischen Messungen",
          "Oberflächenqualität und Rückverfolgbarkeit der Produktion",
        ],
        "fullnote": "Die vollständige Seite ist auf Englisch verfügbar: [Quality (English)](/aluminum-extrusion-quality-certification/).",
      },
      "capabilities": {
        "title": "Aluminium-Strangpressen — Fertigungskapazitäten",
        "description": "YuanZhong Technology Co., Limited bietet vollständige Aluminium-Strangpresskapazitäten: Profilstrangpressen, CNC-Bearbeitung, Fertigung, Oberflächenveredelung und Präzisionsprüfung.",
        "h1": "Fertigungskapazitäten",
        "intro": "YuanZhong Technology Co., Limited verfügt über ein integriertes Fertigungssystem, das globale OEM-Kunden mit zuverlässigen Aluminium-Profillösungen unterstützt.",
        "bullets": [
          "Profilstrangpressen in einem breiten Tonnenbereich",
          "Wärmebehandlung (T4, T5, T6) und Präzisionssägen",
          "CNC-Bearbeitung, Biegen, Schweißen und Montage",
        ],
        "fullnote": "Die vollständige Seite ist auf Englisch verfügbar: [Manufacturing Capabilities (English)](/aluminum-extrusion-capabilities/).",
      },
      "contact": {
        "title": "Kontakt — YuanZhong Technology Co., Limited",
        "description": "Kontaktieren Sie YuanZhong Technology Co., Limited für Angebote zu Aluminium-Strangpressung, CNC-Bearbeitung und OEM-Fertigung sowie technische Unterstützung. E-Mail, Telefon und Adresse.",
        "h1": "Kontaktieren Sie uns",
        "intro": "Kontaktieren Sie das Team von YuanZhong Technology Co., Limited für Angebote, technische Unterstützung und Fertigungsfragen. Das schnellste ist das Angebotsformular unten.",
        "fullnote": "Die vollständige Kontaktseite ist auf Englisch verfügbar: [Contact (English)](/contact/).",
      },
    },
  },
  "fr": {
    "contact_heading": "Contact direct",
    "cta_label": "Demander un devis d'extrusion sur mesure",
    "services_link": "/aluminum-extrusion-services/",
    "pages": {
      "about": {
        "title": "À propos de YuanZhong Technology Co., Limited — Extrusion d'aluminium",
        "description": "YuanZhong Technology Co., Limited est un fabricant d'extrusion d'aluminium à Dongguan, en Chine, fournissant des profilés sur mesure, l'usinage CNC et les finitions de surface aux clients OEM du monde entier.",
        "h1": "À propos de YuanZhong Technology Co., Limited",
        "intro": "YuanZhong Technology Co., Limited est un fabricant d'extrusion d'aluminium basé à Dongguan, Guangdong, en Chine, qui conçoit et fabrique des profilés en aluminium sur mesure et des composants de précision pour les clients OEM en Amérique du Nord, en Europe, en Asie et dans le monde entier.",
        "bullets": [
          "Source unique pour l'outillage, l'extrusion, le traitement thermique, l'usinage CNC, les finitions et le contrôle",
          "Profilés sur mesure selon le plan, la tolérance et la finition",
          "Fabrication et assemblage de sous-ensembles prêts à l'emploi",
        ],
        "fullnote": "La page complète est disponible en anglais : [About (English)](/about-aluminium-extrusion-manufacturer/).",
      },
      "quality": {
        "title": "Extrusion d'aluminium — Qualité et contrôle",
        "description": "YuanZhong Technology Co., Limited applique des systèmes professionnels de gestion de la qualité et de contrôle pour l'extrusion d'aluminium, avec vérification des matériaux, contrôle dimensionnel et traçabilité.",
        "h1": "Qualité et contrôle",
        "intro": "Une extrusion d'aluminium fiable exige plus que la capacité de production. La certification, les systèmes de contrôle et la maîtrise des processus garantissent la performance pour les clients OEM.",
        "bullets": [
          "Vérification des matériaux et essais des alliages",
          "Contrôle dimensionnel par MMT et mesures géométriques",
          "Qualité de surface et traçabilité de production",
        ],
        "fullnote": "La page complète est disponible en anglais : [Quality (English)](/aluminum-extrusion-quality-certification/).",
      },
      "capabilities": {
        "title": "Extrusion d'aluminium — Capacités de fabrication",
        "description": "YuanZhong Technology Co., Limited propose des capacités complètes d'extrusion d'aluminium : profilés, usinage CNC, fabrication, finitions et contrôle de précision.",
        "h1": "Capacités de fabrication",
        "intro": "YuanZhong Technology Co., Limited dispose d'un système de fabrication intégré qui soutient les clients OEM avec des solutions de profilés aluminium fiables.",
        "bullets": [
          "Extrusion de profilés sur une large gamme de tonnages",
          "Traitement thermique (T4, T5, T6) et découpe de précision",
          "Usinage CNC, pliage, soudure et assemblage",
        ],
        "fullnote": "La page complète est disponible en anglais : [Manufacturing Capabilities (English)](/aluminum-extrusion-capabilities/).",
      },
      "contact": {
        "title": "Contact — YuanZhong Technology Co., Limited",
        "description": "Contactez YuanZhong Technology Co., Limited pour des devis d'extrusion d'aluminium, l'usinage CNC et la fabrication OEM, ainsi que le support technique. E-mail, téléphone et adresse.",
        "h1": "Contactez-nous",
        "intro": "Contactez l'équipe de YuanZhong Technology Co., Limited pour les devis, le support technique et vos questions de fabrication. Le plus rapide est le formulaire de devis ci-dessous.",
        "fullnote": "La page complète est disponible en anglais : [Contact (English)](/contact/).",
      },
    },
  },
  "es": {
    "contact_heading": "Contacto directo",
    "cta_label": "Solicitar presupuesto de extrusión a medida",
    "services_link": "/aluminum-extrusion-services/",
    "pages": {
      "about": {
        "title": "Acerca de YuanZhong Technology Co., Limited — Extrusión de aluminio",
        "description": "YuanZhong Technology Co., Limited es un fabricante de extrusión de aluminio en Dongguan, China, que suministra perfiles a medida, mecanizado CNC y acabados de superficie a clientes OEM de todo el mundo.",
        "h1": "Acerca de YuanZhong Technology Co., Limited",
        "intro": "YuanZhong Technology Co., Limited es un fabricante de extrusión de aluminio con sede en Dongguan, Guangdong, China, que diseña y fabrica perfiles de aluminio a medida y componentes de precisión para clientes OEM en Norteamérica, Europa, Asia y el resto del mundo.",
        "bullets": [
          "Fuente única para utillaje, extrusión, tratamiento térmico, mecanizado CNC, acabados y control",
          "Perfiles a medida según plano, tolerancia y acabado",
          "Fabricación y montaje de subconjuntos listos para usar",
        ],
        "fullnote": "La página completa está disponible en inglés: [About (English)](/about-aluminium-extrusion-manufacturer/).",
      },
      "quality": {
        "title": "Extrusión de aluminio — Calidad y control",
        "description": "YuanZhong Technology Co., Limited aplica sistemas profesionales de gestión de calidad y control para la extrusión de aluminio, con verificación de materiales, control dimensional y trazabilidad.",
        "h1": "Calidad y control",
        "intro": "Una extrusión de aluminio fiable exige más que capacidad de producción. La certificación, los sistemas de control y el control de procesos garantizan el rendimiento para los clientes OEM.",
        "bullets": [
          "Verificación de materiales y ensayos de aleaciones",
          "Control dimensional por MMC y mediciones geométricas",
          "Calidad de superficie y trazabilidad de producción",
        ],
        "fullnote": "La página completa está disponible en inglés: [Quality (English)](/aluminum-extrusion-quality-certification/).",
      },
      "capabilities": {
        "title": "Extrusión de aluminio — Capacidades de fabricación",
        "description": "YuanZhong Technology Co., Limited ofrece capacidades completas de extrusión de aluminio: perfiles, mecanizado CNC, fabricación, acabados y control de precisión.",
        "h1": "Capacidades de fabricación",
        "intro": "YuanZhong Technology Co., Limited cuenta con un sistema de fabricación integrado que respalda a los clientes OEM con soluciones de perfiles de aluminio fiables.",
        "bullets": [
          "Extrusión de perfiles en un amplio rango de toneladas",
          "Tratamiento térmico (T4, T5, T6) y corte de precisión",
          "Mecanizado CNC, plegado, soldadura y ensamblaje",
        ],
        "fullnote": "La página completa está disponible en inglés: [Manufacturing Capabilities (English)](/aluminum-extrusion-capabilities/).",
      },
      "contact": {
        "title": "Contacto — YuanZhong Technology Co., Limited",
        "description": "Contacte con YuanZhong Technology Co., Limited para presupuestos de extrusión de aluminio, mecanizado CNC y fabricación OEM, así como soporte técnico. Correo, teléfono y dirección.",
        "h1": "Contáctenos",
        "intro": "Contacte con el equipo de YuanZhong Technology Co., Limited para presupuestos, soporte técnico y preguntas de fabricación. Lo más rápido es el formulario de presupuesto a continuación.",
        "fullnote": "La página completa está disponible en inglés: [Contact (English)](/contact/).",
      },
    },
  },
  "ja": {
    "contact_heading": "直接の連絡先",
    "cta_label": "カスタム押出の見積もりを依頼",
    "services_link": "/aluminum-extrusion-services/",
    "pages": {
      "about": {
        "title": "YuanZhong Technology Co., Limitedについて — アルミ押出",
        "description": "YuanZhong Technology Co., Limitedは、中国・東莞のアルミ押出メーカーです。世界中のOEM顧客にカスタムプロファイル、CNC加工、表面処理を提供しています。",
        "h1": "YuanZhong Technology Co., Limitedについて",
        "intro": "YuanZhong Technology Co., Limitedは、中国広東省東莞市に拠点を置くアルミ押出メーカーです。北米、欧州、アジアおよび世界中のOEM顧客向けに、カスタムアルミプロファイルと高精度部品を設計・製造しています。",
        "bullets": [
          "金型、押出、熱処理、CNC加工、表面処理、検査を一貫対応",
          "図面・公差・仕上げに合わせたカスタムプロファイル",
          "組立て完成品の製造",
        ],
        "fullnote": "完全なページは英語でご覧いただけます：[About (English)](/about-aluminium-extrusion-manufacturer/)。",
      },
      "quality": {
        "title": "アルミ押出 — 品質管理と検査",
        "description": "YuanZhong Technology Co., Limitedは、材料確認、寸法検査、トレーサビリティを備えたプロのアルミ押出品質管理・検査システムを導入しています。",
        "h1": "品質管理と検査",
        "intro": "信頼できるアルミ押出には、生産能力以上のものが必要です。認証、検査システム、プロセス管理がOEM顧客への安定した性能を支えます。",
        "bullets": [
          "材料確認と合金試験",
          "三次元測定機（CMM）による寸法検査",
          "表面品質と生産のトレーサビリティ",
        ],
        "fullnote": "完全なページは英語でご覧いただけます：[Quality (English)](/aluminum-extrusion-quality-certification/)。",
      },
      "capabilities": {
        "title": "アルミ押出 — 製造能力",
        "description": "YuanZhong Technology Co., Limitedは、プロファイル押出、CNC加工、製造、表面処理、精密検査を含む総合的なアルミ押出製造能力を提供します。",
        "h1": "製造能力",
        "intro": "YuanZhong Technology Co., Limitedは、信頼できるアルミプロファイルソリューションでOEM顧客を支える統合製造システムを備えています。",
        "bullets": [
          "幅広いトン数でのプロファイル押出",
          "熱処理（T4、T5、T6）と精密切断",
          "CNC加工、曲げ、溶接、組立て",
        ],
        "fullnote": "完全なページは英語でご覧いただけます：[Manufacturing Capabilities (English)](/aluminum-extrusion-capabilities/)。",
      },
      "contact": {
        "title": "お問い合わせ — YuanZhong Technology Co., Limited",
        "description": "アルミ押出、CNC加工、OEM製造の見積もりや技術サポートについてはYuanZhong Technology Co., Limitedまで。メール、電話、住所。",
        "h1": "お問い合わせ",
        "intro": "見積もり、技術サポート、製造に関するご質問はYuanZhong Technology Co., Limitedまで。最も早いのは下の見積もりフォームです。",
        "fullnote": "完全なページは英語でご覧いただけます：[Contact (English)](/contact/)。",
      },
    },
  },
}

def build_body(lang, page_key, p):
    lines = []
    lines.append(f"## {p['h1']}")
    lines.append("")
    lines.append(p["intro"])
    lines.append("")
    if page_key != "contact":
        for b in p["bullets"]:
            lines.append(f"- {b}")
        lines.append("")
        lines.append(f"[{L[lang]['cta_label']} →]({L[lang]['services_link']})")
        lines.append("")
    else:
        ch = L[lang]["contact_heading"]
        lines.append(f"## {ch}")
        lines.append("")
        lines.append(f"**{COMPANY}**  ")
        lines.append(f"{ADDRESS}  ")
        lines.append(f"E-Mail: {EMAIL}")
        lines.append("")
        lines.append("{{< rfq_form >}}")
        lines.append("")
    lines.append(p["fullnote"])
    lines.append("")
    return "\n".join(lines)

def build_frontmatter(lang, page_key, p, is_contact):
    fm = []
    fm.append("---")
    fm.append(f'title: "{p["title"]}"')
    fm.append(f'description: "{p["description"]}"')
    fm.append('layout: "single"')
    fm.append("draft: false")
    if is_contact:
        fm.append("date: 2026-01-01")
        fm.append('tags: ["contact", "request a quote", "engineering support"]')
        fm.append('categories: ["Contact"]')
        fm.append("seo:")
        fm.append(f'  meta_title: "{p["title"]} | {COMPANY}"')
        fm.append(f'  meta_description: "{p["description"]}"')
        fm.append('  keywords: ["contact manufacturer", "request a quote", "engineering support", "aluminum extrusion supplier", "CNC machining China"]')
    fm.append("---")
    return "\n".join(fm)

def main():
    created = []
    for lang in ("de", "ja", "fr", "es"):
        for page_key, (dir_name, is_contact) in PAGES.items():
            p = L[lang]["pages"][page_key]
            fm = build_frontmatter(lang, page_key, p, is_contact)
            body = build_body(lang, page_key, p)
            content = fm + "\n\n" + body
            out_path = os.path.join(REPO, "content", dir_name, f"index.{lang}.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            created.append(out_path)
    for c in created:
        print("created:", c)

if __name__ == "__main__":
    main()
