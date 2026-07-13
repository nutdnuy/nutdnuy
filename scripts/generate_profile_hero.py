#!/usr/bin/env python3
"""Generate two original animated sci-fi parody heroes for the profile README."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-hero"

SCENE = {
    "name": "Nuthdanai Wangpratham",
    "role_left": "QUANT RESEARCHER",
    "role_right": "AI AGENT BUILDER",
    "proof_points": ("PAPERS → ALPHAS", "AGENTS → WORKFLOWS", "RESEARCH → DECISIONS"),
    "footer": "BANGKOK · QUANTSERAS · @NUTDNUY",
}

THEMES = {
    "dark": {
        "outer": "#0C1513",
        "rim": "#1C2C28",
        "canvas": "#121212",
        "surface": "#1D1D1D",
        "surface_2": "#242424",
        "ink": "#F5F7F6",
        "muted": "#AAB8B3",
        "line": "#FFFFFF",
        "portal_a": "#69F0AE",
        "portal_b": "#03DAC6",
        "signal": "#00E676",
        "orange": "#FFB74D",
        "glow": ".34",
    },
    "light": {
        "outer": "#E9F5F0",
        "rim": "#B7D8CC",
        "canvas": "#121212",
        "surface": "#1D1D1D",
        "surface_2": "#242424",
        "ink": "#F5F7F6",
        "muted": "#AAB8B3",
        "line": "#FFFFFF",
        "portal_a": "#69F0AE",
        "portal_b": "#03DAC6",
        "signal": "#00E676",
        "orange": "#FFB74D",
        "glow": ".40",
    },
}


def particles(c: dict[str, str]) -> str:
    dots = [
        (126, 156, 3, "M0 0 C 76 -72, 188 24, 300 18", 8),
        (168, 476, 2, "M0 0 C 80 -74, 196 -40, 286 -134", 10),
        (452, 170, 2, "M0 0 C -68 76, 38 152, -50 274", 9),
        (528, 468, 3, "M0 0 C -92 -40, -78 -172, -212 -238", 11),
        (312, 108, 2, "M0 0 C 90 44, 10 112, 144 184", 7),
        (604, 274, 2, "M0 0 C -86 54, -174 8, -276 90", 12),
    ]
    result = []
    for i, (x, y, radius, path, duration) in enumerate(dots):
        color = c["portal_a"] if i % 2 == 0 else c["portal_b"]
        result.append(
            f'''<circle cx="{x}" cy="{y}" r="{radius}" fill="{color}" filter="url(#softGlow)">
  <animate attributeName="opacity" values="0;.9;.25;0" dur="{duration}s" begin="-{i + 1}s" repeatCount="indefinite"/>
  <animateMotion dur="{duration}s" begin="-{i + 1}s" repeatCount="indefinite" path="{path}"/>
</circle>'''
        )
    return "\n".join(result)


def proof_cards(c: dict[str, str]) -> str:
    rows = []
    for i, label in enumerate(SCENE["proof_points"]):
        y = 366 + i * 48
        accent = c["portal_a"] if i != 1 else c["portal_b"]
        rows.append(
            f'''<g>
  <rect x="722" y="{y}" width="390" height="34" rx="10" fill="{c['surface_2']}" stroke="{c['line']}" stroke-opacity=".08"/>
  <rect x="722" y="{y}" width="5" height="34" rx="2.5" fill="{accent}">
    <animate attributeName="height" values="34;20;34" dur="2.8s" begin="-{i}s" repeatCount="indefinite"/>
  </rect>
  <text x="742" y="{y + 22}" fill="{c['ink']}" font-size="13" font-weight="700" letter-spacing=".7">{label}</text>
</g>'''
        )
    return "\n".join(rows)


def render(theme: str, c: dict[str, str]) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610" role="img" aria-labelledby="title desc">
<title id="title">{SCENE['name']} — Quant researcher and AI agent builder</title>
<desc id="desc">An original animated sci-fi parody scene: a quant scientist and junior analyst emerge from a luminous research portal.</desc>
<defs>
  <linearGradient id="portalGradient" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{c['portal_a']}"/>
    <stop offset=".55" stop-color="{c['portal_b']}"/>
    <stop offset="1" stop-color="{c['signal']}"/>
    <animate attributeName="x1" values="0;1;0" dur="9s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="1;0;1" dur="9s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="cardGradient" x1="0" y1="0" x2="1" y2="1">
    <stop stop-color="{c['surface_2']}"/><stop offset="1" stop-color="{c['canvas']}"/>
  </linearGradient>
  <radialGradient id="portalCore"><stop stop-color="{c['portal_a']}" stop-opacity=".34"/><stop offset=".55" stop-color="{c['portal_b']}" stop-opacity=".11"/><stop offset="1" stop-color="{c['canvas']}" stop-opacity="0"/></radialGradient>
  <filter id="softGlow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="portalGlow" x="-45%" y="-45%" width="190%" height="190%"><feGaussianBlur stdDeviation="14" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <clipPath id="sceneClip"><rect x="42" y="42" width="634" height="526" rx="28"/></clipPath>
</defs>
<g font-family="Geist, Avenir Next, SF Pro Display, Segoe UI, sans-serif">
  <rect x="10" y="10" width="1160" height="590" rx="34" fill="{c['outer']}"/>
  <rect x="11" y="11" width="1158" height="588" rx="33" fill="none" stroke="{c['rim']}" stroke-width="2"/>
  <rect x="27" y="27" width="1126" height="556" rx="28" fill="{c['canvas']}"/>

  <g clip-path="url(#sceneClip)">
    <rect x="42" y="42" width="634" height="526" rx="28" fill="#161C1A"/>
    <circle cx="324" cy="309" r="260" fill="url(#portalCore)" opacity="{c['glow']}"/>
    <g id="portal" filter="url(#portalGlow)">
      <ellipse cx="326" cy="304" rx="232" ry="222" fill="none" stroke="url(#portalGradient)" stroke-width="18" opacity=".84">
        <animateTransform attributeName="transform" type="rotate" from="0 326 304" to="360 326 304" dur="30s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="326" cy="304" rx="207" ry="197" fill="none" stroke="{c['portal_b']}" stroke-width="3" stroke-opacity=".72" stroke-dasharray="6 12">
        <animateTransform attributeName="transform" type="rotate" from="360 326 304" to="0 326 304" dur="20s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="326" cy="304" rx="184" ry="176" fill="none" stroke="{c['portal_a']}" stroke-width="2" stroke-opacity=".42" stroke-dasharray="3 13">
        <animateTransform attributeName="transform" type="rotate" from="0 326 304" to="360 326 304" dur="16s" repeatCount="indefinite"/>
      </ellipse>
    </g>
    <g opacity=".42" stroke="{c['portal_b']}" stroke-width="2" fill="none">
      <path d="M95 440 L148 402 L192 421 L244 350 L290 382 L338 286 L389 318 L448 207 L510 254"/>
      <path d="M100 462 H574" stroke-opacity=".32"/>
      <path d="M100 386 H574" stroke-opacity=".18"/>
      <path d="M100 310 H574" stroke-opacity=".18"/>
    </g>
    <g fill="{c['signal']}" opacity=".62">
      <rect x="130" y="392" width="8" height="42" rx="3"/><rect x="164" y="368" width="8" height="64" rx="3"/>
      <rect x="198" y="396" width="8" height="31" rx="3"/><rect x="232" y="336" width="8" height="90" rx="3"/>
      <rect x="266" y="364" width="8" height="61" rx="3"/><rect x="300" y="288" width="8" height="136" rx="3"/>
    </g>
    <text x="76" y="82" fill="{c['muted']}" font-size="11" letter-spacing="2.4">THE ALPHA LAB INCIDENT</text>
    <text x="76" y="104" fill="{c['portal_a']}" font-size="10" font-weight="700" letter-spacing="1.5">EXPERIMENT 07 / SIGNAL UNSTABLE</text>
    {particles(c)}

    <g id="quant-scientist">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -5;0 0" dur="5.4s" repeatCount="indefinite"/>
      <path d="M135 290 L166 194 L202 256 L238 166 L261 257 L314 203 L290 311 L249 340 L167 335 Z" fill="#81D4FA" stroke="#0E1715" stroke-width="6" stroke-linejoin="round"/>
      <path d="M160 275 C160 220 272 214 285 278 L281 362 C268 409 178 414 160 359 Z" fill="#F3C8A6" stroke="#0E1715" stroke-width="6"/>
      <path d="M171 280 H220 V314 H171 Z M229 280 H278 V314 H229 Z" fill="#E5F8F5" fill-opacity=".82" stroke="#0E1715" stroke-width="5"/>
      <path d="M220 296 H229" stroke="#0E1715" stroke-width="5"/>
      <circle cx="198" cy="297" r="5" fill="#0E1715"/><circle cx="253" cy="297" r="5" fill="#0E1715"/>
      <path d="M192 340 Q220 362 253 338" fill="none" stroke="#0E1715" stroke-width="5" stroke-linecap="round"/>
      <path d="M150 380 Q220 342 294 380 L326 526 H116 Z" fill="#E8F0EF" stroke="#0E1715" stroke-width="6" stroke-linejoin="round"/>
      <path d="M193 375 L220 422 L247 375" fill="{c['portal_b']}" stroke="#0E1715" stroke-width="4"/>
      <rect x="127" y="402" width="165" height="94" rx="12" fill="#0F1816" stroke="{c['portal_a']}" stroke-width="5" transform="rotate(-8 127 402)"/>
      <text x="143" y="435" fill="{c['portal_a']}" font-family="SFMono-Regular, Menlo, monospace" font-size="10" transform="rotate(-8 143 435)">rank(ts_delta(</text>
      <text x="143" y="452" fill="{c['portal_b']}" font-family="SFMono-Regular, Menlo, monospace" font-size="10" transform="rotate(-8 143 452)">signal, 5))</text>
      <path d="M142 474 L173 461 L199 467 L230 438 L267 449" fill="none" stroke="{c['signal']}" stroke-width="3" transform="rotate(-8 142 474)">
        <animate attributeName="stroke-opacity" values=".25;1;.25" dur="1.8s" repeatCount="indefinite"/>
      </path>
      <circle cx="177" cy="415" r="10" fill="{c['orange']}" stroke="#0E1715" stroke-width="3"/><text x="172" y="420" fill="#0E1715" font-size="12" font-weight="800">Q</text>
    </g>

    <g id="junior-analyst">
      <animateTransform attributeName="transform" type="translate" values="0 0;2 3;0 0" dur="3.2s" repeatCount="indefinite"/>
      <path d="M430 336 C425 263 548 245 566 330 L553 391 C530 416 454 414 432 385 Z" fill="#F6C9A6" stroke="#0E1715" stroke-width="6"/>
      <path d="M428 309 Q460 235 535 263 Q571 276 571 327 L540 297 L510 318 L475 286 L448 320 Z" fill="#3B4B50" stroke="#0E1715" stroke-width="6" stroke-linejoin="round"/>
      <ellipse cx="469" cy="339" rx="18" ry="21" fill="#FFFFFF" stroke="#0E1715" stroke-width="4"/><ellipse cx="518" cy="339" rx="18" ry="21" fill="#FFFFFF" stroke="#0E1715" stroke-width="4"/>
      <circle cx="472" cy="341" r="5" fill="#0E1715"><animate attributeName="r" values="5;2;5" dur="4.8s" repeatCount="indefinite"/></circle>
      <circle cx="515" cy="341" r="5" fill="#0E1715"><animate attributeName="r" values="5;2;5" dur="4.8s" repeatCount="indefinite"/></circle>
      <path d="M478 374 Q493 365 509 374" fill="none" stroke="#0E1715" stroke-width="4" stroke-linecap="round"/>
      <path d="M415 407 Q490 375 569 411 L599 526 H396 Z" fill="#FFB74D" stroke="#0E1715" stroke-width="6"/>
      <path d="M514 391 L491 432 L467 393" fill="#F8FAFC" stroke="#0E1715" stroke-width="4"/>
      <g id="research-sheet">
        <animateTransform attributeName="transform" type="rotate" values="0 548 444;3 548 444;0 548 444" dur="1.6s" repeatCount="indefinite"/>
        <path d="M534 394 H620 V488 H534 Z" fill="#F8FAFC" stroke="#0E1715" stroke-width="5" stroke-linejoin="round"/>
        <path d="M550 419 H603 M550 436 H592 M550 453 H611" stroke="#3B4B50" stroke-width="4" stroke-linecap="round"/>
        <path d="M549 473 L565 457 L579 466 L605 438" fill="none" stroke="{c['signal']}" stroke-width="4"/>
      </g>
    </g>
    <path d="M56 535 H652" stroke="{c['line']}" stroke-opacity=".12"/>
  </g>

  <g id="identity-card">
    <rect x="698" y="42" width="440" height="526" rx="28" fill="url(#cardGradient)" stroke="{c['line']}" stroke-opacity=".10"/>
    <rect x="720" y="73" width="166" height="28" rx="14" fill="{c['portal_a']}" fill-opacity=".15" stroke="{c['portal_a']}" stroke-opacity=".55"/>
    <text x="738" y="92" fill="{c['portal_a']}" font-size="10" font-weight="800" letter-spacing="1.6">QUANT LAB / 2026</text>
    <text x="720" y="161" fill="{c['ink']}" font-size="40" font-weight="800" letter-spacing="-.8">Nuthdanai</text>
    <text x="720" y="207" fill="{c['ink']}" font-size="40" font-weight="800" letter-spacing="-.8">Wangpratham</text>
    <path d="M720 232 H1112" stroke="{c['line']}" stroke-opacity=".12"/>
    <text x="720" y="267" fill="{c['portal_a']}" font-size="18" font-weight="800" letter-spacing="1.1">QUANT RESEARCHER</text>
    <text x="720" y="295" fill="{c['portal_b']}" font-size="18" font-weight="800" letter-spacing="1.1">· AI AGENT BUILDER</text>
    <rect x="720" y="316" width="392" height="1" fill="url(#portalGradient)" opacity=".75"><animate attributeName="width" values="100;392;180;392" dur="5s" repeatCount="indefinite"/></rect>
    {proof_cards(c)}
    <rect x="720" y="503" width="392" height="42" rx="12" fill="#121212" stroke="{c['line']}" stroke-opacity=".09"/>
    <circle cx="742" cy="524" r="6" fill="{c['signal']}"><animate attributeName="opacity" values=".35;1;.35" dur="1.7s" repeatCount="indefinite"/></circle>
    <text x="758" y="528" fill="{c['muted']}" font-size="10" font-weight="700" letter-spacing="1.1">{SCENE['footer']}</text>
  </g>
</g>
</svg>
'''


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for theme, colors in THEMES.items():
        (OUTPUT / f"parody-{theme}.svg").write_text(render(theme, colors), encoding="utf-8")


if __name__ == "__main__":
    main()
