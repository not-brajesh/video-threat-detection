import cv2
import os


def extract_frames(
    video_path,
    output_dir="DATA/frames"
):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError("Video not opened")

    print("Video opened successfully")

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        raise RuntimeError("Could not determine FPS of video")

    every_n_frames = int(fps)  # 1 frame per second

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % every_n_frames == 0:

            #  RESIZE FRAME (Huge speed improvement)
            frame = cv2.resize(frame, (640, 360))

            frame_path = os.path.join(
                output_dir,
                f"frame_{saved_count}.jpg"
            )

            cv2.imwrite(frame_path, frame)
            saved_count += 1

        frame_count += 1

    cap.release()

    print(f"Original FPS: {fps}")
    print(f"Total frames saved (1 per second): {saved_count}")

    return [
        os.path.join(output_dir, f)
        for f in sorted(os.listdir(output_dir))
        if f.endswith(".jpg")
    ]