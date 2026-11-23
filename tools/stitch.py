"""Stitch 2x2 zoomed tiles (each 800x500) into one 1600x1000 screenshot.

Usage: python3 tools/stitch.py out.jpg tl.png tr.png bl.png br.png
Tiles come from the page scaled 2x with CSS and shifted by one viewport each.
"""
import sys
from PIL import Image

out, *tiles = sys.argv[1:]
imgs = [Image.open(t).convert("RGB") for t in tiles]
w, h = imgs[0].size
canvas = Image.new("RGB", (w * 2, h * 2), "white")
for i, im in enumerate(imgs):
    canvas.paste(im, ((i % 2) * w, (i // 2) * h))
canvas.save(out, quality=92)
print("saved", out, canvas.size)
