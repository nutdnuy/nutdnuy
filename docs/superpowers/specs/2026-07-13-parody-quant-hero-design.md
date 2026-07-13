# Parody Quant Hero — Design Spec

## Goal

Replace the current small, pale terminal/ASCII profile banner with a memorable
GitHub profile hero that presents Nuthdanai as a quant researcher and AI-agent
builder through an original, affectionate sci-fi cartoon parody.

## Creative Direction

**Concept:** `The Alpha Lab Incident` — a brilliant, chaotic quant scientist
and an anxious junior analyst stand in front of a portal created by a runaway
alpha-research experiment.

The characters are original designs. They may evoke the broad energy of a
dimension-hopping adult animated sci-fi comedy—spiky blue-haired mad scientist,
wide-eyed sidekick, absurd portal science—but must not copy named characters,
their exact faces, costumes, dialogue, or show artwork.

## Visual System

- Canvas: `1180 × 610`, SVG with a readable static fallback and SMIL-only
  animation.
- Both GitHub color-scheme variants retain a dark, high-contrast signature
  scene; the light variant uses a pale outer margin only, not a pale interior.
- QuantSeras palette: base `#121212`, charcoal elevation overlays, primary
  `#69F0AE`, teal `#03DAC6`, chart green `#00E676`, muted warning orange
  `#FFB74D`.
- A small orange accent may connect to the existing profile avatar but must not
  become a competing brand color.
- Main readable type: large name plus one-line role. Any supporting labels are
  secondary and must remain legible at GitHub's typical README width.

## Composition

1. **Hero characters (left 58%)**
   - Mad quant scientist: cyan spiky hair, lab coat with a `Q` patch, holding a
     terminal tablet with a glowing alpha expression.
   - Nervous junior analyst: original round-eyed design, holding an overflowing
     research sheet / laptop, visibly alarmed by the experiment.
   - Giant green-teal portal behind them supplies depth and immediate contrast.
2. **Identity card (right 42%)**
   - `Nuthdanai Wangpratham` as the largest textual element.
   - `QUANT RESEARCHER · AI AGENT BUILDER` as the only large subheading.
   - Three compact proof points: `Papers → Alphas`, `Agents → Workflows`, and
     `Research → Decisions`.
   - A low-emphasis footer: `Bangkok · QuantSeras · @nutdnuy`.
3. **Data texture, not dashboard**
   - A few background candlesticks, a rising signal line, and formula fragments
     may appear inside / behind the portal.
   - No skills pills, location/education rows, social row, or faux terminal
     chrome. The existing clickable badges below the image remain the social
     navigation.

## Animation

- Portal rings rotate slowly in opposing directions.
- Green particles and paper fragments orbit out of the portal.
- Tablet alpha line pulses; one small candlestick flips between gain/loss.
- Scientist's hair/coat gently floats; sidekick's eyes blink and research sheet
  shakes once per loop.
- The role line types once then stays visible; no text is clipped in the
  fallback or while animating.

Animations must use only SVG/SMIL primitives supported by GitHub image
rendering. The base SVG state must be attractive and complete if animation is
disabled.

## README Integration

- Replace the current `picture` hero sources with `parody-dark.svg` and
  `parody-light.svg`.
- Keep links, project descriptions, stats, and contact section unchanged.
- Retire the current `dark.svg` and `light.svg` assets after the replacement is
  visual-verified, so the repository has one canonical hero pair.

## Acceptance Checks

- GitHub dark and light profile screenshots show the scene at full contrast.
- The name and role are immediately readable at the width in the user's
  provided desktop screenshot.
- Characters read as an original parody, not a direct recreation of a specific
  copyrighted character.
- SVG XML validates; no JavaScript, external images, or unsupported content.
- Static render and delayed Chrome render both retain full, unclipped text.
- README continues to theme-switch through `picture` sources.

## Scope Boundaries

- This change does not alter the GitHub avatar, public bio, social destinations,
  or project copy.
- No stock artwork, external fonts, or third-party banner service is used.
