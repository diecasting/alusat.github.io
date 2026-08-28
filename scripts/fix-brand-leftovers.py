#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix leftover uppercase ALUSAT brand tokens in headings/titles/comments.
Leaves alusat.com domain and lowercase linkedin/alusat URLs untouched."""
import os
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (path, old, new, case_sensitive)
fixes = [
    ("content/about-aluminium-extrusion-manufacturer/index.md", "ALUSAT", "YUANZHONG", True),
    ("content/aluminum-extrusion-design-services/index.md", "ALUSAT", "YUANZHONG", True),
    ("content/aluminum-extrusion-manufacturing-process/index.md", "ALUSAT", "YUANZHONG", True),
    ("content/complex-aluminum-extrusion-profiles-manufacturer/index.md", "ALUSAT", "YUANZHONG", True),
    ("layouts/partials/related-resources.html", "Alusat", "YuanZhong", True),
    ("layouts/partials/sections/resources.html", "Alusat", "YuanZhong", True),
    ("config/_default/hugo.toml", "Alusat", "YuanZhong", True),
]

for rel, old, new, cs in fixes:
    p = os.path.join(REPO, rel)
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    if old in txt:
        txt = txt.replace(old, new)
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        print("fixed:", rel)
    else:
        print("no match (skip):", rel)
