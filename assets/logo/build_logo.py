"""Builds queenright-logo.svg (viewBox 0 0 100 100).

Layers: navy background = the system; white node crown = the agent team;
honey dot on the top edge = the accountable human ("queen");
slate band = the platform underneath.
"""
from pathlib import Path

NAVY, HONEY, SLATE, WHITE = "#1F2A44", "#F2A900", "#8FA3C7", "#FFFFFF"
S, OX, TOPY = .76, 12, 18          # crown scale, x offset, top edge of the background
OY = TOPY - 10 * S                 # puts the queen node exactly on that edge
CROWN = [(20, 72), (14, 42), (34, 60), (50, 10), (66, 60), (86, 42), (80, 72)]
QUEEN = 3
BAND_Y = OY + 72 * S + 6


def build():
    p = [(OX + x * S, OY + y * S) for x, y in CROWN]
    poly = " ".join(f"{x:.2f},{y:.2f}" for x, y in p)
    out = [f'<rect x="6" y="{TOPY}" width="88" height="76" rx="16" fill="{NAVY}"/>',
           f'<circle cx="50" cy="{TOPY}" r="{8.5 * S + 3.2:.2f}" fill="{WHITE}"/>',
           f'<polygon points="{poly}" fill="none" stroke="{WHITE}" stroke-width="{4.2 * S:.2f}" stroke-linejoin="round"/>']
    for i, (x, y) in enumerate(p):
        r, c = (8.5, HONEY) if i == QUEEN else ((7, WHITE) if i in (1, 5) else (4.5, WHITE))
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r * S:.2f}" fill="{c}"/>')
    out.append(f'<rect x="27" y="{BAND_Y:.2f}" width="46" height="6.5" rx="3.25" fill="{SLATE}"/>')
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">' + "".join(out) + "</svg>\n"


if __name__ == "__main__":
    Path(__file__).with_name("queenright-logo.svg").write_text(build(), encoding="utf-8")
