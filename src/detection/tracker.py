# src/detection/tracker.py

import itertools


def iou(boxA, boxB):
    xA = max(boxA["x_min"], boxB["x_min"])
    yA = max(boxA["y_min"], boxB["y_min"])
    xB = min(boxA["x_max"], boxB["x_max"])
    yB = min(boxA["y_max"], boxB["y_max"])

    inter_w = max(0, xB - xA)
    inter_h = max(0, yB - yA)
    inter_area = inter_w * inter_h

    areaA = (boxA["x_max"] - boxA["x_min"]) * (boxA["y_max"] - boxA["y_min"])
    areaB = (boxB["x_max"] - boxB["x_min"]) * (boxB["y_max"] - boxB["y_min"])

    union = areaA + areaB - inter_area
    if union == 0:
        return 0.0

    return inter_area / union


class SimpleTracker:
    def __init__(self, iou_threshold=0.4):
        self.iou_threshold = iou_threshold
        self.next_id = itertools.count(1)
        self.tracks = {}  # track_id -> bbox

    def update(self, detections):
        """
        detections: list of bbox dicts (pixel coords)
        returns: list of bbox dicts with 'track_id'
        """
        updated_tracks = {}
        output = []

        for det in detections:

            # 🚫 ignore tiny / garbage boxes
            if (det["x_max"] - det["x_min"]) < 50 or (det["y_max"] - det["y_min"]) < 50:
                continue

            best_iou = 0
            best_id = None

            for track_id, prev_box in self.tracks.items():
                score = iou(det, prev_box)
                if score > best_iou:
                    best_iou = score
                    best_id = track_id

            if best_iou > self.iou_threshold:
                track_id = best_id
            else:
                track_id = next(self.next_id)

            det_with_id = det.copy()
            det_with_id["track_id"] = track_id

            updated_tracks[track_id] = det
            output.append(det_with_id)

        self.tracks = updated_tracks
        return output
