"""Builds queenright-social.svg, the 1200x630 link-preview banner (og:image).

Logo and name sit in the centre, so chat apps that crop previews to a
square still show both. Render the PNG with a headless browser, e.g.:
  msedge --headless --screenshot=queenright-social.png --window-size=1200,630 queenright-social.svg
"""
from pathlib import Path

from build_logo import NAVY, SLATE, build as build_logo

W, H, LOGO = 1200, 630, 220
FONT = 'system-ui, -apple-system, &quot;Segoe UI&quot;, Roboto, sans-serif'


def build():
    logo = build_logo().strip().replace(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">',
        f'<svg x="{(W - LOGO) / 2}" y="85" width="{LOGO}" height="{LOGO}" viewBox="0 0 100 100">')
    out = [f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
           logo,
           f'<text x="{W / 2}" y="355" text-anchor="middle" font-family="{FONT}" font-size="76" '
           f'font-weight="700" fill="#FFFFFF">Queenright</text>',
           f'<text x="{W / 2}" y="415" text-anchor="middle" font-family="{FONT}" font-size="32" '
           f'fill="#D5DBE8">Stable concepts for human–agent collaboration</text>',
           f'<text x="{W / 2}" y="525" text-anchor="middle" font-family="{FONT}" font-size="24" '
           f'letter-spacing="2" fill="{SLATE}">queenright.org</text>']
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">' + "".join(out) + "</svg>\n")


if __name__ == "__main__":
    Path(__file__).with_name("queenright-social.svg").write_text(build(), encoding="utf-8")
