#!/usr/bin/env python3
"""Bake title cards over the Image Generator scene for GitHub profile use."""

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "profile-hero"
SOURCE = "alpha-lab-cinematic-v1.png"

THEMES = {
    "dark": {"outer": "#0B1512", "rim": "#264F43", "tag": "#69F0AE"},
    "light": {"outer": "#EAF7F1", "rim": "#A5D8C3", "tag": "#00C853"},
}


def svg(theme: dict[str, str]) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610">
  <defs>
    <linearGradient id="rightScrim" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#07100E" stop-opacity=".05"/>
      <stop offset=".18" stop-color="#07100E" stop-opacity=".72"/>
      <stop offset="1" stop-color="#07100E" stop-opacity=".95"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity=".42"/></filter>
  </defs>
  <rect width="1180" height="610" rx="34" fill="{theme['outer']}"/>
  <rect x="10" y="10" width="1160" height="590" rx="28" fill="#101614" stroke="{theme['rim']}" stroke-width="2"/>
  <clipPath id="frame"><rect x="27" y="27" width="1126" height="556" rx="23"/></clipPath>
  <g clip-path="url(#frame)">
    <image href="{SOURCE}" x="0" y="0" width="1180" height="610" preserveAspectRatio="none"/>
    <rect x="615" y="27" width="538" height="556" fill="url(#rightScrim)"/>
  </g>
  <g filter="url(#shadow)" font-family="Avenir Next, SF Pro Display, Helvetica Neue, sans-serif">
    <rect x="692" y="69" width="397" height="470" rx="24" fill="#111A17" fill-opacity=".84" stroke="#FFFFFF" stroke-opacity=".11"/>
    <rect x="721" y="101" width="164" height="28" rx="14" fill="#69F0AE" fill-opacity=".13" stroke="#69F0AE" stroke-opacity=".7"/>
    <text x="739" y="120" fill="#69F0AE" font-size="10" font-weight="800" letter-spacing="1.8">ALPHA LAB / 2026</text>
    <text x="720" y="190" fill="#F8FAFC" font-size="39" font-weight="800" letter-spacing="-.7">Nuthdanai</text>
    <text x="720" y="234" fill="#F8FAFC" font-size="39" font-weight="800" letter-spacing="-.7">Wangpratham</text>
    <path d="M720 259 H1058" stroke="#FFFFFF" stroke-opacity=".15"/>
    <text x="720" y="300" fill="#69F0AE" font-size="16" font-weight="800" letter-spacing="1.1">QUANT RESEARCHER</text>
    <text x="720" y="327" fill="#03DAC6" font-size="16" font-weight="800" letter-spacing="1.1">· AI AGENT BUILDER</text>
    <path d="M720 353 H1058" stroke="#03DAC6" stroke-opacity=".72"/>
    <text x="720" y="400" fill="#F8FAFC" font-size="13" font-weight="750" letter-spacing=".8">PAPERS → ALPHAS</text>
    <text x="720" y="433" fill="#F8FAFC" font-size="13" font-weight="750" letter-spacing=".8">AGENTS → WORKFLOWS</text>
    <text x="720" y="466" fill="#F8FAFC" font-size="13" font-weight="750" letter-spacing=".8">RESEARCH → DECISIONS</text>
    <circle cx="726" cy="501" r="5" fill="#00E676"/>
    <text x="742" y="505" fill="#B0BEC5" font-size="10" font-weight="700" letter-spacing="1.1">BANGKOK · QUANTSERAS · @NUTDNUY</text>
  </g>
</svg>'''


def main() -> None:
    if not (ASSETS / SOURCE).exists():
        raise FileNotFoundError(ASSETS / SOURCE)
    for name, theme in THEMES.items():
        source = ASSETS / f"cinematic-{name}.svg"
        output = ASSETS / f"cinematic-{name}.png"
        source.write_text(svg(theme), encoding="utf-8")
        subprocess.run(
            ["rsvg-convert", "-w", "1180", "-h", "610", str(source), "-o", str(output)],
            check=True,
        )
        source.unlink()


if __name__ == "__main__":
    main()
