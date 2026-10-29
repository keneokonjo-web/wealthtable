"""African-inspired pattern system for the brand kit (original geometric designs, loosely inspired by
West African woven cloth (kente / aso-oke strips), Yoruba adire circles, Malian mud-cloth marks,
East African beadwork triangles, and Akan 'chain' (unity) motifs). All thin-line and tonal so they
sit quietly in the background. Colourways are parameters, so they can follow any palette change."""
import math

COLORWAYS = {
    # name: (background, line, accent)
    'ivory-burgundy': ('#F4EADB', '#5A0F1C', '#B8923A'),
    'burgundy-gold': ('#4A0A15', '#C9A24B', '#E9D9B8'),
    'sand-terracotta': ('#F8F2E5', '#8F4B38', '#B8923A'),
    'ink-sand': ('#262A1A', '#D9CDB4', '#B8923A'),
}


def _svg(w, h, inner, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{b}{inner}</svg>'


def kente(bg, ln, ac, sw=2.0):
    """Woven strips: zigzag / diamonds / chequer / ladder / sawtooth. Tile 240 x 240, repeats both ways."""
    o = []
    # separators (the weave lines)
    for y in (0, 48, 96, 144, 192):
        o.append(f'<line x1="0" y1="{y}" x2="240" y2="{y}" stroke="{ln}" stroke-width="{sw * 1.5}"/>')
    # band 1: zigzag
    pts = ' '.join(f'{x},{40 if (x // 20) % 2 == 0 else 8}' for x in range(0, 261, 20))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{ln}" stroke-width="{sw}" stroke-linejoin="miter"/>')
    pts2 = ' '.join(f'{x},{44 if (x // 20) % 2 == 0 else 12}' for x in range(0, 261, 20))
    o.append(f'<polyline points="{pts2}" fill="none" stroke="{ac}" stroke-width="{sw * .7}" stroke-linejoin="miter" opacity=".9"/>')
    # band 2: diamonds with inner diamond
    for k in range(6):
        cx = 20 + 40 * k
        o.append(f'<path d="M{cx} 56L{cx + 16} 72L{cx} 88L{cx - 16} 72Z" fill="none" stroke="{ln}" stroke-width="{sw}"/>')
        o.append(f'<path d="M{cx} 66L{cx + 6} 72L{cx} 78L{cx - 6} 72Z" fill="{ac}"/>')
    # band 3: chequer
    for r in range(3):
        for c in range(15):
            if (r + c) % 2 == 0:
                o.append(f'<rect x="{c * 16}" y="{96 + r * 16}" width="16" height="16" fill="{ln}" opacity=".85"/>')
    # band 4: ladder (three lines + rungs)
    for y in (152, 168, 184):
        o.append(f'<line x1="0" y1="{y}" x2="240" y2="{y}" stroke="{ln}" stroke-width="{sw * .8}"/>')
    for x in range(10, 240, 20):
        o.append(f'<line x1="{x}" y1="152" x2="{x}" y2="184" stroke="{ac}" stroke-width="{sw * .8}"/>')
    # band 5: sawtooth triangles
    for k in range(12):
        x = k * 20
        o.append(f'<path d="M{x} 236L{x + 10} 200L{x + 20} 236Z" fill="{ln}" opacity=".9"/>')
    return _svg(240, 240, ''.join(o), bg)


def adire(bg, ln, ac, sw=1.8):
    """Adire-style circles, crosses and dots. Tile 160 x 160."""
    o = []
    for (cx, cy) in ((40, 40), (120, 120)):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="27" fill="none" stroke="{ln}" stroke-width="{sw}"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="none" stroke="{ln}" stroke-width="{sw}"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{ac}"/>')
        for a in range(0, 360, 45):
            x = cx + 35 * math.cos(math.radians(a)); y = cy + 35 * math.sin(math.radians(a))
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.8" fill="{ln}"/>')
    for (cx, cy) in ((120, 40), (40, 120)):
        o.append(f'<path d="M{cx - 14} {cy}H{cx + 14}M{cx} {cy - 14}V{cy + 14}" stroke="{ln}" stroke-width="{sw * 1.2}" stroke-linecap="square"/>')
        for dx, dy in ((-20, -20), (20, -20), (-20, 20), (20, 20)):
            o.append(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="3" fill="none" stroke="{ac}" stroke-width="{sw}"/>')
    return _svg(160, 160, ''.join(o), bg)


def mudcloth(bg, ln, ac, sw=2.4):
    """Mud-cloth inspired columns of zigzag, crosses and dotted lines. Tile 240 x 240."""
    o = []
    # column A: vertical zigzag with squares
    pts = ' '.join(f'{(12 if (y // 20) % 2 == 0 else 52)},{y}' for y in range(0, 261, 20))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{ln}" stroke-width="{sw}"/>')
    for y in range(10, 240, 40):
        o.append(f'<rect x="{66}" y="{y}" width="8" height="8" fill="{ac}"/>')
    # column B: crosses
    for y in range(12, 240, 24):
        for x in (100, 130):
            o.append(f'<path d="M{x - 6} {y}H{x + 6}M{x} {y - 6}V{y + 6}" stroke="{ln}" stroke-width="{sw * .8}"/>')
    # column C: double vertical lines + dots
    o.append(f'<line x1="176" y1="0" x2="176" y2="240" stroke="{ln}" stroke-width="{sw}"/><line x1="188" y1="0" x2="188" y2="240" stroke="{ln}" stroke-width="{sw * .6}"/>')
    for y in range(8, 240, 16):
        o.append(f'<circle cx="206" cy="{y}" r="2.6" fill="{ln}"/>')
    o.append(f'<line x1="228" y1="0" x2="228" y2="240" stroke="{ac}" stroke-width="{sw * .6}" stroke-dasharray="6 6"/>')
    # column dividers
    for x in (84, 160, 0):
        o.append(f'<line x1="{x}" y1="0" x2="{x}" y2="240" stroke="{ln}" stroke-width="{sw * .5}" opacity=".6"/>')
    return _svg(240, 240, ''.join(o), bg)


def beadwork(bg, ln, ac, sw=1.8):
    """Beadwork-inspired triangle rows. Tile 240 x 120."""
    o = []
    for k in range(6):
        x = k * 40
        o.append(f'<path d="M{x} 36L{x + 20} 4L{x + 40} 36Z" fill="{ln}"/>')
        o.append(f'<path d="M{x + 20} 4L{x + 40} 36L{x + 60} 4" fill="none" stroke="{ln}" stroke-width="{sw}"/>')
        o.append(f'<path d="M{x + 14} 36L{x + 20} 26L{x + 26} 36Z" fill="{bg}"/>')
    o.append(f'<line x1="0" y1="46" x2="240" y2="46" stroke="{ac}" stroke-width="{sw}"/>')
    for k in range(12):
        cx = 10 + 20 * k
        o.append(f'<path d="M{cx} 54L{cx + 8} 62L{cx} 70L{cx - 8} 62Z" fill="{ac}"/>')
    o.append(f'<line x1="0" y1="78" x2="240" y2="78" stroke="{ac}" stroke-width="{sw}"/>')
    for k in range(6):
        x = k * 40
        o.append(f'<path d="M{x} 84L{x + 20} 116L{x + 40} 84Z" fill="none" stroke="{ln}" stroke-width="{sw}"/>')
        o.append(f'<circle cx="{x + 20}" cy="94" r="2.6" fill="{ln}"/>')
    return _svg(240, 120, ''.join(o), bg)


def chain(bg, ln, ac, sw=1.8):
    """Interlocking diamond chain (unity). Tile 120 x 120."""
    o = []
    for (cx, cy) in ((60, 60), (0, 0), (120, 0), (0, 120), (120, 120)):
        o.append(f'<path d="M{cx} {cy - 42}L{cx + 42} {cy}L{cx} {cy + 42}L{cx - 42} {cy}Z" fill="none" stroke="{ln}" stroke-width="{sw}"/>')
        o.append(f'<path d="M{cx} {cy - 26}L{cx + 26} {cy}L{cx} {cy + 26}L{cx - 26} {cy}Z" fill="none" stroke="{ln}" stroke-width="{sw * .6}" opacity=".7"/>')
    o.append(f'<path d="M60 52L68 60L60 68L52 60Z" fill="{ac}"/>')
    for (x, y) in ((60, 0), (60, 120), (0, 60), (120, 60)):
        o.append(f'<path d="M{x} {y - 5}L{x + 5} {y}L{x} {y + 5}L{x - 5} {y}Z" fill="{ac}"/>')
    return _svg(120, 120, ''.join(o), bg)


PATTERNS = {'kente': kente, 'adire': adire, 'mudcloth': mudcloth, 'beadwork': beadwork, 'chain': chain}


def strip(width, height, ln, ac, bg=None):
    """A thin woven border strip (zigzag + diamonds between rules) for use on posters. Repeats every 40px."""
    o = []
    mid = height / 2
    o.append(f'<line x1="0" y1="1" x2="{width}" y2="1" stroke="{ln}" stroke-width="1.6"/>')
    o.append(f'<line x1="0" y1="{height - 1}" x2="{width}" y2="{height - 1}" stroke="{ln}" stroke-width="1.6"/>')
    n = int(width // 40) + 2
    pts = ' '.join(f'{k * 20},{height * .32 if k % 2 == 0 else height * .68}' for k in range(0, n * 2 + 2))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{ln}" stroke-width="1.4"/>')
    for k in range(n):
        cx = 20 + 40 * k
        o.append(f'<path d="M{cx} {mid - 5}L{cx + 5} {mid}L{cx} {mid + 5}L{cx - 5} {mid}Z" fill="{ac}"/>')
    return _svg(int(width), int(height), ''.join(o), bg)
