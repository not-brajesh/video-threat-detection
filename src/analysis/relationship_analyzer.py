import math
from collections import defaultdict


class RelationshipAnalyzer:
    def __init__(self, distance_threshold=80, min_frames=5):
        """
        distance_threshold: pixels
        min_frames: how long two IDs stay close
        """
        self.distance_threshold = distance_threshold
        self.min_frames = min_frames
        self.history = defaultdict(int)

    def _center(self, box):
        cx = (box["x_min"] + box["x_max"]) / 2
        cy = (box["y_min"] + box["y_max"]) / 2
        return cx, cy

    def analyze(self, detections):
        """
        detections: list of tracked boxes in ONE frame
        """
        relations = []
        centers = {}

        for det in detections:
            centers[det["track_id"]] = self._center(det)

        ids = list(centers.keys())

        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                id1, id2 = ids[i], ids[j]
                x1, y1 = centers[id1]
                x2, y2 = centers[id2]

                dist = math.dist((x1, y1), (x2, y2))

                key = tuple(sorted((id1, id2)))

                if dist < self.distance_threshold:
                    self.history[key] += 1
                else:
                    self.history[key] = 0

                if self.history[key] >= self.min_frames:
                    relations.append({
                        "pair": [id1, id2],
                        "distance": round(dist, 2),
                        "duration_frames": self.history[key],
                        "relation": "close_proximity"
                    })

        return relations
