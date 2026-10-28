"""Brand guidelines (HTML + PDF) and colour swatches. Run after the other builders:
PYTHONPATH=/tmp/pylibs python3 scripts/brand/build_guidelines.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

PH = f'../assets/img/photos/'
W, H = 1600, 1000


def cmyk(hexv):
    r, g, b = [int(hexv[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    k = 1 - max(r, g, b)
    if k >= 1: return (0, 0, 0, 100)
    return tuple(round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))


def rgb(hexv): return tuple(int(hexv[i:i + 2], 16) for i in (1, 3, 5))


PAL = [('Sand', C['sand'], 'Primary background', 'Pages, posters, social, paper'), ('Olive', C['olive'], 'Primary brand colour', 'Panels, headlines, footers, avatars'),
       ('Terracotta', C['terra'], 'Primary brand colour', 'Accents, event panels, italics'), ('Deep Olive', C['olive_d'], 'Text and depth', 'Headlines on light, large numerals'),
       ('Blush', C['blush'], 'Soft background', 'Alternate sections'), ('Stone', C['stone'], 'Neutral background', 'Footers, founder, quiet sections'),
       ('Ink', C['ink'], 'Body text', 'Paragraphs and small print'), ('Gold', C['gold'], 'Hairline accent only', 'Rules, frames, diamonds. Never fills')]

css = f'''
body{{background:#ddd}}
.slide{{width:{W}px;height:{H}px;position:relative;overflow:hidden;page-break-after:always;background:{C['sand']};color:{C['ink']};padding:80px 100px}}
.slide.olive{{background:{C['olive']};color:{C['sand']}}}.slide.terra{{background:{C['terra']};color:{C['sand']}}}
.k{{font-family:'Lexend Zetta';font-weight:300;font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:{C['terra']}}}
.olive .k,.terra .k{{color:{C['gold']}}}
h1{{font-family:'Bodoni Moda';font-weight:400;font-size:88px;line-height:1.02;letter-spacing:-.012em}}h1 em{{font-style:italic;color:{C['terra']}}}.olive h1 em,.terra h1 em,.olive h2 em,.terra h2 em{{color:{C['sand']}}}
h2{{font-family:'Bodoni Moda';font-weight:400;font-size:54px;line-height:1.05;letter-spacing:-.01em;margin:14px 0 26px}}h2 em{{font-style:italic;color:{C['terra']}}}
p{{font-size:20px;line-height:1.55;max-width:760px}}
.num{{position:absolute;right:100px;bottom:56px;font-family:'Lexend Zetta';font-weight:300;font-size:12px;letter-spacing:.3em;opacity:.6}}
.hair{{height:1px;background:{C['gold']};margin:22px 0}}
.grid{{display:grid;gap:26px}}
.cell{{background:{C['blush']};display:grid;place-items:center;position:relative;padding:20px}}
.cell small{{position:absolute;left:14px;bottom:10px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;opacity:.7}}
.sw{{height:200px;position:relative;display:flex;flex-direction:column;justify-content:flex-end;padding:16px}}
.sw b{{font-family:'Lexend Zetta';font-weight:300;font-size:14px;letter-spacing:.14em;text-transform:uppercase}}
.sw span{{font-size:13px;opacity:.85;line-height:1.5}}
img{{display:block}}
.li{{display:flex;gap:16px;align-items:baseline;padding:11px 0;border-top:1px solid {C['gold']};font-size:19px}}
.li b{{font-family:'Lexend Zetta';font-weight:300;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:{C['terra']};width:170px;flex:none}}
.no{{position:relative}}.no::after{{content:"×";position:absolute;right:10px;top:4px;font-size:30px;color:{C['terra']}}}
'''

LG = 'logos/png/'


def im(src, style=''): return f'<img src="{src}" style="{style}">'


slides = []
# 1 cover
slides.append(f'''<div class="slide olive"><div style="position:absolute;inset:0;background:url(art/ripple-olive.png) center/cover;opacity:.9"></div>
  <div style="position:relative;height:100%;display:grid;place-items:center;text-align:center"><div>{im(LG + 'primary-stacked-sand.png', 'width:560px;margin:0 auto')}<div class="k" style="margin-top:56px;color:{C['sand']}">Brand guidelines · Version 1.0 · October 2026</div></div></div></div>''')
# 2 story
slides.append(f'''<div class="slide"><div class="k">01 · Brand story</div><h1 style="margin-top:20px">Leave richer<br>than you <em>arrived.</em></h1><div class="hair" style="width:120px"></div>
  <div style="display:grid;grid-template-columns:1.1fr .9fr;gap:80px"><div><p>The Wealth Table is a purposefully designed gathering where women connect around real opportunities, shared ambitions, and the future of wealth and ownership. It is where women bring more than their stories to the table: the businesses they are building, the investments they are exploring, the opportunities they are pursuing, and the connections they need to make their next move.</p>
  <p style="margin-top:20px">Founded by Udo Okonjo, Founder of Radiant Collective Capital. Held in Nairobi, Accra and Lagos, and expanding across Africa and beyond.</p></div>
  <div><div class="li"><b>Connection</b>Meaningful relationships over networking.</div><div class="li"><b>Opportunity</b>Real introductions, investments, partnerships.</div><div class="li"><b>Collaboration</b>Participation and contribution, not pitches.</div><div class="li"><b>Ownership</b>From success to ownership.</div></div></div><div class="num">02</div></div>''')
# 3 logo suite
cells = [('Primary stacked', 'primary-stacked-olive.png', 'width:360px'), ('Horizontal', 'horizontal-olive.png', 'width:420px'), ('Wordmark', 'wordmark-olive.png', 'width:380px'),
         ('Monogram', 'monogram-olive.png', 'width:200px'), ('Seal', 'seal-olive.png', 'height:250px'), ('Table mark', 'table-mark-terracotta.png', 'height:250px')]
slides.append(f'''<div class="slide"><div class="k">02 · Logo suite</div><h2>One family, <em>six marks.</em></h2>
  <div class="grid" style="grid-template-columns:repeat(3,1fr);grid-auto-rows:310px">{''.join(f'<div class="cell">{im(LG + f, st)}<small>{n}</small></div>' for n, f, st in cells)}</div>
  <p style="margin-top:22px;font-size:17px;max-width:1300px">The primary stacked logo is the default. Use the horizontal logo where height is limited, the monogram and seal for avatars and stamps, and the table mark as a graphic device. All are supplied as SVG (vector) and PNG in sand, olive, terracotta, ink and white.</p><div class="num">03</div></div>''')
# 4 clear space & min size
slides.append(f'''<div class="slide"><div class="k">03 · Clear space and size</div><h2>Give it <em>room.</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:70px;margin-top:10px">
   <div class="cell" style="height:560px"><div style="position:relative;padding:70px;border:1.5px dashed {C['terra']}">{im(LG + 'primary-stacked-olive.png', 'width:400px')}<div style="position:absolute;left:0;top:0;width:70px;height:70px;border-right:1.5px dashed {C['terra']};border-bottom:1.5px dashed {C['terra']};display:grid;place-items:center;font-family:'Antonio';font-size:28px;color:{C['terra']}">X</div></div><small>X = half the height of the monogram</small></div>
   <div><p>Keep a clear space of <b>X</b> (half the height of the WT monogram) on every side. No text, image edges or other logos inside it.</p><div class="hair"></div>
   <div class="li"><b>Stacked</b>Minimum 120 px wide · 30 mm</div><div class="li"><b>Horizontal</b>Minimum 180 px wide · 45 mm</div><div class="li"><b>Wordmark</b>Minimum 110 px wide · 28 mm</div><div class="li"><b>Monogram</b>Minimum 32 px wide · 8 mm</div><div class="li"><b>Seal</b>Minimum 90 px · 22 mm</div>
   <div style="display:flex;gap:40px;align-items:end;margin-top:40px">{im(LG + 'primary-stacked-olive.png', 'width:120px')}{im(LG + 'horizontal-olive.png', 'width:180px')}{im(LG + 'monogram-olive.png', 'width:32px')}{im(LG + 'seal-olive.png', 'width:90px')}</div></div></div><div class="num">04</div></div>''')
# 5 colour use + don'ts
mini = lambda bg, f: f'<div style="background:{bg};height:200px;display:grid;place-items:center">{im(LG + f, "width:230px")}</div>'
slides.append(f'''<div class="slide"><div class="k">04 · Logo colour and misuse</div><h2>Always <em>legible.</em></h2>
  <div class="grid" style="grid-template-columns:repeat(4,1fr)">{mini(C['sand'], 'primary-stacked-olive.png')}{mini(C['olive'], 'primary-stacked-sand.png')}{mini(C['terra'], 'primary-stacked-sand.png')}<div style="height:200px;background:url({PH}a-6797-sm.jpg) center/cover;display:grid;place-items:center">{im(LG + 'primary-stacked-white.png', 'width:230px')}</div></div>
  <div class="hair" style="margin:34px 0 20px"></div><div class="k" style="margin-bottom:16px">Do not</div>
  <div class="grid" style="grid-template-columns:repeat(5,1fr)">
   <div class="cell no" style="height:200px">{im(LG + 'primary-stacked-olive.png', 'width:230px;transform:scaleX(1.5)')}<small>Stretch</small></div>
   <div class="cell no" style="height:200px">{im(LG + 'primary-stacked-terracotta.png', 'width:230px;filter:hue-rotate(120deg)')}<small>Recolour</small></div>
   <div class="cell no" style="height:200px">{im(LG + 'primary-stacked-olive.png', 'width:230px;transform:rotate(-14deg)')}<small>Rotate</small></div>
   <div class="cell no" style="height:200px;background:{C['terra']}">{im(LG + 'primary-stacked-olive.png', 'width:230px')}<small style="color:{C['sand']}">Low contrast</small></div>
   <div class="cell no" style="height:200px">{im(LG + 'primary-stacked-olive.png', 'width:230px;filter:drop-shadow(6px 8px 6px rgba(0,0,0,.45))')}<small>Effects</small></div></div><div class="num">05</div></div>''')
# 6 colour
slides.append(f'''<div class="slide"><div class="k">05 · Colour</div><h2>Warm, grounded, <em>quietly rich.</em></h2>
  <div class="grid" style="grid-template-columns:repeat(4,1fr);gap:18px">{''.join(f'<div class="sw" style="background:{h};color:{C["sand"] if n in ("Olive","Terracotta","Deep Olive","Ink") else C["ink"]};{"border:1px solid rgba(38,42,26,.18)" if n in ("Sand","Blush") else ""}"><b>{n}</b><span>{h}<br>RGB {" ".join(str(v) for v in rgb(h))}<br>CMYK ≈ {" ".join(str(v) for v in cmyk(h))}<br><i>{u}</i></span></div>' for n, h, u, _ in PAL)}</div>
  <div style="display:flex;height:34px;margin-top:34px"><div style="flex:40;background:{C['sand']};border:1px solid rgba(38,42,26,.2)"></div><div style="flex:25;background:{C['olive']}"></div><div style="flex:15;background:{C['terra']}"></div><div style="flex:10;background:{C['stone']}"></div><div style="flex:6;background:{C['olive_d']}"></div><div style="flex:3;background:{C['ink']}"></div><div style="flex:1;background:{C['gold']}"></div></div>
  <p style="margin-top:14px;font-size:16px">Suggested proportion: sand 40, olive 25, terracotta 15, stone 10, deep olive 6, ink 3, gold 1. CMYK values are approximate conversions; confirm against a printed proof.</p><div class="num">06</div></div>''')
# 7 type
slides.append(f'''<div class="slide"><div class="k">06 · Typography</div><h2>Four typefaces, <em>one voice.</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:26px 70px">
   <div><div class="k" style="color:{C['olive']}">Lexend Zetta · display capitals</div><div style="font-family:'Lexend Zetta';font-weight:200;text-transform:uppercase;font-size:44px;letter-spacing:.02em;margin:12px 0">Come to the table</div><p style="font-size:16px">Light (200/300), uppercase, wide. Headlines, labels and buttons on the website.</p></div>
   <div><div class="k" style="color:{C['olive']}">Bodoni Moda · editorial</div><div style="font-family:'Bodoni Moda';font-size:54px;margin:8px 0">Leave richer <em>than you arrived.</em></div><p style="font-size:16px">Regular with italic emphasis. Posters, social headlines, quotes. Echoes the logo.</p></div>
   <div><div class="k" style="color:{C['olive']}">Hanken Grotesk · text</div><div style="font-family:'Hanken Grotesk';font-weight:300;font-size:30px;line-height:1.4;margin:12px 0">A purposefully designed gathering where women connect around real opportunities.</div><p style="font-size:16px">Light (300) and Regular (400). Paragraphs, captions, interface text.</p></div>
   <div><div class="k" style="color:{C['olive']}">Antonio · numerals</div><div style="font-family:'Antonio';font-weight:300;font-size:120px;line-height:1;margin:6px 0">21 NOV 2026</div><p style="font-size:16px">Condensed Light. Dates, fees, big numbers and the footer wordmark.</p></div></div>
  <p style="margin-top:20px;font-size:16px;max-width:1300px">All four are open-source (Google Fonts, SIL OFL) and included in <b>fonts/</b>. Headlines: sentence case in Bodoni, UPPERCASE in Lexend. Keep one italic word per headline.</p><div class="num">07</div></div>''')
# 8 icons
ics = ['table', 'invitation', 'calendar', 'location', 'connection', 'opportunity', 'collaboration', 'ownership', 'wealth', 'gallery', 'conversation', 'arrow']
slides.append(f'''<div class="slide"><div class="k">07 · Iconography</div><h2>Fine lines, <em>round ends.</em></h2>
  <div class="grid" style="grid-template-columns:repeat(6,1fr);gap:18px">{''.join(f'<div class="cell" style="height:190px">{im("icons/png/" + n + ".png", "width:96px")}<small>{n}</small></div>' for n in ics)}</div>
  <p style="margin-top:24px;font-size:17px;max-width:1200px">48 px grid, 1.6 px stroke, round caps and joins, no fills (except seat dots). Use olive or ink on light backgrounds and sand on dark. SVG and PNG supplied.</p><div class="num">08</div></div>''')
# 9 art
slides.append(f'''<div class="slide"><div class="k">08 · Art and patterns</div><h2>The table, <em>seen from above.</em></h2>
  <div class="grid" style="grid-template-columns:repeat(3,1fr);grid-template-rows:260px 260px;gap:16px">
   <div style="background:url(art/ripple-olive.png) center/cover"></div><div style="background:url(art/seats-large-sand.png) center/cover;border:1px solid rgba(38,42,26,.15)"></div><div style="background:url(art/pattern-monogram-terracotta.png) center/cover"></div>
   <div style="background:url(art/pattern-seats-olive.png) center/cover"></div><div style="background:url(art/ripple-sand.png) center/cover;border:1px solid rgba(38,42,26,.15)"></div><div style="background:url(art/ripple-terracotta.png) center/cover"></div></div>
  <p style="margin-top:20px;font-size:17px;max-width:1300px">The brand device is a round table: concentric ripples of conversation and seats around a ring. Use ripples as quiet backgrounds in gold or tonal hairlines; use seats as a pattern or avatar. Keep opacity low behind text.</p><div class="num">09</div></div>''')
# 10 photography
ph = ['n-10863', 'a-6823', 'n-10816', 'a-6565']
slides.append(f'''<div class="slide"><div class="k">09 · Photography</div><h2>Warm, candid, <em>documentary.</em></h2>
  <div class="grid" style="grid-template-columns:repeat(4,1fr);gap:16px">{''.join(f'<div style="height:330px;background:url({PH}{p}-sm.jpg) center/cover"></div>' for p in ph)}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;margin-top:26px"><div><div class="li"><b>Look</b>Natural light, real moments, white florals, candles.</div><div class="li"><b>People</b>Laughing, listening, speaking. Never posed stock.</div><div class="li"><b>Crop</b>Faces clear of text; keep the table in frame.</div></div>
  <div><div class="li"><b>Quality</b>1,500 px or wider, sharp. Do not use low-resolution or upscaled images.</div><div class="li"><b>Credit</b>Credit the photographer and confirm usage rights.</div><div class="li"><b>Treatment</b>Black and white for the founder; full colour elsewhere. No filters.</div></div></div><div class="num">10</div></div>''')
# 11 social
sv = ['instagram/01-what-we-do.png', 'instagram/03-next-event-lagos.png', 'instagram/05-past-event-nairobi.png', 'instagram/13-participation.png']
av = ['avatar-olive-monogram.png', 'avatar-sand-seal.png', 'avatar-terracotta-monogram.png']
slides.append(f'''<div class="slide"><div class="k">10 · Social</div><h2>Consistent, <em>calm,</em> confident.</h2>
  <div style="display:flex;gap:22px;align-items:flex-start">{''.join(f'<img src="social/{s}" style="height:520px;width:auto">' for s in sv)}<div style="display:grid;gap:16px;padding-left:6px">{''.join(f'<img src="avatars/{a}" style="width:130px;height:130px;border-radius:50%">' for a in av)}</div></div>
  <p style="margin-top:22px;font-size:17px;max-width:1300px">Templates: Instagram posts 1080×1350, stories 1080×1920, highlight covers, LinkedIn 1200×627, banners 1584×396 and 1128×191, and a five-slide carousel. One idea per graphic, one italic word, always the URL.</p><div class="num">11</div></div>''')
# 12 posters
slides.append(f'''<div class="slide terra"><div class="k">11 · Posters</div><h2 style="color:{C['sand']}">Invitation and <em>remembrance.</em></h2>
  <div style="display:flex;gap:34px;align-items:flex-start"><img src="posters/poster-lagos-invitation.png" style="height:640px;width:auto"><img src="posters/poster-accra-recap.png" style="height:640px;width:auto"><img src="posters/poster-nairobi-recap.png" style="height:640px;width:auto"><p style="font-size:17px;max-width:250px">Sand background, gold double frame, ripple device. Bodoni headline with one italic word, Lexend labels, an olive base panel. Posters are 2:3, supplied as PNG and PDF.</p></div><div class="num">12</div></div>''')
# 13 voice
slides.append(f'''<div class="slide"><div class="k">12 · Voice</div><h2>Warm, assured, <em>specific.</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:70px"><div><div class="k" style="color:{C['olive']};margin-bottom:10px">We say</div>
   <div class="li" style="font-family:'Bodoni Moda';font-size:26px">Come to the table.</div><div class="li" style="font-family:'Bodoni Moda';font-size:26px">Leave richer than you arrived.</div><div class="li" style="font-family:'Bodoni Moda';font-size:26px">From conversation to action.</div><div class="li" style="font-family:'Bodoni Moda';font-size:26px">Different women. Shared ambition. Bigger possibilities.</div><div class="li" style="font-family:'Bodoni Moda';font-size:26px">How do we move more women from success to ownership?</div></div>
   <div><div class="k" style="color:{C['olive']};margin-bottom:10px">Principles</div><div class="li"><b>Invite</b>Speak to a guest, not a crowd.</div><div class="li"><b>Be precise</b>Dates, venues, rates. No hype.</div><div class="li"><b>Own it</b>Ownership, not just achievement.</div><div class="li"><b>Be generous</b>Participation and contribution over pitches.</div><div class="li"><b>Stay true</b>Only real numbers and real women.</div></div></div><div class="num">13</div></div>''')
# 14 index
slides.append(f'''<div class="slide olive"><div class="k">13 · File index</div><h2 style="color:{C['sand']}">What is <em>in the kit.</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 70px;font-size:20px">
   <div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">logos/</b>SVG + PNG, 7 marks × 5 colours</div><div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">icons/</b>12 icons, SVG + PNG</div>
   <div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">avatars/</b>8 profile images, 1080 px</div><div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">art/</b>Ripples, seats, patterns</div>
   <div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">fonts/</b>Lexend Zetta, Bodoni Moda, Hanken Grotesk, Antonio</div><div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">posters/</b>Lagos, Accra, Nairobi (PNG + PDF)</div>
   <div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">social/</b>Instagram, stories, highlights, LinkedIn, carousel</div><div class="li" style="border-color:rgba(248,242,229,.35)"><b style="color:{C['gold']}">colors/</b>Swatches, CSS variables</div></div>
  <p style="margin-top:40px;color:{C['sand']};opacity:.9">Questions: info@thewealthtableglobal.com · +234 8096000049 · 10, Onisiwo Road, Ikoyi, Lagos</p><div class="num">14</div></div>''')

html = f'<!doctype html><html><head><meta charset="utf-8"><title>The Wealth Table: Brand Guidelines</title><style>{BASE_CSS}{css}</style></head><body>{"".join(slides)}</body></html>'
p = f'{KIT}/Wealth-Table-Brand-Guidelines.html'
open(p, 'w', encoding='utf8').write(html)
# PDF: one 1600x1000 page per slide
JOBS.append(dict(html=FILE + p, w=W, h=H, out=f'{KIT}/Wealth-Table-Brand-Guidelines.pdf', scale=1, transparent=False, pdf=True))

# colour files
os.makedirs(f'{KIT}/colors', exist_ok=True)
open(f'{KIT}/colors/colors.css', 'w').write(':root{\n' + '\n'.join(f'  --wt-{n.lower().replace(" ", "-")}: {h};' for n, h, *_ in PAL) + '\n}\n')
open(f'{KIT}/colors/palette.txt', 'w').write('\n'.join(f'{n:12} {h}  RGB {rgb(h)}  CMYK~{cmyk(h)}  {u}' for n, h, u, _ in PAL))
sw = ''.join(f'<div style="background:{h};color:{C["sand"] if n in ("Olive","Terracotta","Deep Olive","Ink") else C["ink"]};padding:26px;height:300px;display:flex;flex-direction:column;justify-content:flex-end;font-size:20px;{"border:1px solid #ccc" if n in ("Sand","Blush") else ""}"><b style="font-family:Lexend Zetta;font-weight:300;letter-spacing:.12em;text-transform:uppercase;font-size:17px">{n}</b>{h}</div>' for n, h, *_ in PAL)
render('swatches', page(f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;width:1600px">{sw}</div>', 1600, 600), 1600, 600, f'{KIT}/colors/swatches.png')
flush()
print('guidelines done')
