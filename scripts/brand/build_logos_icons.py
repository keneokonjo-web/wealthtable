import math
def dots_ring(cx, cy, r, n, rr):
    return ''.join(f'<circle cx="{cx + r * math.cos(2 * math.pi * i / n - math.pi / 2):.2f}" cy="{cy + r * math.sin(2 * math.pi * i / n - math.pi / 2):.2f}" r="{rr}" fill="currentColor" stroke="none"/>' for i in range(n))


ICONS = {
    'table': '<circle cx="24" cy="24" r="8.5"/>' + dots_ring(24, 24, 16.5, 8, 2.3),
    'invitation': '<rect x="6" y="12" width="36" height="24" rx="2"/><path d="M6 14l18 13 18-13"/><circle cx="24" cy="27" r="3.4"/>',
    'calendar': '<rect x="7" y="10" width="34" height="31" rx="3"/><path d="M7 19h34M16 6v8M32 6v8"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="currentColor" stroke="none"/>' for x in (15, 24, 33) for y in (26, 33)),
    'location': '<path d="M24 43S11 30 11 20a13 13 0 0 1 26 0c0 10-13 23-13 23z"/><circle cx="24" cy="20" r="4.5"/>',
    'connection': '<circle cx="18" cy="24" r="11"/><circle cx="30" cy="24" r="11"/>',
    'opportunity': '<path d="M8 37l13-13 7 7 13-15"/><path d="M31 16h10v10"/>',
    'collaboration': '<circle cx="24" cy="17" r="9"/><circle cx="16.5" cy="30" r="9"/><circle cx="31.5" cy="30" r="9"/>',
    'ownership': '<circle cx="15" cy="24" r="8"/><path d="M23 24h19M35 24v7M41 24v5"/>',
    'wealth': '<circle cx="24" cy="24" r="16"/><circle cx="24" cy="24" r="11"/><path d="M24 18.5l5.5 5.5-5.5 5.5-5.5-5.5z"/>',
    'gallery': '<rect x="6" y="9" width="36" height="30" rx="2"/><path d="M6 33l11-11 8 8 5-5 12 11"/><circle cx="33" cy="17" r="3"/>',
    'conversation': '<rect x="18" y="6" width="12" height="22" rx="6"/><path d="M12 23a12 12 0 0 0 24 0M24 35v7M17 42h14"/>',
    'arrow': '<path d="M8 24h31M29 14l10 10-10 10"/>',
}
