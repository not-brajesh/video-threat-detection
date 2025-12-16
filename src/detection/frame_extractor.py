import cv2
import os

video_path = "data/videos/sample.mp4"
output_dir = "data/frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video open nahi ho rahi")
    exit()

print("Video opened successfully")

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Video khatam ho gaya")
        break

    frame_count += 1

    # har 10th frame save karo
    if frame_count % 10 == 0:
        frame_name = f"frame_{saved_count}.jpg"
        frame_path = os.path.join(output_dir, frame_name)
        cv2.imwrite(frame_path, frame)
        saved_count += 1

cap.release()
print(f"Total frames saved: {saved_count}")
