import json
import os

# local imports
from frame_extractor import extract_frames
from vlm_detector import llava_detect

VIDEO_PATH = "DATA/videos/sample.mp4"
OUTPUT_JSON = "DATA/output_detections.json"


def run_video_pipeline(video_path):
    """
    Runs full Phase-1 pipeline:
    Video -> Frames -> Stub Detection -> JSON
    """

    # extract frames from video
    frames = extract_frames(
        video_path,
        output_dir="DATA/frames",
        every_n_frames=30
    )

    all_detections = []

    for frame_path in frames:
        result = llava_detect(frame_path)
        all_detections.append(result)

    return all_detections


if __name__ == "__main__":

    # ensure DATA folder exists
    os.makedirs("DATA", exist_ok=True)

    detections = run_video_pipeline(VIDEO_PATH)

    # save final JSON
    with open(OUTPUT_JSON, "w") as f:
        json.dump(detections, f, indent=4)

    print("✅ Phase 1 complete. Detection JSON saved.")
    print(f"📄 Output file: {OUTPUT_JSON}")
