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

            # NOTE:
            # Tiny-box filter TEMPORARILY REMOVED for testing Phase-3
            # (Will be added back later for real video)

            best_iou = 0.0
            best_id = None

            for track_id, prev_box in self.tracks.items():
                score = iou(det, prev_box)
                if score > best_iou:
                    best_iou = score
                    best_id = track_id

            if best_iou > self.iou_threshold and best_id is not None:
                track_id = best_id
            else:
                track_id = next(self.next_id)

            det_with_id = det.copy()
            det_with_id["track_id"] = track_id

            updated_tracks[track_id] = det
            output.append(det_with_id)

        self.tracks = updated_tracks
        return output

import math
from collections import deque

class DirectionTracker:
    def __init__(self, history_size=15, fps=30):
        self.history_size = history_size
        self.fps = fps
        self.tracks = {}  # track_id -> deque of (cx, cy)

    def update(self, tracked_objects):
        """
        tracked_objects: list of dicts having 'track_id' and 'bbox'
        bbox format: {"x_min":, "y_min":, "x_max":, "y_max":}
        """
        results = []

        for obj in tracked_objects:
            tid = obj["track_id"]
            box = {
                "x_min": obj["x_min"],
                "y_min": obj["y_min"],
                "x_max": obj["x_max"],
                "y_max": obj["y_max"]
            }

      
            cx = (box["x_min"] + box["x_max"]) / 2
            cy = (box["y_min"] + box["y_max"]) / 2

            if tid not in self.tracks:
                self.tracks[tid] = deque(maxlen=self.history_size)

            self.tracks[tid].append((cx, cy))

            dx, dy, speed, direction = self._compute_motion(self.tracks[tid])

            results.append({
                "track_id": tid,
                "dx": dx,
                "dy": dy,
                "speed": speed,
                "direction": direction
            })

        return results

    def _compute_motion(self, points):
        if len(points) < 2:
            return 0.0, 0.0, 0.0, "STATIONARY"

        x1, y1 = points[0]
        x2, y2 = points[-1]

        dx = (x2 - x1) * self.fps
        dy = (y2 - y1) * self.fps

        speed = math.sqrt(dx*dx + dy*dy)

        angle = math.degrees(math.atan2(-dy, dx)) % 360

        if speed < 5:
            direction = "STATIONARY"
        elif 45 <= angle < 135:
            direction = "N"
        elif 135 <= angle < 225:
            direction = "W"
        elif 225 <= angle < 315:
            direction = "S"
        else:
            direction = "E"

        return dx, dy, speed, direction
