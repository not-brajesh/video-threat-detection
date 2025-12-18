import cv2
import os

def extract_frames(
    video_path,
    output_dir="DATA/frames",
    every_n_frames=30
):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_count = 0

    if not cap.isOpened():
        raise RuntimeError("❌ Video open nahi ho raha")

    print("Video opened successfully")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % every_n_frames == 0:
            frame_path = os.path.join(
                output_dir,
                f"frame_{saved_count}.jpg"
            )
            cv2.imwrite(frame_path, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Total frames saved: {saved_count}")

    return [
        os.path.join(output_dir, f)
        for f in sorted(os.listdir(output_dir))
        if f.endswith(".jpg")
    ]
