"""Screenshot the prototype screens at phone size.

Usage: python prototype/dev/shoot.py
Saves shots/proto_<screen>.png at the project root.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "prototype" / "index.html"
SHOTS = ROOT / "shots"
SCREENS = ["home", "story", "mission"]


def main():
    if not INDEX.exists():
        print("prototype/index.html not found yet - nothing to shoot.")
        return 0

    from playwright.sync_api import sync_playwright

    SHOTS.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 393, "height": 852},
            device_scale_factor=2,
        )
        page = context.new_page()
        for screen in SCREENS:
            page.goto(INDEX.as_uri() + "#" + screen)
            page.reload()  # hash-only navigation does not reload the page
            page.wait_for_timeout(800)
            out = SHOTS / f"proto_{screen}.png"
            page.screenshot(path=str(out))
            print(f"saved {out.relative_to(ROOT).as_posix()}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
