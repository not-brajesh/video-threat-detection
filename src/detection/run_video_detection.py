import json
import os
from tracker import SimpleTracker

# local imports
from frame_extractor import extract_frames
from vlm_detector import llava_detect

VIDEO_PATH = "DATA/videos/sample.mp4"
OUTPUT_JSON = "DATA/output_detections.json"


def run_video_pipeline(video_path):
    """
    Phase 2 pipeline:
    Video -> Frames -> Detection -> Tracking -> JSON
    """

    frames = extract_frames(
        video_path,
        output_dir="DATA/frames",
        every_n_frames=60
    )

    # 🔒 Tracker initialized ONCE (very important)
    tracker = SimpleTracker(iou_threshold=0.4)

    all_results = []

    for frame_path in frames:
        result = llava_detect(frame_path)

        detections = result.get("detections", [])

        # 🧠 Apply tracking only if detections exist
        if detections:
            tracked_boxes = tracker.update(detections)
        else:
            tracked_boxes = []

        all_results.append({
            "image": frame_path,
            "detections": tracked_boxes
        })

    return all_results


if __name__ == "__main__":

    os.makedirs("DATA", exist_ok=True)

    results = run_video_pipeline(VIDEO_PATH)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=4)

    print("✅ Phase 2 complete. Detection + Tracking JSON saved.")
    print(f"📄 Output file: {OUTPUT_JSON}")
