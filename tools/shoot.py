"""Run everything: prototype screenshots, then overlay PNG export.

Usage: python tools/shoot.py
The prototype part is prototype/dev/shoot.py (Builder A's script, reused here
so the screenshot logic lives in one place). This script only adds the overlay
export: exports/<data-export>.png with a transparent background.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORTS = ROOT / "exports"


def run_prototype_shots():
    path = ROOT / "prototype" / "dev" / "shoot.py"
    spec = importlib.util.spec_from_file_location("proto_shoot", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def export_overlays():
    overlays = ROOT / "overlays" / "index.html"
    if not overlays.exists():
        return
    from playwright.sync_api import sync_playwright

    EXPORTS.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 393, "height": 852}, device_scale_factor=2)
        page.goto(overlays.as_uri())
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(500)
        for el in page.query_selector_all("[data-export]"):
            out = EXPORTS / f"{el.get_attribute('data-export')}.png"
            el.screenshot(path=str(out), omit_background=True)
            print(f"saved {out.relative_to(ROOT).as_posix()}")
        browser.close()


if __name__ == "__main__":
    run_prototype_shots()
    export_overlays()
    sys.exit(0)
