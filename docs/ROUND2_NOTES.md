# Round 2: what changed and why

Feedback on round 1: the four concepts looked the same (same cream/burgundy/dark palette, same section order), the references were not visible, images were low quality, and "Register your interest" was buried. Round 2 starts again.

## Reference to concept mapping (Playbook §2–3)
| Concept | Main reference(s) | Visible borrowed ingredients |
|---|---|---|
| 1 `c1-warm.html` | Mejuma Tuscany | Lowercase serif wordmark across the whole hero, floating "Menu + dot" capsule, property-style cards with data rows, yellow band, sticky stacking step cards, "let's meet" split, giant footer wordmark, one yellow accent on greige |
| 2 `c2-quiet.html` | Jakobsen Copenhagen | One light serif at every size, centred-logo text nav, one giant paragraph, drifting image columns, "All products" index list that swaps a preview image, full-bleed scenes with tiny corner captions, a single pale-blue colour block, quiet contact-column footer |
| 3 `c3-sand.html` | Ballena Cabo, Tengile MalaMala | Ballena's 600×50 glass bar that re-tints per section, whole-section colour changes, wide capital headlines, three tall cards, B&W portrait, underline-only form, giant condensed footer wordmark; Tengile's indented second headline line, scattered image cloud, olive/blush pairing |
| 4 `c4-resort.html` | Velaa Private Island, Lingers | Velaa's thin serif with italic emphasis words, translucent register block in a quiet top bar, collage with the statement between images, tagged tiles, one deep-navy band, full-bleed quote, numbered sitemap; Lingers' giant pale watermark and sticky date + Register widget |
La Caminera (the fifth original reference) contributed the docked-bar idea that became the hero Register bar in concept 3 and the hairline details; its site was largely a video that did not render in the capture.

## Palettes are now light and come from the references
Mejuma off-white/greige/yellow · Jakobsen paper/ink/pale blue · Ballena sand/terracotta + Tengile olive/blush · Velaa greige/taupe + one navy band. No dark-dominant concept.

## Register your interest
In every concept it is: in the navigation, in the hero, in a sticky control (capsule / floating button / glass bar button / bottom-left widget / bottom bar on phones), after the tables section, and in the closing section. Any of those opens the same registration form (modal), preselecting the table when relevant.

## Image audit (see also SITE_EXTRACTION.md §6)
Scored 35 originals on resolution and sharpness and viewed each one. **Removed:** the three city card pictures from the live site (Lagos 1120px and visibly upscaled, Accra 600×900, Nairobi 480×640), plus soft or dim frames (Accra 6582 blurry, 6725 dark, Nairobi 10874/10890 partial/name card). **Kept:** 24 sharp frames at 1500–1600px, re-exported at JPEG quality 92 with no upscaling. **Accra photos carry a "QJ pictures" corner mark**, cropped off (bottom 125px); confirm photographer credit and usage. No Lagos event photograph exists yet; Lagos is shown through the invitation poster at small size.
Moved to `docs/extracted/low-res-not-used/`.

## Technical
Logos are pre-coloured PNGs (`img/logo/*-{cream,white,brown,black,olive,navy,terra}.png`) because CSS masks fail on `file://`; pages open by double-click. Fonts are self-hosted in `fonts/`.
