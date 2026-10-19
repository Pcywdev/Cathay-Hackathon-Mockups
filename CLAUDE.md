# Little Explorers prototype

Hackathon concept prototype for "Cathay Little Explorers" (junior membership mode).
Synthetic data only. Never imply a real Cathay integration. No official logos.

## Stack
- Plain HTML + CSS + vanilla JS. No frameworks, no build step, no npm.
- Every page links shared/tokens.css and loads shared/data.js via <script>.
- All text and numbers come from window.DATA. Never hard-code copy.
- Illustrations: inline SVG only. No external images, fonts or CDNs.

## Layout
- Design for a 393x852 phone viewport; must also work on a real phone browser.
- Prototype screens switch via location.hash (#home, #story, #mission).
  Handle both DOMContentLoaded and hashchange.
- Every prototype screen shows DATA.labels.concept in small text.

## Ownership
- prototype/, shared/, CLAUDE.md = Builder A.
- overlays/, tools/, .claude/skills/ = Builder B. Never edit these.

## Working rules
- Before saying a task is done, run `python prototype/dev/shoot.py`
  (or /screen-check once it exists) and look at every screenshot.
- Small changes. One milestone per session.
- Missions are trip-linked only (check-in, boarding, arrival).
  Never add any way to earn outside a trip.
