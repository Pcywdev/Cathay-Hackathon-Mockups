---
name: screen-check
description: Verify prototype screens and overlays after any visual change. Use before declaring any screen or overlay done.
---

# Screen check

1. Run `python tools/shoot.py`.
2. Open every image in shots/ and exports/ and look at it.
3. Check each item and report PASS or FAIL with a one-line reason:
   - Text and numbers match shared/data.js exactly (miles 1,250 to 1,300, cap 2,000, "+50")
   - Prototype screens show the label "Concept screen, synthetic data"
   - Nothing is cut off, overlapping or overflowing at 393x852
   - Text readable at phone size (body at least 15px, no low-contrast grey on tinted backgrounds)
   - Prototype follows shared/DESIGN.md: orange only on miles and rewards, stamp blue only on stamps, two radii (16px, 999px), one shadow
   - Overlays look like native Android (Material 3 notifications, Google Messages bubbles), not iOS
   - Overlay PNGs have transparent backgrounds and are named S<scene>_<what>; exports/ holds exactly 7:
     S1_notif_link_removed, S4c_notif_graduation, S2_text_sweep, S6_text_ending, S6_future_1, S6_future_2, S6_future_3
   - No missions or copy suggesting earning outside a trip
   - No official Cathay logo; nothing implies a real integration
4. Fix FAILs, then re-run once. If still failing after two rounds, stop and report.
