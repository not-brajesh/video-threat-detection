# src/tracking/direction_tracker.py

import math
from collections import deque
from src.detection.tracker import SimpleTracker


class DirectionTracker:
    def __init__(self, iou_threshold=0.4, history_size=5):
        self.tracker = SimpleTracker(iou_threshold=iou_threshold)
        self.history_size = history_size

        # track_id -> deque of (cx, cy)
        self.track_history = {}

    def _get_center(self, box):
        cx = (box["x_min"] + box["x_max"]) / 2
        cy = (box["y_min"] + box["y_max"]) / 2
        return cx, cy

    def update(self, detections, frame_idx):
        tracked = self.tracker.update(detections)

        for det in tracked:
            tid = det["track_id"]
            cx, cy = self._get_center(det)

            if tid not in self.track_history:
                self.track_history[tid] = deque(maxlen=self.history_size)

            self.track_history[tid].append((cx, cy))

        return tracked

    # ✅ THIS WAS MISSING
    def get_motion_vector(self, track_id):
        history = self.track_history.get(track_id, [])

        if len(history) < 2:
            return 0.0, 0.0

        (x1, y1) = history[-2]
        (x2, y2) = history[-1]

        return x2 - x1, y2 - y1

    def get_speed(self, track_id):
        dx, dy = self.get_motion_vector(track_id)
        return math.sqrt(dx * dx + dy * dy)

    def get_direction(self, track_id):
        dx, dy = self.get_motion_vector(track_id)

        if dx == 0 and dy == 0:
            return "STATIONARY"

        angle = math.degrees(math.atan2(-dy, dx)) % 360

        if 45 <= angle < 135:
            return "N"
        elif 135 <= angle < 225:
            return "W"
        elif 225 <= angle < 315:
            return "S"
        else:
            return "E"

    def predict_position(self, track_id, steps=3):
        history = self.track_history.get(track_id, [])

        if not history:
            return None

        cx, cy = history[-1]
        dx, dy = self.get_motion_vector(track_id)

        return cx + dx * steps, cy + dy * steps
