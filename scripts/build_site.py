#!/usr/bin/env python3
"""Generates index.html and the two gallery pages from scripts/content.json.
Run from the repo root:  python3 scripts/build_site.py
Static output is committed so Vercel needs no build step."""
import json, html, os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = json.load(open(os.path.join(ROOT, 'scripts/content.json'), encoding='utf8'))
E = html.escape
SITE_URL = os.environ.get('SITE_URL', '').rstrip('/')          # e.g. https://wealthtable.vercel.app (used for og:image)

ALT = dict(W['alt'])
ALT.update({'n-10820': 'Two guests chatting in Nairobi', 'n-10827': 'A speaker at the Nairobi table', 'n-10832': 'A speaker in front of The Wealth Table backdrop in Nairobi',
            'a-6585': 'Guests in conversation in Accra'})
NAIROBI = ['n-10863', 'n-10880', 'n-10840', 'n-10860', 'n-10816', 'n-10817', 'n-10836', 'n-10844', 'n-10887', 'n-10857', 'n-10849', 'n-10820', 'n-10827', 'n-10832']
ACCRA = ['a-6762', 'a-6812', 'a-6823', 'a-6797', 'a-6565', 'a-6679', 'a-6626', 'a-6917', 'a-6923', 'a-6949', 'a-6912', 'a-6618', 'a-6585']
CITY = {
    'nairobi': dict(W['nairobi'], flag='ke', place='Nairobi, Kenya', venue_short='Kwetu Nairobi', gallery=NAIROBI, slug='nairobi', iso='KE'),
    'accra': dict(W['accra'], flag='gh', place='Accra, Ghana', venue_short='Cantonments, Accra', gallery=ACCRA, slug='accra', iso='GH'),
}
PHOTO_DIR = os.path.join(ROOT, 'assets/img/photos')


def dims(name, small=False, prefix='assets/img/photos/'):
    p = os.path.join(ROOT, prefix.replace('../', ''), name + ('-sm' if small else '') + '.jpg')
    with Image.open(p) as im:
        return im.size


def img(name, alt=None, small=False, lazy=True, cls='', style='', prefix='assets/img/photos/'):
    w, h = dims(name, small, prefix)
    a = E(alt if alt is not None else ALT.get(name, ''))
    return (f'<img src="{prefix}{name}{"-sm" if small else ""}.jpg" alt="{a}" width="{w}" height="{h}"'
            f'{" loading=\"lazy\" decoding=\"async\"" if lazy else " fetchpriority=\"high\""}'
            f'{f" class=\"{cls}\"" if cls else ""}{f" style=\"{style}\"" if style else ""}>')


def flag(code, big=False, prefix='assets/img/flags/'):
    names = {'ke': 'Kenya', 'gh': 'Ghana', 'ng': 'Nigeria'}
    return f'<i class="flag{" lg" if big else ""}"><img src="{prefix}{code}.svg" alt="Flag of {names[code]}" width="90" height="60"></i>'


REG = '<a class="btn{extra}" href="#" data-luma>{label} <i>→</i></a>'


def reg(label='Register your interest', extra=''):
    return REG.format(label=label, extra=(' ' + extra) if extra else '')


def head(title, desc, canon, og_img, extra_head='', loading=False):
    og = (SITE_URL + '/' + og_img) if SITE_URL else '/' + og_img
    return f'''<!doctype html>
<html lang="en"{' class="is-loading"' if loading else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#8f4b38">
<link rel="apple-touch-icon" href="{'' if canon == 'home' else '../../'}assets/img/apple-touch-icon.png">
<link rel="icon" type="image/png" href="{'' if canon == 'home' else '../../'}assets/img/favicon-white.png" media="(prefers-color-scheme: dark)">
<link rel="icon" type="image/png" href="{'' if canon == 'home' else '../../'}assets/img/favicon-dark.png" media="(prefers-color-scheme: light)">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
{extra_head}'''


def css_links(pre):
    return (f'<link rel="stylesheet" href="{pre}assets/fonts/fonts.css">\n<link rel="stylesheet" href="{pre}assets/css/base.css">\n<link rel="stylesheet" href="{pre}assets/css/site.css">\n</head>\n')


def menu_html(pre, home):
    h = '' if home else pre
    return f'''<div class="menu" id="menu" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="top"><img src="{pre}assets/img/logo/wordmark-cream.png" alt="The Wealth Table" width="1588" height="230"><button id="closeMenu">Close</button></div>
  <nav aria-label="Menu">
    <a href="{h}#top"><small>01</small>Home</a>
    <a href="{h}#about"><small>02</small>About</a>
    <a href="{h}#tables"><small>03</small>The tables</a>
    <a href="{h}#faq"><small>04</small>Questions</a>
    <a class="nextbox" href="{h}#lagos"><span><small>Lagos · 21 November 2026</small>View next event</span><span aria-hidden="true">→</span></a>
  </nav>
  <div class="foot"><span>{E(W['email'])}</span><span>{E(W['phone'])}</span><span>{E(W['address'])}</span></div>
</div>
'''


def nav_html(pre, home):
    h = '' if home else pre
    return f'''<header class="nav" id="nav">
  <a class="reg" href="#" data-luma><span>Register interest</span></a>
  <a class="logo" href="{h}#top" aria-label="The Wealth Table, home"><img class="c" src="{pre}assets/img/logo/wordmark-cream.png" alt="The Wealth Table" width="1588" height="230"><img class="k" src="{pre}assets/img/logo/wordmark-olive.png" alt="" width="1588" height="230"></a>
  <button class="bg" id="openMenu" aria-label="Open menu" aria-haspopup="dialog" aria-expanded="false"><i></i><i></i></button>
</header>
'''


def footer_html(pre, home):
    h = '' if home else pre
    return f'''<footer data-nb="rgba(227,225,212,.6)" data-fg="ink">
  <div class="fg">
    <div><img src="{pre}assets/img/logo/lockup-full-olive.png" alt="The Wealth Table. Leave richer than you arrived." width="180" height="85" style="width:180px;height:auto;margin-bottom:1rem"><p>{E(W['footerLine'])}</p></div>
    <div><b>Explore</b><a href="{h}#about">About</a><br><a href="{h}#tables">The tables</a><br><a href="{h}#gatherings">Gatherings</a><br><a href="{h}#faq">Questions</a></div>
    <div><b>Contact</b><a href="mailto:{E(W['email'])}">{E(W['email'])}</a><br>{E(W['phone'])}<br>{E(W['address'])}</div>
    <div><b>Social</b><a href="{W['social']['linkedin']}" target="_blank" rel="noopener">LinkedIn</a><br><a href="{W['social']['instagram']}" target="_blank" rel="noopener">Instagram</a><br><a href="https://radiantcollectivecapital.vercel.app" target="_blank" rel="noopener">Radiant Collective Capital</a></div>
  </div>
  <div class="fb"><span>© 2026 The Wealth Table Global. All rights reserved.</span><span>Lagos · Accra · Nairobi</span></div>
  <div class="fw" aria-hidden="true">The Wealth Table</div>
</footer>
'''


def scripts(pre):
    return f'<script src="{pre}assets/js/config.js"></script>\n<script src="{pre}assets/js/site.js" defer></script>\n</body>\n</html>\n'


PRELOAD = '''<div class="pre" aria-hidden="true">
  <div class="h t"></div><div class="h b"></div>
  <div class="c">
    <div class="m mono"><img src="assets/img/logo/wt-monogram-cream.png" alt="" width="777" height="338"></div>
    <div class="rule"></div>
    <div class="m word"><img src="assets/img/logo/wordmark-cream.png" alt="" width="1588" height="230"></div>
    <div class="tag"><img src="assets/img/logo/tagline-cream.png" alt="" width="1067" height="74"></div>
  </div>
  <div class="count">00</div><div class="bar"></div>
</div>
<noscript><style>.pre{display:none}.mask>span{transform:none!important}.nav,.dock{transform:translate(-50%,0)!important}[data-reveal]{opacity:1!important;transform:none!important}.veil{clip-path:none!important}html.is-loading,html.is-loading body{overflow:auto}</style></noscript>
'''


def recap(c, rev):
    n = c['slug']
    body = f'<p>{E(c["body"][0])}</p>'
    return f'''<article class="gath{' rev' if rev else ''}" id="{n}">
        <div class="im" data-reveal><div class="ph">{img(c['gallery'][4] if n == 'nairobi' else c['gallery'][0], style='object-position:50% 45%')}</div></div>
        <div class="tx" data-reveal style="--d:120">
          <p class="tag">{E(c['venue_short'])}</p>
          <h3 class="H">{E(c['title']).replace(' – ', '<br>')}</h3>
          <div class="meta">
            <div><span>Date</span>{E(c['date'])}</div>
            <div><span>Women</span>{'≈ ' if n == 'accra' else ''}{c['women']}</div>
            <div class="loc"><span>Location</span><div>{flag(c['flag'], True)}<b>{E(c['place'])}</b></div></div>
          </div>
          {body}
          <p class="pull">{E(c['pull'])}</p>
          <div class="acts"><a class="btn" href="gallery/{n}/">View gallery <i>→</i></a></div>
        </div>
      </article>'''


def hero_video():
    """Adds the hero video when assets/video/hero.mp4 exists (drop the file in and rebuild)."""
    if not os.path.exists(os.path.join(ROOT, 'assets/video/hero.mp4')):
        return ''
    webm = '<source src="assets/video/hero.webm" type="video/webm">' if os.path.exists(os.path.join(ROOT, 'assets/video/hero.webm')) else ''
    return ('<video class="hero-video" muted playsinline loop preload="auto" aria-hidden="true" tabindex="-1" poster="assets/img/photos/a-6797.jpg">'
            + webm + '<source src="assets/video/hero.mp4" type="video/mp4"></video>')


def build_home():
    L = W['lagos']
    cloud = ['n-10840', 'a-6618', 'n-10817', 'a-6949', 'n-10816', 'a-6626', 'a-6917']
    par = [.12, -.08, .16, -.1, .14, -.12, .1]
    cloud_html = ''.join(f'<div class="s s{i + 1}" data-par="{par[i]}"><div class="ph">{img(n, small=True)}</div></div>' for i, n in enumerate(cloud))
    faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in W['faq'])
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Event", "name": "The Wealth Table Lagos", "startDate": "2026-11-21T11:00:00+01:00", "endDate": "2026-11-21T17:00:00+01:00",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled",
        "location": {"@type": "Place", "name": "Civic Centre", "address": {"@type": "PostalAddress", "addressLocality": "Victoria Island, Lagos", "addressCountry": "NG"}},
        "description": "An invitation-only gathering of women leaders, entrepreneurs, investors and wealth builders exploring one question: how do we move more women from success to ownership?",
        "organizer": {"@type": "Organization", "name": "The Wealth Table Global", "url": SITE_URL or "/"},
        "offers": [{"@type": "Offer", "name": "RCC member", "price": "200", "priceCurrency": "USD"}, {"@type": "Offer", "name": "Non-member", "price": "300", "priceCurrency": "USD"}]
    })
    out = head('The Wealth Table | Leave richer than you arrived.',
               'An invitation-only gathering where women connect around real opportunities, shared ambitions and the future of wealth and ownership. Nairobi, Accra, Lagos.',
               'home', 'assets/img/og.jpg', f'<script type="application/ld+json">{ld}</script>\n', loading=True)
    out += '<script>if(matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.remove("is-loading")</script>\n'
    out += css_links('')
    out += '<body>\n<a class="skip" href="#about">Skip to content</a>\n' + PRELOAD + nav_html('', True) + menu_html('', True)
    out += f'''<main id="top">
  <section class="hero" data-nb="rgba(3,9,13,.19)" data-fg="cream">
    <div class="bgi">{img('a-6797', lazy=False, style='object-position:50% 55%')}{hero_video()}</div>
    <h1><span class="mask"><span style="--d:300">Leave richer</span></span><span class="mask"><span style="--d:440">than you arrived.</span></span></h1>
    <p class="sub"><span class="mask"><span style="--d:760">An invitation-only gathering of women building, investing and owning.</span></span></p>
    <a class="dock" href="#" data-luma aria-label="Register your interest for The Wealth Table Lagos">
      <span class="t"><b>Next gathering · Sat 21 November 2026 · Civic Centre, VI Lagos</b><span>Register your interest</span></span>
      <span class="go">Register <span aria-hidden="true">→</span></span>
    </a>
  </section>

  <section class="sec on-sand" id="about" data-nb="rgba(248,242,229,.6)" data-fg="ink">
    <div class="state">
      <h2 class="H" data-reveal>From conversation<br>to action.</h2>
      <div class="r" data-reveal style="--d:120"><p>The Wealth Table is a purposefully designed gathering where women connect around real opportunities, shared ambitions, and the future of wealth and ownership.</p><a class="btn" href="#faq" style="justify-self:start">What to expect <i>→</i></a></div>
    </div>
    <div class="cards" id="tables">
      <a class="tcard solid" href="#lagos" data-reveal><span class="tag">Next · 21 Nov 2026</span><span class="big">Lagos</span><div class="b"><span>Civic Centre, VI Lagos</span><span>Details <i>+</i></span></div></a>
      <a class="tcard" href="#gatherings" data-reveal style="--d:100">{img('a-6823', small=True, style='object-position:50% 25%')}<span class="chip">{flag('gh')}</span><h3>Accra</h3><div class="b"><span>3 October 2026<br>Cantonments, Ghana</span><span>Explore <i>+</i></span></div></a>
      <a class="tcard" href="#gatherings" data-reveal style="--d:200">{img('n-10857', small=True, style='object-position:36% 40%')}<span class="chip">{flag('ke')}</span><h3>Nairobi</h3><div class="b"><span>13 June 2026<br>Kwetu Nairobi, Kenya</span><span>Explore <i>+</i></span></div></a>
    </div>
  </section>

  <section class="sec on-terra" id="lagos" data-nb="rgba(143,75,56,.55)" data-fg="cream">
    <div class="split">
      <div class="tx">
        <p class="tag">The Wealth Table Conference</p>
        <h2 class="H" data-reveal>The Wealth Table™<br>Lagos</h2>
        <div class="facts"><div><b>Date</b><span>{E(L['date'])}</span></div><div><b>Time</b><span>{E(L['time'])}</span></div><div><b>Venue</b><span>{E(L['venue'])}</span></div></div>
        <p style="max-width:54ch;opacity:.92"><b style="font-weight:500">{E(L['kicker'])}</b> {E(L['body'])}</p>
        <p class="q">{E(L['question'])}</p>
        <div class="fees"><div>RCC members<b>{E(L['fee']['rcc'])}</b></div><div>Non-members<b>{E(L['fee']['non'])}</b></div></div>
        <div>{reg(extra='fill')}</div>
      </div>
      <div class="pf" data-reveal>{img('poster-lagos', alt='The Wealth Table Lagos invitation: Saturday 21 November 2026, Civic Centre, Victoria Island', prefix='assets/img/')}</div>
    </div>
  </section>

  <section class="sec on-olive cloud" id="cloud" data-nb="rgba(79,91,42,.55)" data-fg="cream" aria-label="Moments from the gatherings">
    {cloud_html}
    <div class="mid"><p class="tag">What the list gives you</p><h2 class="H" data-reveal>Come to<br>the table.</h2><div class="gv">{''.join(f'<p>{E(t)}</p>' for t in W['gives'])}</div>{reg()}</div>
  </section>

  <section class="sec on-blush" id="gatherings" data-nb="rgba(245,238,233,.6)" data-fg="ink">
    <p class="tag" style="margin-bottom:2.6rem">Where we have been</p>
    {recap(CITY['nairobi'], False)}
    {recap(CITY['accra'], True)}
  </section>

  <section class="sec on-stone" id="host" data-nb="rgba(227,225,212,.6)" data-fg="ink">
    <div class="founder">
      <div class="ph veil">{img('n-10849', style='object-position:42% 40%')}</div>
      <div class="tx"><p class="tag">About the founder</p><h2 class="H">Udo Okonjo</h2><p>{E(W['founder']['body'][1])}</p><p>{E(W['founder']['body'][2])}</p><p class="H" style="font-size:clamp(.95rem,1.5vw,1.3rem);color:var(--terra)">{E(W['founder']['invitation'])}</p>
        <div style="display:flex;gap:.8rem;flex-wrap:wrap">{reg(extra='dark')}<a class="btn" href="https://radiantcollectivecapital.vercel.app" target="_blank" rel="noopener">Radiant Collective Capital <i>↗</i></a></div></div>
    </div>
  </section>

  <section class="sec on-sand" id="faq" data-nb="rgba(248,242,229,.6)" data-fg="ink">
    <div class="faqs"><div><p class="tag">Frequently asked questions</p><h2 class="H" style="margin-top:1.2rem">The Wealth Table<br>FAQ</h2></div><div class="faq">{faq}</div></div>
  </section>

  <section class="sec on-olive" id="register" data-nb="rgba(79,91,42,.55)" data-fg="cream">
    <div class="cta-big">
      <p class="tag">The Wealth Table</p>
      <h2 class="H" data-reveal>Join us, we are about<br>to do it again.</h2>
      <p>{E(W['closing']['body'])}</p>
      {reg('Register your interest', 'fill xl')}
    </div>
  </section>
</main>
'''
    out += footer_html('', True) + scripts('')
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf8').write(out)


def build_gallery(c, other):
    n = c['slug']
    pre = '../../'
    figs = ''.join(
        f'<figure data-lb="{pre}assets/img/photos/{p}.jpg" data-reveal style="--d:{(i % 3) * 80}">{img(p, small=True, prefix=pre + "assets/img/photos/")}</figure>'
        for i, p in enumerate(c['gallery']))
    out = head(f'{c["city"]} Gallery | The Wealth Table', f'Photographs from The Wealth Table {c["city"]}, {c["date"]}, {c["venue_short"]}.', 'gallery', 'assets/img/og.jpg')
    out += css_links(pre)
    out += '<body>\n<a class="skip" href="#gallery">Skip to the gallery</a>\n' + nav_html(pre, False) + menu_html(pre, False)
    out += f'''<main id="top">
  <section class="on-sand" data-nb="rgba(248,242,229,.6)" data-fg="ink">
    <div class="ghero">
      <div>
        <a class="back" href="{pre}#gatherings">← Back to the tables</a>
        <h1 class="mask"><span>{E(c['city'])}<br>Gallery</span></h1>
      </div>
      <div class="r">
        <p class="tag">{E(c['venue_short'])}</p>
        <div class="meta">
          <div><span>Date</span>{E(c['date'])}</div>
          <div><span>Women</span>{'≈ ' if n == 'accra' else ''}{c['women']}</div>
          <div class="loc"><span>Location</span><div>{flag(c['flag'], True, pre + 'assets/img/flags/')}<b>{E(c['place'])}</b></div></div>
        </div>
        <p>{E(c['pull'])}</p>
        <div>{reg('Register your interest')}</div>
      </div>
    </div>
    <div class="masonry" id="gallery">{figs}</div>
    <div class="gnav">
      <a href="{pre}#gatherings">← All gatherings</a>
      <a href="{pre}gallery/{other['slug']}/">{E(other['city'])} gallery →</a>
    </div>
  </section>
</main>
'''
    out += footer_html(pre, False)
    out += f'<script>document.documentElement.classList.add("is-loaded");document.querySelectorAll(".ghero .mask").forEach(function(m){{m.classList.add("is-in")}})</script>\n' + scripts(pre)
    d = os.path.join(ROOT, 'gallery', n); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf8').write(out)


if __name__ == '__main__':
    build_home()
    build_gallery(CITY['nairobi'], CITY['accra'])
    build_gallery(CITY['accra'], CITY['nairobi'])
    print('built')
