import json
import os

from src.threat_detection.threat_detector import ThreatDetector
from src.analysis.relationship_analyzer import RelationshipAnalyzer
from src.detection.tracker import SimpleTracker
from src.tracking.direction_tracker import DirectionTracker
from src.detection.person_detector import detect_persons
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

    threat_detector = ThreatDetector(running_speed_threshold=10.0)

    all_results = []

    for frame_idx, frame_path in enumerate(frames):

        result = llava_detect(frame_path)

        raw_detections = result.get("detections", [])
        detections = detect_persons(raw_detections)

        if detections:
            tracked_boxes = tracker.update(detections)
            direction_tracker.update(tracked_boxes, frame_idx)
        else:
            tracked_boxes = []

        # Attach REAL motion directly (no motion_data list)
        for det in tracked_boxes:
            tid = det.get("track_id")
            if tid is None:
                continue

            dx, dy = direction_tracker.get_motion_vector(tid)
            speed = direction_tracker.get_speed(tid)
            direction = direction_tracker.get_direction(tid)

            det["motion"] = {
                "dx": dx,
                "dy": dy,
                "speed": speed,
                "direction": direction
            }

        relationships = relationship_analyzer.analyze(tracked_boxes)

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

    print("✅ Pipeline executed successfully.")
    print(f"📄 Output file updated: {OUTPUT_JSON}")
