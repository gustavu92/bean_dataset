import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
ann_path = root / "annotations" / "instances.json"
images_dir = root / "images"

with ann_path.open() as f:
    coco = json.load(f)

image_files = {p.name for p in images_dir.glob("*.jpg")}
json_files = {image["file_name"] for image in coco["images"]}
missing = sorted(json_files - image_files)
extra = sorted(image_files - json_files)
category_ids = {category["id"] for category in coco["categories"]}
image_ids = {image["id"] for image in coco["images"]}
invalid_annotations = [
    annotation["id"]
    for annotation in coco["annotations"]
    if annotation["image_id"] not in image_ids or annotation["category_id"] not in category_ids
]

print(f"Images in JSON: {len(json_files)}")
print(f"Images in folder: {len(image_files)}")
print(f"Annotations: {len(coco['annotations'])}")
print(f"Categories: {[category['name'] for category in coco['categories']]}")

if missing or extra or invalid_annotations:
    raise SystemExit(
        f"Invalid dataset. Missing: {len(missing)}, extra: {len(extra)}, invalid annotations: {len(invalid_annotations)}"
    )

print("Dataset OK")
