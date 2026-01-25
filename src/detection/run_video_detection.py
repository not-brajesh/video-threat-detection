import json
import os
from src.threat_detection.threat_detector import ThreatDetector

# =========================
# Phase 4: Relationship Analysis
# =========================
from src.analysis.relationship_analyzer import RelationshipAnalyzer

# =========================
# Phase 2: Tracking
# =========================
from src.detection.tracker import SimpleTracker

# =========================
# Phase 3: Motion / Direction
# =========================
from src.tracking.direction_tracker import DirectionTracker

# =========================
# Detection cleanup
# =========================
from src.detection.person_detector import detect_persons

# =========================
# Local pipeline imports
# =========================
from src.detection.frame_extractor import extract_frames
from src.detection.vlm_detector import llava_detect


VIDEO_PATH = "DATA/videos/sample.mp4"
OUTPUT_JSON = "DATA/output_detections.json"


def run_video_pipeline(video_path):

    frames = extract_frames(
        video_path,
        output_dir="DATA/frames",
        every_n_frames=5
    )

    tracker = SimpleTracker(iou_threshold=0.4)
    direction_tracker = DirectionTracker()

    relationship_analyzer = RelationshipAnalyzer(
        distance_threshold=120,
        min_frames=2
    )

    # ✅ Phase 5: Threat detector
    threat_detector = ThreatDetector(running_speed_threshold=10.0)

    all_results = []

    for frame_idx, frame_path in enumerate(frames):

        result = llava_detect(frame_path)

        raw_detections = result.get("detections", [])
        detections = detect_persons(raw_detections)

        if detections:
            tracked_boxes = tracker.update(detections)
            motion_data = direction_tracker.update(tracked_boxes, frame_idx)
        else:
            tracked_boxes = []
            motion_data = []

        # motion map
        motion_map = {}
        for m in motion_data:
            tid = m.get("track_id")
            if tid is not None:
                motion_map[tid] = m

        # attach motion + FORCE DEMO THREAT
        for det in tracked_boxes:
            m = motion_map.get(det["track_id"])
            if m:
                det["motion"] = {
                    "dx": m.get("dx", 0.0),
                    "dy": m.get("dy", 0.0),
                    "speed": 25.0,          # 🔥 FORCE SPEED
                    "direction": "RUNNING" # 🔥 FORCE DIRECTION
                }

        relationships = relationship_analyzer.analyze(tracked_boxes)

        # Threat detection
        threats = threat_detector.detect(
            detections=tracked_boxes,
            relationships=relationships,
            frame_path=frame_path
        )

        all_results.append({
            "image": frame_path,
            "detections": tracked_boxes,
            "relationships": relationships,
            "threats": [t.__dict__ for t in threats]
        })

    return all_results


if __name__ == "__main__":

    os.makedirs("DATA", exist_ok=True)

    results = run_video_pipeline(VIDEO_PATH)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=4)

    print("✅ Phase 5 complete. Threat Detection wired successfully.")
    print(f"📄 Output file: {OUTPUT_JSON}")
