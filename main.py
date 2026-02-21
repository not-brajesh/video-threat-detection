import json
import os

from src.detection.run_video_detection import run_video_pipeline

VIDEO_PATH = "DATA/videos/sample.mp4"
OUTPUT_JSON = "DATA/output_detections.json"

if __name__ == "__main__":

    os.makedirs("DATA", exist_ok=True)

    results = run_video_pipeline(VIDEO_PATH)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=4)

    print("✅ Pipeline executed successfully.")
    print(f"📄 Output file updated: {OUTPUT_JSON}")