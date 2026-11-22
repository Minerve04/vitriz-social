"""Rend en JPEG 1080x1350 chaque a-publier/<AAAA-MM-JJ>.html."""
import glob, os, sys
from playwright.sync_api import sync_playwright
todo = sorted(glob.glob("a-publier/*.html"))
if not todo:
    print("Rien à rendre."); sys.exit(0)
errs = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for h in todo:
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(h)); pg.wait_for_timeout(800)
        w, hh = pg.evaluate("[document.documentElement.scrollWidth, document.documentElement.scrollHeight]")
        if w > 1080 or hh > 1350:
            errs.append(f"{h} déborde ({w}x{hh})")
        pg.screenshot(path=h[:-5] + ".jpg", type="jpeg", quality=90, clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        pg.close(); print("rendu", h)
    b.close()
if errs:
    print("::error::" + " ; ".join(errs)); sys.exit(1)
