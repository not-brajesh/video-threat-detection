def remove_duplicates(detections, eps=0.02):
    unique = []
    for d in detections:
        duplicate = False
        for u in unique:
            if (
                abs(d["x_min"] - u["x_min"]) < eps and
                abs(d["y_min"] - u["y_min"]) < eps and
                abs(d["x_max"] - u["x_max"]) < eps and
                abs(d["y_max"] - u["y_max"]) < eps
            ):
                duplicate = True
                break
        if not duplicate:
            unique.append(d)
    return unique


def remove_full_frame_boxes(detections, tol=0.02):
    cleaned = []
    for d in detections:
        if (
            d["x_min"] <= tol and
            d["y_min"] <= tol and
            d["x_max"] >= 1.0 - tol and
            d["y_max"] >= 1.0 - tol
        ):
            continue
        cleaned.append(d)
    return cleaned


def detect_persons(raw_detections):
    if not raw_detections:
        return []

    detections = remove_duplicates(raw_detections)
    detections = remove_full_frame_boxes(detections)

    return detections
