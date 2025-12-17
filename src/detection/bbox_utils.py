def normalized_to_pixel_bbox(bbox_norm, image_width, image_height):
    """
    Convert normalized bbox (0–1) to absolute pixel bbox
    """

    x_min = int(bbox_norm["x_min"] * image_width)
    y_min = int(bbox_norm["y_min"] * image_height)
    x_max = int(bbox_norm["x_max"] * image_width)
    y_max = int(bbox_norm["y_max"] * image_height)

    return {
        "x_min": x_min,
        "y_min": y_min,
        "x_max": x_max,
        "y_max": y_max
    }


if __name__ == "__main__":
    # test
    bbox_norm = {
        "x_min": 0.1,
        "y_min": 0.1,
        "x_max": 0.4,
        "y_max": 0.8
    }

    pixel_bbox = normalized_to_pixel_bbox(bbox_norm, 1280, 720)
    print("Pixel bbox:", pixel_bbox)