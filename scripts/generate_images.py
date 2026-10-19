
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
IMAGE_DIR = ROOT / "images"
OUTPUT_FILE = ROOT / "images.json"

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"
}

def make_title(filename):
    # Bỏ phần mở rộng, thay dấu gạch ngang và gạch dưới bằng khoảng trắng.
    title = Path(filename).stem
    title = re.sub(r"[-_]+", " ", title)
    return title.strip()

images = []

if IMAGE_DIR.exists():
    for path in sorted(IMAGE_DIR.rglob("*")):
        if not path.is_file():
            continue

        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        relative_path = path.relative_to(ROOT).as_posix()

        images.append({
            "id": relative_path,
            "src": relative_path,
            "title": make_title(path.name)
        })

manifest = {
    "images": images
}

OUTPUT_FILE.write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

print(f"Đã tạo images.json với {len(images)} ảnh.")
