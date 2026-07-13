#!/usr/bin/env python3
"""Generate matching dark and light animated GitHub profile hero SVGs."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-hero"


THEMES = {
    "dark": {
        "bg": "#030712",
        "panel": "#0F172A",
        "panel_alt": "#111B31",
        "text": "#F8FAFC",
        "muted": "#94A3B8",
        "hairline": "#FFFFFF",
        "hairline_opacity": ".09",
        "accent_a": "#7C3AED",
        "accent_b": "#22D3EE",
        "accent_c": "#10B981",
        "shadow": "#020617",
        "glow_opacity": ".26",
        "noise_opacity": ".045",
        "reflection_opacity": ".11",
    },
    "light": {
        "bg": "#FFFFFF",
        "panel": "#F8FAFC",
        "panel_alt": "#F1F5F9",
        "text": "#0F172A",
        "muted": "#475569",
        "hairline": "#0F172A",
        "hairline_opacity": ".08",
        "accent_a": "#2563EB",
        "accent_b": "#06B6D4",
        "accent_c": "#10B981",
        "shadow": "#64748B",
        "glow_opacity": ".13",
        "noise_opacity": ".025",
        "reflection_opacity": ".32",
    },
}


ASCII_LINES = [
    "              .+*##*+.",
    "          .=#%%%%%%%%#=.",
    "        .+%%%#*++++*#%%%=",
    "       -%%%*.        .*%%#-",
    "      +%%#:   .::::.   -%%#+",
    "     -%%%-  .+#%%%%#+.  =%%%-",
    "     #%%*   *%%+::+%%*   #%%#",
    "    .%%%=   %%#.  .#%%   =%%%.",
    "     #%%*   +%%*..*%%+   *%%#",
    "     =%%%-   =#%%%%#=   -%%%+",
    "      +%%#-   .+##+.   -#%%+",
    "       *%%%*:  ____  :*%%%*",
    "        =%%%%#=----=#%%%%=",
    "          +#%%%%%%%%%%#+",
    "        .---=+*####*+=---.",
    "     .-==.   N U T D N U Y  ==-.",
]


SKILLS = [
    ("Python", 704, 403, 84),
    ("AI Agents", 797, 403, 103),
    ("Quant", 910, 403, 76),
    ("Research", 996, 403, 91),
    ("Git", 704, 441, 60),
    ("Docker", 774, 441, 78),
    ("APIs", 862, 441, 64),
    ("Data", 936, 441, 66),
    ("Portfolio", 1012, 441, 86),
]


def details_rows(c):
    rows = [
        ("LOC", "Bangkok, Thailand"),
        ("EDU", "Quant Finance + Applied AI"),
        ("NOW", "Agentic investment research"),
        ("WEB", "quantseras.com/blog"),
        ("MAIL", "Connect via LinkedIn"),
    ]
    out = []
    for i, (key, value) in enumerate(rows):
        y = 242 + i * 31
        delay = .9 + i * .22
        begin = delay - 3.0
        out.append(
            f'''<g opacity="1">
  <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.08;0.14;0.88;1" dur="12s" begin="{begin:.2f}s" repeatCount="indefinite"/>
  <animateTransform attributeName="transform" type="translate" values="12 0;12 0;0 0;0 0;0 -2" keyTimes="0;0.08;0.14;0.88;1" dur="12s" begin="{begin:.2f}s" repeatCount="indefinite"/>
  <text x="704" y="{y}" fill="{c['accent_b']}" font-size="10" font-weight="700" letter-spacing="1.4">{key}</text>
  <text x="758" y="{y}" fill="{c['muted']}" font-size="13">{value}</text>
</g>'''
        )
    return "\n".join(out)


def skill_pills(c):
    out = []
    for i, (label, x, y, width) in enumerate(SKILLS):
        delay = i * .24
        begin = delay - 2.5
        out.append(
            f'''<g opacity="1">
  <animate attributeName="opacity" values="0;1;1;.78;1" keyTimes="0;.15;.62;.80;1" dur="5.6s" begin="{begin:.2f}s" repeatCount="indefinite"/>
  <rect x="{x}" y="{y}" width="{width}" height="28" rx="14" fill="url(#pillFill)" stroke="url(#accent)" stroke-opacity=".42" filter="url(#pillGlow)"/>
  <circle cx="{x + 14}" cy="{y + 14}" r="3" fill="{c['accent_c']}"><animate attributeName="opacity" values=".45;1;.45" dur="2.4s" begin="{delay:.2f}s" repeatCount="indefinite"/></circle>
  <text x="{x + 24}" y="{y + 18}" fill="{c['text']}" font-size="10.5" font-weight="600" letter-spacing=".2">{label}</text>
</g>'''
        )
    return "\n".join(out)


def typing_phrases(c):
    phrases = [
        ("Quant Research Engineer", 290),
        ("AI Agent Builder", 205),
        ("Investment Researcher", 260),
        ("Open Source Contributor", 282),
        ("Financial Educator", 220),
    ]
    out = []
    for i, (phrase, width) in enumerate(phrases):
        start = max(.001, i * .2)
        reveal = start + .026
        hold = start + .168
        fade = start + .195
        base_opacity = "1" if i == 0 else "0"
        out.append(
            f'''<g opacity="{base_opacity}" clip-path="url(#typeClip{i})">
  <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;{start:.3f};{hold:.3f};{fade:.3f};1" dur="15s" repeatCount="indefinite"/>
  <text x="704" y="207" fill="url(#accent)" font-size="20" font-weight="650" letter-spacing=".2">{phrase}</text>
  <rect x="{704 + width}" y="190" width="8" height="20" rx="1" fill="{c['accent_b']}">
    <animate attributeName="x" values="704;704;{704 + width};{704 + width};704" keyTimes="0;{start:.3f};{reveal:.3f};{fade:.3f};1" dur="15s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0;1;0;1" dur=".78s" repeatCount="indefinite"/>
  </rect>
</g>
<clipPath id="typeClip{i}"><rect x="704" y="185" width="{width + 12}" height="28"><animate attributeName="width" values="0;0;{width + 12};{width + 12};0" keyTimes="0;{start:.3f};{reveal:.3f};{fade:.3f};1" dur="15s" repeatCount="indefinite"/></rect></clipPath>'''
        )
    return "\n".join(out)


def ascii_rows(c):
    out = []
    for i, line in enumerate(ASCII_LINES):
        y = 125 + i * 23
        delay = .35 + i * .11
        begin = delay - 2.5
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        out.append(
            f'''<g clip-path="url(#asciiClip{i})" opacity="1">
  <animate attributeName="opacity" from="0" to="1" dur=".5s" begin="{begin:.2f}s" fill="freeze"/>
  <text x="82" y="{y}" fill="url(#asciiGradient)" font-size="15.5" font-weight="700" letter-spacing=".25" filter="url(#asciiGlow)">{safe}</text>
</g>
<clipPath id="asciiClip{i}"><rect x="75" y="{y - 18}" width="390" height="23"><animate attributeName="width" from="0" to="390" dur=".85s" begin="{begin:.2f}s" fill="freeze"/></rect></clipPath>'''
        )
    return "\n".join(out)


def render(theme, c):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="title desc">
<title id="title">Nuthdanai Wangpratham — Quant finance and AI agent builder</title>
<desc id="desc">Animated terminal-style GitHub profile banner with an ASCII portrait, professional details, skills, and social links.</desc>
<defs>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{c['accent_a']}"><animate attributeName="stop-color" values="{c['accent_a']};{c['accent_b']};{c['accent_a']}" dur="8s" repeatCount="indefinite"/></stop>
    <stop offset=".52" stop-color="{c['accent_b']}"><animate attributeName="stop-color" values="{c['accent_b']};{c['accent_c']};{c['accent_b']}" dur="8s" repeatCount="indefinite"/></stop>
    <stop offset="1" stop-color="{c['accent_c']}"><animate attributeName="stop-color" values="{c['accent_c']};{c['accent_a']};{c['accent_c']}" dur="8s" repeatCount="indefinite"/></stop>
    <animate attributeName="x1" values="0;1;0" dur="10s" repeatCount="indefinite"/><animate attributeName="x2" values="1;0;1" dur="10s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="asciiGradient" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c['accent_b']}"/><stop offset=".5" stop-color="{c['accent_a']}"/><stop offset="1" stop-color="{c['accent_c']}"/><animate attributeName="x1" values="-.4;.8;-.4" dur="7s" repeatCount="indefinite"/><animate attributeName="x2" values=".6;1.8;.6" dur="7s" repeatCount="indefinite"/></linearGradient>
  <linearGradient id="border" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c['hairline']}" stop-opacity=".04"/><stop offset=".45" stop-color="{c['accent_b']}" stop-opacity=".75"/><stop offset=".55" stop-color="{c['accent_a']}" stop-opacity=".75"/><stop offset="1" stop-color="{c['hairline']}" stop-opacity=".04"/><animate attributeName="x1" values="-1;1" dur="5s" repeatCount="indefinite"/><animate attributeName="x2" values="0;2" dur="5s" repeatCount="indefinite"/></linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c['hairline']}" stop-opacity="{c['reflection_opacity']}"/><stop offset=".38" stop-color="{c['panel']}" stop-opacity=".7"/><stop offset="1" stop-color="{c['panel_alt']}" stop-opacity=".92"/></linearGradient>
  <linearGradient id="pillFill" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c['accent_a']}" stop-opacity=".12"/><stop offset="1" stop-color="{c['accent_b']}" stop-opacity=".06"/></linearGradient>
  <radialGradient id="orbA"><stop stop-color="{c['accent_a']}" stop-opacity="{c['glow_opacity']}"/><stop offset="1" stop-color="{c['accent_a']}" stop-opacity="0"/></radialGradient>
  <radialGradient id="orbB"><stop stop-color="{c['accent_b']}" stop-opacity="{c['glow_opacity']}"/><stop offset="1" stop-color="{c['accent_b']}" stop-opacity="0"/></radialGradient>
  <radialGradient id="orbC"><stop stop-color="{c['accent_c']}" stop-opacity="{c['glow_opacity']}"/><stop offset="1" stop-color="{c['accent_c']}" stop-opacity="0"/></radialGradient>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="22" stdDeviation="24" flood-color="{c['shadow']}" flood-opacity=".34"/></filter>
  <filter id="asciiGlow" x="-30%" y="-50%" width="160%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="pillGlow" x="-30%" y="-70%" width="160%" height="240%"><feGaussianBlur in="SourceGraphic" stdDeviation=".7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="noise"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" seed="17"><animate attributeName="seed" values="17;31;17" dur="10s" repeatCount="indefinite"/></feTurbulence><feColorMatrix type="saturate" values="0"/></filter>
  <clipPath id="frameClip"><rect x="10" y="10" width="1160" height="590" rx="30"/></clipPath>
</defs>

<g font-family="Geist Mono, SFMono-Regular, Cascadia Code, Segoe UI Mono, monospace">
  <rect x="10" y="10" width="1160" height="590" rx="30" fill="{c['bg']}"/>
  <g clip-path="url(#frameClip)">
    <circle cx="150" cy="120" r="280" fill="url(#orbA)"><animate attributeName="cx" values="100;220;100" dur="13s" repeatCount="indefinite"/><animate attributeName="cy" values="90;155;90" dur="11s" repeatCount="indefinite"/></circle>
    <circle cx="1020" cy="130" r="300" fill="url(#orbB)"><animate attributeName="cx" values="1060;930;1060" dur="16s" repeatCount="indefinite"/></circle>
    <circle cx="690" cy="570" r="280" fill="url(#orbC)"><animate attributeName="cy" values="600;515;600" dur="14s" repeatCount="indefinite"/></circle>
    <rect x="10" y="10" width="1160" height="590" filter="url(#noise)" opacity="{c['noise_opacity']}"/>
    <g fill="{c['accent_b']}">
      <circle cx="52" cy="84" r="1.5"><animateMotion dur="9s" repeatCount="indefinite" path="M0 0 C 50 -20, 90 40, 150 0"/><animate attributeName="opacity" values="0;.8;0" dur="9s" repeatCount="indefinite"/></circle>
      <circle cx="900" cy="535" r="1"><animateMotion dur="12s" repeatCount="indefinite" path="M0 0 C -80 -40, -30 -120, 50 -160"/><animate attributeName="opacity" values="0;.6;0" dur="12s" repeatCount="indefinite"/></circle>
      <circle cx="560" cy="72" r="1.2"><animateMotion dur="10s" repeatCount="indefinite" path="M0 0 C 40 60, -20 120, 35 180"/><animate attributeName="opacity" values=".1;.7;.1" dur="10s" repeatCount="indefinite"/></circle>
    </g>
    <rect x="0" y="-80" width="1180" height="90" fill="url(#accent)" opacity=".035"><animate attributeName="y" values="-90;620" dur="7s" repeatCount="indefinite"/></rect>
  </g>

  <rect x="11" y="11" width="1158" height="588" rx="29" fill="none" stroke="url(#border)" stroke-width="1.5"/>
  <g filter="url(#shadow)">
    <rect x="44" y="48" width="444" height="514" rx="25" fill="url(#glass)" stroke="{c['hairline']}" stroke-opacity="{c['hairline_opacity']}"/>
    <rect x="506" y="48" width="630" height="514" rx="25" fill="url(#glass)" stroke="{c['hairline']}" stroke-opacity="{c['hairline_opacity']}"/>
  </g>
  <path d="M64 50 H462 Q484 50 486 72 V114 C350 76 210 67 64 86Z" fill="{c['hairline']}" opacity="{c['reflection_opacity']}"/>
  <path d="M526 50 H1110 Q1134 50 1134 74 V108 C926 66 728 68 526 88Z" fill="{c['hairline']}" opacity="{c['reflection_opacity']}"/>

  <g>
    <text x="76" y="82" fill="{c['muted']}" font-size="10" letter-spacing="2">PORTRAIT.SYS / LIVE</text>
    <circle cx="450" cy="78" r="4" fill="{c['accent_c']}"><animate attributeName="opacity" values=".35;1;.35" dur="1.7s" repeatCount="indefinite"/></circle>
    <g><animateTransform attributeName="transform" type="translate" values="0 2;0 -4;0 2" dur="5.5s" repeatCount="indefinite"/>
      {ascii_rows(c)}
      <rect x="374" y="475" width="9" height="18" rx="1" fill="{c['accent_b']}"><animate attributeName="opacity" values="1;0;1" dur=".8s" repeatCount="indefinite"/></rect>
    </g>
    <rect x="64" y="103" width="404" height="2" fill="url(#accent)" opacity=".25"><animate attributeName="y" values="103;520;103" dur="5s" repeatCount="indefinite"/></rect>
    <text x="76" y="537" fill="{c['muted']}" font-size="9" letter-spacing="1.2">SIGNAL 98.4%  /  HUMAN + MACHINE</text>
  </g>

  <g>
    <circle cx="542" cy="79" r="5" fill="#FF5F57"/><circle cx="560" cy="79" r="5" fill="#FEBC2E"/><circle cx="578" cy="79" r="5" fill="#28C840"/>
    <text x="608" y="83" fill="{c['muted']}" font-size="10" letter-spacing="1.5">NUTHDANAI@RESEARCH:~</text>
    <rect x="526" y="103" width="590" height="1" fill="{c['hairline']}" opacity="{c['hairline_opacity']}"/>
    <text x="704" y="143" fill="{c['muted']}" font-size="13">Hi <tspan fill="{c['accent_b']}">👋</tspan>  I'm</text>
    <text x="704" y="178" fill="{c['text']}" font-size="27" font-weight="750" letter-spacing="-.5">Nuthdanai Wangpratham</text>
    {typing_phrases(c)}
    <text x="548" y="143" fill="{c['accent_b']}" font-size="10" letter-spacing="1.5">01</text>
    <path d="M548 154 V354" stroke="{c['hairline']}" stroke-opacity="{c['hairline_opacity']}"/>
    <text x="548" y="378" fill="{c['accent_c']}" font-size="10" letter-spacing="1.5">02</text>
    <path d="M548 389 V493" stroke="{c['hairline']}" stroke-opacity="{c['hairline_opacity']}"/>
    <text x="548" y="518" fill="{c['accent_a']}" font-size="10" letter-spacing="1.5">03</text>
    <path d="M574 139 C622 139 640 139 678 139" stroke="url(#accent)" stroke-width="1" opacity=".45"/>

    {details_rows(c)}
    <text x="704" y="388" fill="{c['text']}" font-size="11" font-weight="700" letter-spacing="1.7">TOOLKIT / SIGNAL STACK</text>
    {skill_pills(c)}

    <rect x="680" y="486" width="430" height="50" rx="16" fill="{c['panel_alt']}" fill-opacity=".74" stroke="{c['hairline']}" stroke-opacity="{c['hairline_opacity']}"/>
    <text x="704" y="506" fill="{c['muted']}" font-size="9" letter-spacing="1.6">FIND ME ONLINE</text>
    <text x="704" y="523" fill="{c['text']}" font-size="11.5" font-weight="650">GH  @nutdnuy</text>
    <circle cx="819" cy="516" r="2" fill="{c['accent_b']}"/>
    <text x="833" y="523" fill="{c['text']}" font-size="11.5" font-weight="650">in  nuthdanai-w</text>
    <circle cx="964" cy="516" r="2" fill="{c['accent_a']}"/>
    <text x="978" y="523" fill="{c['text']}" font-size="11.5" font-weight="650">YT  @NuthdanaiW</text>
  </g>
</g>
</svg>
'''


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for theme, colors in THEMES.items():
        (OUTPUT / f"{theme}.svg").write_text(render(theme, colors), encoding="utf-8")


if __name__ == "__main__":
    main()
