import json
import os

# trackers
from tracker import SimpleTracker, DirectionTracker

# local imports
from frame_extractor import extract_frames
from vlm_detector import llava_detect

VIDEO_PATH = "DATA/videos/sample.mp4"
OUTPUT_JSON = "DATA/output_detections.json"
FPS = 30


def run_video_pipeline(video_path):
    """
    Phase 3 pipeline:
    Video -> Frames -> Detection -> Tracking -> Motion -> JSON
    """

    frames = extract_frames(
        video_path,
        output_dir="DATA/frames",
        every_n_frames=60
    )

    # 🔒 Trackers initialized ONCE
    tracker = SimpleTracker(iou_threshold=0.4)
    direction_tracker = DirectionTracker(fps=FPS)

    all_results = []

    for frame_path in frames:
        result = llava_detect(frame_path)
        detections = result.get("detections", [])

        # 🧠 Apply tracking
        if detections:
            tracked_boxes = tracker.update(detections)
            motion_data = direction_tracker.update(tracked_boxes)
        else:
            tracked_boxes = []
            motion_data = []

        # attach motion info to detections
        for det in tracked_boxes:
            for motion in motion_data:
                if det["track_id"] == motion["track_id"]:
                    det["motion"] = {
                        "dx": motion["dx"],
                        "dy": motion["dy"],
                        "speed": motion["speed"],
                        "direction": motion["direction"]
                    }

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

    print("✅ Phase 3 complete. Detection + Tracking + Motion saved.")
    print(f"📄 Output file: {OUTPUT_JSON}")
