# The Wealth Table: extraction log of the current site

Source: https://thewealthtableglobal.com (WordPress + Elementor + Hello theme). Captured 28 Oct 2026.
Raw homepage text is in `docs/extracted/home-page-raw-text.txt`. All content below is the client's own and is reused verbatim in the concepts (Playbook §7: nothing invented).

## 1. Pages found (sitemap)
| URL | What it is | Use in concepts |
|---|---|---|
| `/` | The one-page site (all content below) | Source of everything |
| `/contact/` | Contact form (first/last name, email, optional phone, topic: Inquiry / Suggest, message) + email, phone, office | Contact section |
| `/wealth-summit/` | Empty shell: only the header + waitlist + footer | Ignored |
| `/hello-world/` | Default WordPress post, with a sample comment | Ignored, should be deleted from the live site |
| `/mang/` | Web-developer maintenance note (hosting/domain expiry 9 Jul 2027, support plan "expires 30 Sep 2026") | Internal; **not used**. Note for the client: it is publicly reachable and should be unpublished |

## 2. Identity
- **Name:** The Wealth Table™ (also "The Wealth Table Global" in titles/footer)
- **Tagline:** *Leave richer than you arrived.* ("Come to the table. Leave richer than you arrived.")
- **Founder / host:** Udo Okonjo (Founder, Radiant Collective Capital, "RCC", https://rcc.africa/)
- **Page title:** "The Wealth Table Global – Leave richer than you arrived."
- **Contact:** info@thewealthtableglobal.com · +234 8096000049 · 10, Onisiwo Road, Ikoyi, Lagos
- **Social:** LinkedIn https://ng.linkedin.com/in/udomaryanneokonjo · Instagram https://www.instagram.com/udo_okonjo
- **Footer credit link:** https://zengarybooks.com/ (wraps the footer logo, probably the web builder or an affiliated project; confirm with client)
- **Copyright:** © 2026 The Wealth Table Global. All rights reserved.

## 3. Navigation (current)
`[logo WT]  Register your Interest · About · Contact` + a floating **Join Waitlist** button. Sticky-header plugin. Logo links home.

## 4. Homepage content, section by section (in order)
1. **Hero:** "The Wealth Table", "Leave Richer Than You Arrived.", button **REGISTER YOUR INTEREST** (→ waitlist). A second link "About The Wealth Table" (→ Nairobi anchor).
2. **"What the list gives you":** (a) Invitations are released in waves, to the list before anyone else. (b) The founding rate, held for you. (c) Members of The Wealth Table are invited first.
3. **Three city cards** (image + name + CTA):
   - LAGOS, "Register Your Interest" (`lagos-card.jpg`, aerial of Lagos waterfront)
   - ACCRA, "Relive The Gathering" (`accra-card.jpg`, Kwame Nkrumah Memorial Park)
   - NAIROBI, "Relive The Gathering" (`nairobi-card.jpg`, KICC tower at dusk)
4. **Lagos conference block:** label "The Wealth Table Conference" / headline *Leave richer than you arrived.* / **THE WEALTH TABLE™ LAGOS** / **Sat, Nov 21st, 2026** / **11:00 AM – 5:00 PM (WAT)** / **Civic Centre, VI Lagos** / EVENT DETAILS: "From Conversation to Action. Building on the powerful conversations in Nairobi and Accra, The Wealth Table arrives in Lagos for a bold new chapter. This invitation-only gathering will bring together an exceptional circle of women leaders, entrepreneurs, investors, and wealth builders to explore one defining question: How do we move more women from success to ownership?" / button **REQUEST AN INVITATION**. Image: the Lagos invitation poster (`lagos-event-poster.jpg`: "You are cordially invited… A private gathering of women building, investing and owning for a more prosperous Africa. Saturday 21 November 2026, 12:00–5:00 PM [poster says 12:00, site says 11:00: **discrepancy to confirm**], Civic Centre Lagos, By invitation and approved registration. Connection · Opportunity · Collaboration. Hosted by Udo Okonjo, Founder, Radiant Collective Capital").
5. **Nairobi recap:** venue "KWETU NAIROBI, KENYA 🇰🇪", "Nairobi – Where It All Began.", DATE 13 June 2026. "The inaugural edition… brought together 24 remarkable women in Nairobi for an intimate, invitation-only gathering centred on wealth, ownership, opportunity and intentional connection. In a room defined by openness, generosity and bold conversations, women shared experiences, challenged assumptions and explored what it truly means to build and own wealth on their own terms. The word of the day was Courage, a fitting beginning to a growing global conversation about women, wealth and ownership." / "Leave richer than you arrived." / button **Join Next Nairobi Wait List** / 15-photo gallery.
6. **Accra recap:** venue "CANTONMENTS, ACCRA, GHANA 🇬🇭", "Accra – Where It Continued.", DATE 3 October 2026. "Where the Conversation Continued. Following its inaugural gathering in Nairobi, The Wealth Table arrived in Accra, bringing together approximately 25 remarkable women for an intimate, invitation-only evening of meaningful conversations and connections. Hosted in a beautiful private residence, the gathering created space for honest reflections on wealth, ownership, opportunity, and the power of women coming together with intention. The evening was marked by openness, shared wisdom, fresh perspectives, and a collective desire to move beyond conversations towards meaningful action. Different women. Shared ambition. Bigger possibilities." / button **Join Next Accra Waitlist** / 15-photo gallery.
7. **About the founder:** "Udo Okonjo". "Udo Okonjo believes the next chapter of women's success must be about more than achievement. It must be about ownership. An entrepreneur, investor, board director, and founder of Radiant Collective Capital, Udo has spent decades championing women's leadership, economic advancement, and the power of building wealth with intention. She created The Wealth Table from a simple conviction: when accomplished women come together for honest conversations about money, power, opportunity and ownership, extraordinary possibilities emerge. More than another networking event, The Wealth Table is a space for meaningful connections, shared intelligence, bold thinking, and the conversations that inspire women to make bigger moves. Her invitation is simple: Come to the table. Leave richer than you arrived." Buttons: **request an Invitation**, **Explore The Radiant Capital** (→ rcc.africa). Image: `founder-udo-okonjo.jpg` (a group-at-table photograph, **not** an individual portrait; a real portrait of Udo is needed).
8. **FAQ (9 items):** What is it · Who is it for · Do I need to be an RCC member (No; RCC members get preferential rates) · What to expect · Participation fee (**Lagos: $200 RCC members, $300 non-members**, same experience) · How to register for Lagos ("Register for Lagos" → form → choose rate → pay; confirmed on payment, subject to availability) · When & where Lagos (Sat 21 Nov 2026, Civic Centre, Victoria Island, 11:00–5:00 WAT) · Other cities (yes, "across Africa and beyond") · How to pay (USD, option of Naira at local rate). Full wording is in `docs/extracted/home-page-raw-text.txt`; the concepts' `data.js` holds the same text.
9. **"Still have questions? / More Inquiry?"** → Contact page.
10. **Waitlist form** (Fluent Forms): Email, First Name, "Select Preferred Table" (Lagos / Accra / Nairobi / General – Wealth Table), **Join Your Waitlist**. Consent text: "By subscribing, you agree to our Privacy Policy and provide consent to receive important updates from thewealthtableglobal.com. You can unsubscribe anytime." (No Privacy Policy page exists in the sitemap: **gap**).
11. **Closing CTA:** "THE WEALTH TABLE: Join us, we are about to do it again. Together, we are redefining what financial empowerment looks like, creating a future where women lead with confidence, own assets with purpose, and build legacies that inspire generations to come." → **Join Our Future Waitlist Now**.
12. **Footer:** logo, "This is where women bring more than their stories to the table. They bring the businesses they're building, the investments they're exploring, the opportunities they're pursuing, and the connections they need to make their next move." Address / phone / email, links Home · Contact us · About Us, OUR SOCIAL MEDIA (LinkedIn, Instagram), copyright.

## 5. Visual system currently in use
- **Logo:** white/cream WT monogram (high-contrast Didone-style serif, W and T interlocked) used in the nav (`adaxx.png`); full lock-up (WT + "THE WEALTH TABLE™" + rule + italic "Leave richer than you arrived.") used in the footer (`SAXSD.png`). Cream is `#F0EAE0`.
- **Fonts loaded by Elementor:** Instrument Serif, Bricolage Grotesque, Inter, Inter Tight, Poppins, Roboto (Google Fonts). The logo itself is a Didone (Bodoni/Playfair-like).
- **Colours found:** `#1A2C37` (deep navy-teal, most used), `#CCA20C` (gold), `#B4190F` (red), `#33434C`, `#8C959A`, `#D1D5D7`. The Lagos invitation poster uses cream `#F3E7DB`, burgundy `#500A14` / `#3A060A`. **The poster is the strongest brand signal: cream + deep burgundy + gold line-work.** The concepts lean on it.
- **Imagery:** documentary event photography (warm, candid, bright), plus three city postcards.
- **Tech:** Elementor Pro 4.3, Fluent Forms, Jeg Elementor Kit, Sticky Header Effects, Swiper, e-gallery lightbox.

## 6. Assets saved (`concepts/img/`)
**Logos** (`logo/`, transparent PNG, each in `-cream` and `-ink` colour):
| File | What |
|---|---|
| `wt-monogram-*.png` | **Logo 1:** the "WT" mark only (cut from the footer lock-up, 777×338) |
| `wordmark-*.png` | **Logo 2:** "THE WEALTH TABLE™" wordmark (1588×230) |
| `tagline-*.png` | **Logo 3:** "Leave richer than you arrived." italic line (1067×74) |
| `lockup-full-*.png` | Original combined lock-up, cropped tight |
| `wt-monogram-nav-*.png` | The nav's original WT file, cropped tight (763×331) |

**Photographs** (`photos/`, 35 files, re-encoded ≤1800px JPEG, 7 MB total):
- `nairobi-*` ×16 (13 June 2026: speakers in front of the "THE WEALTH TABLE" backdrop, long white-floral table, guests laughing, networking) + `nairobi-card` (KICC tower)
- `accra-*` ×15 (3 Oct 2026: private residence, candlelit table, guests in green/blue/orange, chef, buffet) + `accra-card` (memorial park)
- `lagos-card` (aerial Lagos waterfront), `lagos-event-poster` (the invitation), `founder-udo-okonjo` (see note above)
- Original filenames are `Image-108xx.jpg` (Nairobi) and `QJP_123A6xxx.jpg` (Accra); mapping is in the name suffix.

## 7. Issues spotted on the live site (for the rebrand conversation)
1. Poster says 12:00 PM, site says 11:00 AM start, to be confirmed.
2. No Privacy Policy page though the form links consent to one.
3. `/mang/` (maintenance note) and `/hello-world/` are public.
4. "Register You Interest" typo on the Lagos card; "Prefered" typo in the form; "Join us, we are about to do It again" is awkward.
5. Nav says "Register your Interest" but the page's real action is a waitlist; two competing CTAs ("Join Waitlist" and "Register your Interest").
6. Flag emojis and "Image-xxxx.jpg" gallery with no captions or alt text.
7. The "founder" photo is not a portrait of the founder.
8. No payment/registration page for Lagos yet, although the FAQ says "Click Register for Lagos".
9. Several image/alt attributes are empty (accessibility and SEO).
