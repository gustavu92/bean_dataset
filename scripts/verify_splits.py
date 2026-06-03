import json
from pathlib import Path

base = Path(__file__).resolve().parents[1]
all_images = {p.name for p in (base / "images").glob("*.jpg")}

def check_txt(path):
    names = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    missing = [name for name in names if name not in all_images]
    if missing:
        raise RuntimeError(f"Missing images in {path}: {missing[:5]}")
    if len(names) != len(set(names)):
        raise RuntimeError(f"Duplicate images in {path}")
    return names

for txt in (base / "splits").rglob("*.txt"):
    names = check_txt(txt)
    print(f"{txt.relative_to(base)}: {len(names)} images")

for ann_path in (base / "annotations" / "splits").rglob("*.json"):
    data = json.loads(ann_path.read_text())
    names = {img["file_name"] for img in data["images"]}
    if not names <= all_images:
        raise RuntimeError(f"Invalid image references in {ann_path}")
    print(f"{ann_path.relative_to(base)}: {len(data['images'])} images, {len(data['annotations'])} annotations")

print("Splits OK")
