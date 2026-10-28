# Reference ingredient list (Playbook §2 step 4)

Rendered with Playwright/Chromium at 1440×900 and scrolled through. We borrow ingredients, never layouts, text, images or code (Playbook §1).

## URL notes
| You wrote | What I used | Note |
|---|---|---|
| mejuma-tuscany.com / tuscany.com | https://www.mejuma-tuscany.com | `tuscany.com` redirects to an unrelated LinkedIn profile, so I treated the two as one reference |
| jakobsencopehagen.com | https://jakobsencopenhagen.com | spelling fixed |
| BALLENACABO.com | https://ballenacabo.com | |
| TENGILEMALAmala.com | https://tengilemalamala.com | `tengilemala.com` does not exist; this is the Tengile MalaMala Collection |
| lacaminera.com | https://www.hotellacaminera.com | `lacaminera.com` is a parked "for sale" page; used the Hotel La Caminera Club de Campo site (the likely intent). **Tell me if you meant something else.** Its hero is a YouTube video that failed to load in the headless browser, so I judged the rest of the page |

## Mejuma Tuscany (warm, quiet, editorial)
- **Type:** *Made Mirage* (a delicate high-contrast display serif) for headlines, *Golos Text* for body. Colossal lowercase wordmark that fills the hero edge to edge; a single dot detached over the "j".
- **Colour:** off-white `#F1F1F1`, taupe `#C4BCB0`, ink brown `#38352C`, **one** saturated yellow `#FFC94D`-style accent used only on pill buttons and a banner.
- **Nav:** pill-shaped "Menu" button + round dot button, top right; wordmark top-left; both float in a translucent capsule once you scroll.
- **Structure:** hero wordmark → statement → property cards with data rows → yellow "curious?" strip → big headline on taupe → numbered process rows (.04 Coordinate, .05 Arrive) → founders story → giant wordmark footer.
- **Motion:** headline sections that scale/slide as you scroll (GSAP/ScrollTrigger + Lenis smooth scroll), image panels that reveal behind text.

## Jakobsen Copenhagen (Scandinavian calm)
- **Type:** one family only, *ABC Arizona Flare*, in a light weight at very large sizes for the brand statement.
- **Colour:** warm off-white `#FAF8F4`, near-black `#161614`; colour comes from the photography, with one full-bleed pale-blue section as a surprise.
- **Nav:** the simplest possible: text links left (Products, Retailers, Stories), centred wordmark, links right (About, Contact, EN/DE). White on the hero, ink on paper.
- **Structure:** full-bleed video hero with centred logo → one giant paragraph statement → staggered, asymmetric image columns → full-bleed product scene → index list ("29 All Products / Sofas / Lounge Chairs") that swaps an image → craft story → footer with contact columns.
- **Motion:** slow parallax columns at different speeds, underline-on-hover links, Lenis smooth scrolling.

## Ballena Cabo (the user's favourite navbar)
- **Navbar spec (measured):** `position: fixed`, **600px wide × 50px high**, centred, `background: rgba(3,9,13,.19)`, `backdrop-filter: blur(25px)`, **5px radius**. Contents: left an outlined **BOOK NOW** button, centre the wordmark, right a two-line hamburger. The bar tints to match the section behind (olive, charcoal). Opens a full overlay with large links (Home, Events, Menu, Gallery, Location, About, Instagram, Gift Cards).
- **Type:** *Sweet Sans Pro* wide, all-caps, tracked headlines; *TT Commons Pro* for small text. Giant condensed "BALLENA" wordmark in the footer.
- **Colour:** sand `#F8F2E5`, terracotta, olive green, charcoal. Sections change background colour wholesale as you scroll.
- **Structure:** looping video hero with a short caps headline → statement over landscape → split terracotta/photo "flavors" → three tall cards (Events, Gallery, Gift Cards) → about with B&W portrait → newsletter → giant wordmark.

## Tengile MalaMala Collection (luxury safari)
- **Type:** a thin wide-set display serif in ALL CAPS for the hero ("UNMATCHED / ABUNDANCE", the second line indented right), *Inter* for UI, large soft serif paragraphs in olive for statements.
- **Colour:** blush-cream `#F5EEE9`, deep olive `#373F1D` for text and the footer, white buttons.
- **Structure:** video hero, ENQUIRE left / MENU right with a centred logo → long editorial paragraph → lodge/camp cards with captions → full-bleed gallery with "1 / 6" counter → conservation block with small images **scattered around centred text** → people (staff portraits) carousel → full-bleed "Plan a trip" with text over an aerial → olive footer.
- **Motion:** scattered image cloud with parallax, horizontal people strip, "Play Video" control.

## Hotel La Caminera (classic Spanish luxury)
- **Type:** *PT Serif Pro* for headings and body, *Forma DJR* for tiny labels. Centred layouts, a lot of air, small underlined "CONOCER MÁS →" links.
- **Colour:** black hero, ivory sections, gold/olive pop-up, restrained.
- **Structure:** dark video hero with a **booking bar** (when / who / promo code + "Buscar") docked to the bottom → short centred statement → three portrait cards (rooms, spa, …) → full-bleed airfield feature → "Territorio de inspiración" mosaic (windmill, cheese, waterfall) → newsletter → black footer with Michelin/TripAdvisor badges.
- **UI worth keeping:** the docked booking bar, hairline-bordered outline "RESERVAR" button, laid-back italic serif tone.

## What we take, mapped to concepts (see playbook §3 format)
| Reference | Ingredient | Used in |
|---|---|---|
| Ballena | The **600×50 floating glass nav** (BOOK NOW · wordmark · hamburger), overlay menu, giant footer wordmark, section background colour changes | **Concept 3 "Ballena-bar" (nav only)**, footer wordmark in 1 and 3 |
| Mejuma | Edge-to-edge hero wordmark, pill buttons with one accent, numbered process rows, taupe/off-white pacing | Concept 1 |
| Jakobsen | Single-family light type at giant size, centred logo nav, asymmetric parallax image columns, index list with image swap | Concept 2 |
| Tengile | Caps serif hero with indented second line, scattered image cloud, olive footer, "ENQUIRE / MENU" nav, large soft statements | Concept 4 |
| La Caminera | Docked booking bar (reused as the waitlist bar), hairline outline CTAs, centred classic serif calm | Concepts 3 and 4 |
