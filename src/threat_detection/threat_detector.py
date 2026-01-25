from dataclasses import dataclass
from typing import List, Dict
import time


@dataclass
class Threat:
    threat_type: str
    severity: int
    description: str
    involved_ids: List[int]
    frame: str
    timestamp: float


class ThreatDetector:
    def __init__(self, running_speed_threshold: float = 50.0):
        self.running_speed_threshold = running_speed_threshold

    def detect(
        self,
        detections: List[Dict],
        relationships: List[Dict],
        frame_path: str
    ) -> List[Threat]:
        threats: List[Threat] = []

        for det in detections:
            motion = det.get("motion", {})
            speed = motion.get("speed", 0.0)

            if speed > self.running_speed_threshold:
                threats.append(
                    Threat(
                        threat_type="RUNNING",
                        severity=2,
                        description=f"Person running with speed {speed:.2f}",
                        involved_ids=[det.get("track_id", -1)],
                        frame=frame_path,
                        timestamp=time.time(),
                    )
                )

        return threats
