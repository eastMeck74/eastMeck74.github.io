import json
from pathlib import Path


FEP_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = FEP_DIR / "photos.json"
JAVASCRIPT_FILE = FEP_DIR / "photos.js"

DISPLAY_NAMES = {
    "Katheryn Kerr.webp": "Kathryn Kerr",
    "Michele Gross Newkirk.webp": "Michele Gross",
    "PUJ7y1-R_400x400.webp": "East Meck Eagle",
    "Rodney Kohlmeyor.webp": "Rodney Kohlmeyer",
}
DESATURATED_PHOTOS = {
    "David Duncan.webp",
    "Kim Alexander.webp",
    "Nancy Henley.webp",
    "Nick Melibruda.webp",
}


photos = []
for image_path in sorted(FEP_DIR.iterdir(), key=lambda path: path.name.casefold()):
    if image_path.is_file() and image_path.suffix.lower() == ".webp":
        photo = {
            "file": image_path.name,
            "name": DISPLAY_NAMES.get(image_path.name, image_path.stem),
        }
        if image_path.name in DESATURATED_PHOTOS:
            photo["desaturate"] = True
        photos.append(photo)

OUTPUT_FILE.write_text(json.dumps(photos, indent=2) + "\n", encoding="utf-8")
JAVASCRIPT_FILE.write_text(
    "window.fallenEaglesPhotos = "
    + json.dumps(photos, ensure_ascii=True, separators=(",", ":"))
    + ";\n",
    encoding="utf-8",
)
print(f"Wrote {len(photos)} WebP photos to {OUTPUT_FILE.name} and {JAVASCRIPT_FILE.name}")
