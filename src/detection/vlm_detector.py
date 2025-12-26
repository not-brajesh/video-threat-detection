import json
import base64
import requests
import re
import time
from PIL import Image

from bbox_utils import normalized_to_pixel_bbox


# =========================
# Ollama config
# =========================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llava:7b"
TIMEOUT = 240
MAX_RETRIES = 2


# =========================
# Prompt
# =========================
PROMPT = """
You are an object detection system.

Detect ALL persons visible in the image.

Return STRICT JSON ARRAY ONLY.
No explanation.
No markdown.
No extra text.

Format:
[
  {
    "label": "person",
    "x_min": 0.0,
    "y_min": 0.0,
    "x_max": 1.0,
    "y_max": 1.0
  }
]

Rules:
- Coordinates MUST be normalized between 0 and 1
- If no person exists, return []
"""


# =========================
# Utils
# =========================
def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def extract_json(text):
    if not text:
        return []

    match = re.search(r"\[\s*(?:\{.*?\}\s*,?\s*)*\]", text, re.DOTALL)
    if not match:
        return []

    try:
        data = json.loads(match.group())
        return data if isinstance(data, list) else []
    except Exception:
        return []


def clamp(v):
    return max(0.0, min(1.0, float(v)))


def is_valid_box(b):
    required = {"x_min", "y_min", "x_max", "y_max"}
    if not required.issubset(b.keys()):
        return False

    # full-frame garbage
    if (
        b["x_min"] == 0 and b["y_min"] == 0 and
        b["x_max"] == 1 and b["y_max"] == 1
    ):
        return False

    return True


def deduplicate_boxes(boxes, tol=20):
    unique = []
    for b in boxes:
        if not any(
            abs(b["x_min"] - u["x_min"]) < tol and
            abs(b["y_min"] - u["y_min"]) < tol and
            abs(b["x_max"] - u["x_max"]) < tol and
            abs(b["y_max"] - u["y_max"]) < tol
            for u in unique
        ):
            unique.append(b)
    return unique


# =========================
# Detector
# =========================
def llava_detect(image_path):
    image = Image.open(image_path).convert("RGB")
    w, h = image.size

    payload = {
        "model": MODEL_NAME,
        "prompt": PROMPT,
        "images": [image_to_base64(image_path)],
        "stream": False
    }

    raw_text = ""

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.post(
                OLLAMA_URL,
                json=payload,
                timeout=TIMEOUT
            )
            raw_text = r.json().get("response", "")
            break
        except Exception as e:
            print(f"⚠️ Ollama attempt {attempt} failed:", e)
            time.sleep(2)

    if not raw_text:
        return {"image": image_path, "detections": []}

    print("\n===== RAW MODEL OUTPUT =====")
    print(raw_text)
    print("============================\n")

    boxes = extract_json(raw_text)

    pixel_boxes = []
    for b in boxes:
        if isinstance(b, dict) and is_valid_box(b):
            # clamp safety
            b["x_min"] = clamp(b["x_min"])
            b["y_min"] = clamp(b["y_min"])
            b["x_max"] = clamp(b["x_max"])
            b["y_max"] = clamp(b["y_max"])

            pixel_boxes.append(
                normalized_to_pixel_bbox(b, w, h)
            )

    pixel_boxes = deduplicate_boxes(pixel_boxes)

    return {
        "image": image_path,
        "detections": pixel_boxes
    }


# =========================
# Test
# =========================
if __name__ == "__main__":
    test_image = "DATA/frames/frame_0.jpg"
    result = llava_detect(test_image)
    print(json.dumps(result, indent=2))
