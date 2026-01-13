print("FILE STARTED")

import sys
import os

# project root ko path me daalo
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)

from src.tracking.direction_tracker import DirectionTracker

# fake detections (2 frames)
frame1 = [
    {"x_min": 100, "y_min": 100, "x_max": 200, "y_max": 300}
]

frame2 = [
    {"x_min": 120, "y_min": 100, "x_max": 220, "y_max": 300}
]

tracker = DirectionTracker(iou_threshold=0.0)  # force match for test

print("UPDATING FRAME 1")
tracker.update(frame1, frame_idx=1)

print("UPDATING FRAME 2")
tracked = tracker.update(frame2, frame_idx=2)

print("TRACKED OUTPUT:", tracked)

for det in tracked:
    tid = det["track_id"]

    dx, dy = tracker.get_motion_vector(tid)
    speed = tracker.get_speed(tid)
    direction = tracker.get_direction(tid)
    future = tracker.predict_position(tid)

    print("Track ID:", tid)
    print("dx, dy:", dx, dy)
    print("speed:", speed)
    print("direction:", direction)
    print("future position:", future)

print("TEST FILE EXECUTED")
