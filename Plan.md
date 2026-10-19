You are my build partner for a hackathon prototype. Work in small steps, verify
visually, and stop at the end of each milestone so I can review and commit.

CONTEXT
We're a university team in the Cathay Hackathon. Our concept, "Cathay Little
Explorers," adds a parent-managed junior mode to Cathay's existing membership app:
children earn small, capped amounts of Asia Miles through missions during family
trips. We are filming a 2-minute pitch video. This prototype appears for about
15 seconds, screen-recorded on a real phone. It is a concept prototype with
SYNTHETIC DATA ONLY. Never imply a real Cathay integration and never use an
official Cathay logo.

MY ROLE
I am Builder A. I own prototype/, shared/ and CLAUDE.md. My teammate owns
overlays/, tools/ and .claude/skills/. Never create or edit files in those folders.

WHAT WE'RE BUILDING (later milestones)
prototype/index.html: a single-page app with three screens switched by URL hash:
- #home: junior mode home (companion character, miles card with annual cap,
  "My trip story" card, mission list, stamp row)
- #story: pre-flight story for the trip
- #mission: "Boarding mission complete!" with an animated miles counter
Tap flow: Home -> "My trip story" -> Story -> back -> "Boarding Badge" ->
Mission -> Done -> Home (miles card shows the new total).

STACK RULES
- Plain HTML + CSS + vanilla JavaScript. No frameworks, no npm, no build step.
- Every page links ../shared/tokens.css and loads ../shared/data.js with a
  <script> tag (so it works when opened as a file and over a local server).
- All text and numbers come from window.DATA. Never hard-code copy.
- Illustrations are inline SVG only. No external images, fonts or CDNs.
- Design for a 393x852 phone viewport.

THIS SESSION: MILESTONE 0 ONLY. Do these steps, then stop.

1. Create .gitignore containing: shots/, .DS_Store, __pycache__/

2. Create CLAUDE.md with exactly this content:

```markdown
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
```

3. Create shared/tokens.css (under 60 lines): CSS variables for a clean
   airline-style palette (deep green primary, light mint background, white
   cards, one warm accent colour for rewards), text colours with strong
   contrast, border radius, a spacing scale, one card shadow, and a system font
   stack (-apple-system, "Segoe UI", Roboto, sans-serif).

4. Create shared/data.js setting window.DATA to exactly this object. For
   story.text, write 3-4 short, warm, child-friendly sentences about Mei and her
   paper-plane friend Pip flying to Tokyo for the first time:

```js
window.DATA = {
  member: { name: "Mei" },
  companion: { name: "Pip" },
  trip: { route: "HKG → Tokyo", label: "Mei's first flight to Tokyo" },
  miles: { before: 1250, missionReward: 50, after: 1300, annualCap: 2000 },
  missions: [
    { id: "checkin",  title: "Check-in Champion", reward: 30, status: "done" },
    { id: "boarding", title: "Boarding Badge",    reward: 50, status: "ready" },
    { id: "window",   title: "Window Watcher",    reward: 30, status: "locked" },
    { id: "arrival",  title: "Arrival Explorer",  reward: 40, status: "locked" }
  ],
  stamps: [
    { city: "Taipei",  collected: true },
    { city: "Bangkok", collected: true },
    { city: "Osaka",   collected: true },
    { city: "Tokyo",   collected: false }
  ],
  story: { title: "Mei and Pip Fly to Tokyo", text: "WRITE THIS" },
  notifications: {
    linkRemoved: { title: "Cathay", body: "Your guardian link has been removed." },
    graduation:  { title: "Cathay", body: "Happy 18th, Mei! 🎓 Your miles, your history and 3 years of family transfers are coming with you." },
    future: [
      "Age 19: Family transfer received. Flying home for the holidays.",
      "Age 22: Graduation trip booked.",
      "Age 30: New junior member added: your daughter."
    ]
  },
  texts: {
    sweep:  [{ from: "Dad", body: "Moved your miles to my account last night before the cut-off 👍 Optimising." }],
    ending: [{ from: "Dad", body: "Can I borrow some miles?" }, { from: "Mei", body: "Optimising, Dad." }]
  },
  labels: { concept: "Concept screen · synthetic data" }
};
```

5. Create prototype/dev/shoot.py: a Python Playwright script that opens
   prototype/index.html at #home, #story and #mission (reloading each time) in
   a 393x852 viewport at device_scale_factor 2, waits 800ms, and saves
   screenshots to shots/proto_<screen>.png at the project root. If
   prototype/index.html doesn't exist yet, print a message and exit cleanly.

6. Run `python prototype/dev/shoot.py` to confirm it works.

7. Summarise what you created in a short list, then stop. Do not start
   building screens.