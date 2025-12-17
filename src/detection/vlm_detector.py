import json
from PIL import Image

# import bbox utility
from bbox_utils import normalized_to_pixel_bbox


def vlm_stub_detect(image_path: str):
    """
    Stub Vision-Language Model detection
    Returns object detection output with PIXEL bounding boxes
    """

    # load image
    img = Image.open(image_path).convert("RGB")
    image_width, image_height = img.size

    # ---- STUB VLM OUTPUT (normalized bbox) ----
    bbox_norm = {
        "x_min": 0.1,
        "y_min": 0.1,
        "x_max": 0.4,
        "y_max": 0.8
    }

    # convert normalized → pixel bbox
    bbox_pixel = normalized_to_pixel_bbox(
        bbox_norm,
        image_width,
        image_height
    )

    objects = [
        {
            "label": "person",
            "confidence": 0.92,
            "bbox_pixel": bbox_pixel
        }
    ]

    # final JSON output
    output = {
        "image": image_path,
        "image_size": {
            "width": image_width,
            "height": image_height
        },
        "objects": objects
    }

    return output


# ----------------- RUN TEST -----------------
if __name__ == "__main__":
    image_path = "DATA/frames/frame_0.jpg"

    result = vlm_stub_detect(image_path)

    print("VLM inference output (FINAL):")
    print(json.dumps(result, indent=4))
