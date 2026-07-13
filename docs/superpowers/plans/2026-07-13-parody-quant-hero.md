# Parody Quant Hero Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current generic terminal banner with a high-contrast, original sci-fi parody hero that is legible and memorable on both GitHub themes.

**Architecture:** Keep SVG generation deterministic and repository-owned. The generator produces a matched `parody-dark.svg` and `parody-light.svg`, each with the same scene geometry but palette-aware outer framing. A small verifier enforces canvas, README wiring, no-script, text-legibility, and original-character constraints; static and delayed browser renders provide visual regression evidence.

**Tech Stack:** Python 3 standard library, SVG + SMIL, `xmllint`, `rsvg-convert`, headless Chrome, Markdown, GitHub `picture` theme switching.

---

## File Structure

- Modify: `scripts/generate_profile_hero.py` — generates the two original parody scene SVGs.
- Create: `scripts/verify_profile_hero.py` — structural checks for generated banner assets and README integration.
- Create: `assets/profile-hero/parody-dark.svg` — dark GitHub scene.
- Create: `assets/profile-hero/parody-light.svg` — light GitHub scene with the same dark interior signature card.
- Modify: `README.md` — switches `picture` sources to the new canonical assets.
- Delete: `assets/profile-hero/dark.svg` and `assets/profile-hero/light.svg` — retired terminal design after visual verification.

### Task 1: Add a failing structural verifier

**Files:**
- Create: `scripts/verify_profile_hero.py`
- Test: `scripts/verify_profile_hero.py`

- [ ] **Step 1: Write the verification program before the new assets exist**

```python
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "profile-hero"
TARGETS = (ASSETS / "parody-dark.svg", ASSETS / "parody-light.svg")

for path in TARGETS:
    text = path.read_text(encoding="utf-8")
    root = ET.fromstring(text)
    assert root.attrib["viewBox"] == "0 0 1180 610"
    assert "<script" not in text and "javascript:" not in text
    assert "Nuthdanai Wangpratham" in text
    assert "QUANT RESEARCHER" in text
    assert "AI AGENT BUILDER" in text
    assert text.count("<animate") >= 16
    assert "portal" in text.lower()
    assert "rick" not in text.lower() and "morty" not in text.lower()

readme = (ROOT / "README.md").read_text(encoding="utf-8")
assert "./assets/profile-hero/parody-dark.svg" in readme
assert "./assets/profile-hero/parody-light.svg" in readme
print("profile hero checks passed")
```

- [ ] **Step 2: Run the verifier and confirm the expected initial failure**

Run: `python3 scripts/verify_profile_hero.py`

Expected: `FileNotFoundError` for `assets/profile-hero/parody-dark.svg`.

- [ ] **Step 3: Commit the executable check**

```bash
git add scripts/verify_profile_hero.py
git commit -m "Add profile hero verification"
```

### Task 2: Generate the original parody scene pair

**Files:**
- Modify: `scripts/generate_profile_hero.py`
- Create: `assets/profile-hero/parody-dark.svg`
- Create: `assets/profile-hero/parody-light.svg`
- Test: `scripts/verify_profile_hero.py`

- [ ] **Step 1: Replace the old scene model with a named, original scene model**

```python
SCENE = {
    "name": "Nuthdanai Wangpratham",
    "role_left": "QUANT RESEARCHER",
    "role_right": "AI AGENT BUILDER",
    "proof_points": ("PAPERS → ALPHAS", "AGENTS → WORKFLOWS", "RESEARCH → DECISIONS"),
    "footer": "BANGKOK · QUANTSERAS · @NUTDNUY",
}

THEMES = {
    "dark": {"outer": "#0E1715", "canvas": "#121212", "surface": "#1D1D1D"},
    "light": {"outer": "#EAF4F0", "canvas": "#121212", "surface": "#1D1D1D"},
}
```

- [ ] **Step 2: Implement only original character geometry**

Implement `scientist_group()` and `analyst_group()` as SVG primitives, using the following identity markers and no franchise names or copied dialogue:

```python
def scientist_group() -> str:
    return '''<g id="quant-scientist">
      <path id="cyan-hair" d="M132 300 L170 218 L198 270 L232 190 L252 275 L310 220 L280 322 Z" fill="#81D4FA"/>
      <path id="lab-coat" d="M144 350 L196 328 L258 328 L312 350 L336 480 H120 Z" fill="#E8F0EF"/>
      <rect id="alpha-tablet" x="242" y="310" width="150" height="95" rx="10"/>
      <text x="262" y="355">rank(ts_delta(signal, 5))</text>
    </g>'''

def analyst_group() -> str:
    return '''<g id="junior-analyst">
      <circle id="analyst-head" cx="470" cy="330" r="54" fill="#F6C9A6"/>
      <circle id="left-eye" cx="452" cy="321" r="15" fill="#FFFFFF"/>
      <circle id="right-eye" cx="488" cy="321" r="15" fill="#FFFFFF"/>
      <path id="research-sheet" d="M504 365 H570 V455 H504 Z" fill="#F8FAFC"/>
    </g>'''
```

Use complete path coordinates when implementing; the geometry must fit inside the left `x=42..676` scene region and cannot overlap the identity card.

- [ ] **Step 3: Implement portal and quant data texture behind the characters**

```xml
<g id="portal">
  <ellipse cx="332" cy="299" rx="252" ry="238" fill="none" stroke="url(#portalGradient)" stroke-width="18"/>
  <ellipse cx="332" cy="299" rx="226" ry="212" fill="none" stroke="#03DAC6" stroke-opacity=".44" stroke-width="4"/>
  <animateTransform attributeName="transform" type="rotate" from="0 332 299" to="360 332 299" dur="28s" repeatCount="indefinite"/>
</g>
```

Use sparse candlesticks, formula fragments, and one rising line inside the portal. Keep them behind both characters.

- [ ] **Step 4: Build the right identity card at readable scale**

```xml
<text x="720" y="175" font-size="47" font-weight="800">Nuthdanai</text>
<text x="720" y="226" font-size="47" font-weight="800">Wangpratham</text>
<text x="720" y="278" font-size="19" font-weight="700">QUANT RESEARCHER</text>
<text x="720" y="306" font-size="19" font-weight="700">· AI AGENT BUILDER</text>
```

Place proof points at `y=376`, `420`, and `464`; footer at `y=524`. Animation is enhancement only; every text node is complete and visible in static rendering.

- [ ] **Step 5: Generate both assets and run the verifier**

Run: `python3 scripts/generate_profile_hero.py && python3 scripts/verify_profile_hero.py`

Expected: `profile hero checks passed`.

- [ ] **Step 6: Commit scene assets and generator**

```bash
git add scripts/generate_profile_hero.py assets/profile-hero/parody-dark.svg assets/profile-hero/parody-light.svg
git commit -m "Add parody quant profile hero"
```

### Task 3: Wire the canonical hero into the README

**Files:**
- Modify: `README.md:3-7`
- Delete: `assets/profile-hero/dark.svg`
- Delete: `assets/profile-hero/light.svg`
- Test: `scripts/verify_profile_hero.py`

- [ ] **Step 1: Replace only the image sources in the existing `picture` block**

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile-hero/parody-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/profile-hero/parody-light.svg">
  <img alt="Nuthdanai Wangpratham — Quant researcher and AI agent builder" src="./assets/profile-hero/parody-light.svg" width="100%">
</picture>
```

- [ ] **Step 2: Remove retired assets only after README points to the new pair**

Run: `rm assets/profile-hero/dark.svg assets/profile-hero/light.svg`

- [ ] **Step 3: Regenerate, validate, and commit**

Run: `python3 scripts/generate_profile_hero.py && python3 scripts/verify_profile_hero.py && xmllint --noout assets/profile-hero/parody-dark.svg assets/profile-hero/parody-light.svg && git diff --check`

Expected: verifier prints `profile hero checks passed`; `xmllint` and `git diff --check` produce no errors.

```bash
git add README.md assets/profile-hero scripts/generate_profile_hero.py scripts/verify_profile_hero.py
git commit -m "Use parody quant profile hero"
```

### Task 4: Perform visual and remote-profile verification

**Files:**
- Test: `assets/profile-hero/parody-dark.svg`
- Test: `assets/profile-hero/parody-light.svg`
- Test: `README.md`

- [ ] **Step 1: Render static fallbacks**

Run: `mkdir -p ../preview && rsvg-convert -w 1180 -h 610 assets/profile-hero/parody-dark.svg -o ../preview/parody-dark-static.png && rsvg-convert -w 1180 -h 610 assets/profile-hero/parody-light.svg -o ../preview/parody-light-static.png`

Expected: two `1180 × 610` PNGs with a complete readable scene and no animation-dependent text.

- [ ] **Step 2: Render delayed animation state in Chrome**

Run: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1180,610 --virtual-time-budget=5000 --screenshot=../preview/parody-dark-motion.png "file://$PWD/assets/profile-hero/parody-dark.svg"`

Expected: portal, particles, and character micro-animation are visible; name and role remain fully readable.

- [ ] **Step 3: Inspect all three renders manually**

Check that the portal is unmistakable, the two original characters dominate the left scene, the identity card does not look like a dashboard, and the light variant has a dark interior rather than a washed-out card.

- [ ] **Step 4: Publish, merge, and verify the live GitHub profile**

Create a branch `agent/parody-quant-hero`, push it, create PR, merge after checks pass, then run:

```bash
gh pr view --json state,mergedAt,mergeCommit,url
curl -fsSL https://raw.githubusercontent.com/nutdnuy/nutdnuy/main/README.md | rg 'parody-(dark|light)\.svg'
```

Expected: PR state is `MERGED`; the remote README references both canonical parody assets.

## Plan Self-Review

- Spec coverage: Tasks 2–3 cover the original two-character parody, portal, dark QuantSeras card, exact identity copy, light/dark assets, and retirement of the prior layout. Task 4 covers static, animated, and live rendering.
- Placeholder scan: no incomplete instructions or deferred implementation language remains.
- Consistency: the generator owns `parody-dark.svg` and `parody-light.svg`; README and verifier both reference the same asset names.
