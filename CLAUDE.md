# Little Explorers prototype

Hackathon concept prototype for "Cathay Little Explorers" (junior membership mode).
Synthetic data only. Never imply a real Cathay integration. No official logos.

## Design
@shared/DESIGN.md

All visual work follows shared/DESIGN.md. If it conflicts with an older
rule here, DESIGN.md wins.

## Stack
- Plain HTML + CSS + vanilla JS. No frameworks, no build step, no npm.
- Every page links shared/fonts.css and shared/tokens.css and loads
  shared/data.js via <script>.
- All text and numbers come from window.DATA. Never hard-code copy.
- Self-hosted fonts in shared/fonts/ are allowed. Illustrations are inline
  SVG. No CDNs or external images.

## Layout
- Must also work on a real phone browser.
- Prototype screens switch via location.hash (#home, #story, #mission).
  Handle both DOMContentLoaded and hashchange.

## Ownership
- prototype/, shared/, CLAUDE.md = Builder A.
- overlays/, tools/, .claude/skills/ = Builder B. Never edit these.

## Working rules
- Before calling anything done: run `python prototype/dev/shoot.py`
  (or /screen-check once it exists), look at every screenshot, and answer
  the 5-question self-check at the end of DESIGN.md.
- Small changes. One milestone per session.
- Missions are trip-linked only (check-in, boarding, arrival).
  Never add any way to earn outside a trip.
