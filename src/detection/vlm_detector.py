import json
from PIL import Image

# import bbox utility
from bbox_utils import normalized_to_pixel_bbox


def vlm_stub_detect(image_path: str):
    """
    Week-1 SAFE VLM Stub Detector
    - NO real Florence inference
    - Outputs FINAL JSON with PIXEL bounding boxes
    """

    # load image
    image = Image.open(image_path).convert("RGB")
    image_width, image_height = image.size

    # -----------------------------
    # STUB normalized bbox (fake VLM output)
    # -----------------------------
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

    # detected objects
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


# -----------------------------
# RUN TEST
# -----------------------------
if __name__ == "__main__":
    image_path = "DATA/frames/frame_0.jpg"

    result = vlm_stub_detect(image_path)

    print("VLM inference output (FINAL - Week 1):")
    print(json.dumps(result, indent=4))
