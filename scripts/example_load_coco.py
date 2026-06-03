from pathlib import Path
import json

dataset_root = Path(__file__).resolve().parents[1]
annotation_file = dataset_root / "annotations" / "instances.json"
images_dir = dataset_root / "images"

with annotation_file.open("r", encoding="utf-8") as f:
    coco = json.load(f)

images = coco["images"]
annotations = coco["annotations"]
categories = coco["categories"]

print(f"Images: {len(images)}")
print(f"Annotations: {len(annotations)}")
print("Categories:")

for category in categories:
    print(f"- {category['id']}: {category['name']}")

first_image = images[0]
image_path = images_dir / first_image["file_name"]

print(f"\nFirst image: {image_path}")
print(f"Exists: {image_path.exists()}")
