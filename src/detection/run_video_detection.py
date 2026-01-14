import json
import os

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
# Local pipeline imports
# =========================
from src.detection.frame_extractor import extract_frames
from src.detection.vlm_detector import llava_detect


VIDEO_PATH = "DATA/videos/sample.mp4"
OUTPUT_JSON = "DATA/output_detections.json"


def run_video_pipeline(video_path):
    """
    Phase 4 pipeline:
    Video -> Frames -> Detection -> Tracking -> Motion -> Relationships -> JSON
    """

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

    all_results = []

    for frame_idx, frame_path in enumerate(frames):

        result = llava_detect(frame_path)
        detections = result.get("detections", [])

        if detections:
            tracked_boxes = tracker.update(detections)
            motion_data = direction_tracker.update(tracked_boxes, frame_idx)
        else:
            tracked_boxes = []
            motion_data = []

        # 🔒 SAFE motion map
        motion_map = {}
        for m in motion_data:
            tid = m.get("track_id")
            if tid is not None:
                motion_map[tid] = m

        # attach motion safely
        for det in tracked_boxes:
            m = motion_map.get(det["track_id"])
            if m:
                det["motion"] = {
                    "dx": m.get("dx", 0.0),
                    "dy": m.get("dy", 0.0),
                    "speed": m.get("speed", 0.0),
                    "direction": m.get("direction", "STATIONARY")
                }

        relationships = relationship_analyzer.analyze(tracked_boxes)

        all_results.append({
            "image": frame_path,
            "detections": tracked_boxes,
            "relationships": relationships
        })

    return all_results


if __name__ == "__main__":

    os.makedirs("DATA", exist_ok=True)

    results = run_video_pipeline(VIDEO_PATH)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=4)

    print("✅ Phase 4 complete. Detection + Tracking + Motion + Relationships saved.")
    print(f"📄 Output file: {OUTPUT_JSON}")
