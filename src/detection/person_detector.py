import cv2

"""
# Dummy bounding box (Day 5 learning)
x1 = int(w * 0.3)
y1 = int(h * 0.3)
x2 = int(w * 0.6)
y2 = int(h * 0.8)

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
"""


image_path = "data/frames/frame_0.jpg"

img = cv2.imread(image_path)

if img is None:
    print("Image load nahi hui")
else:
    print("Image loaded successfully")
    print("Image shape:", img.shape)

    h, w, _ = img.shape

    x1 = int(w * 0.3)
    y1 = int(h * 0.3)
    x2 = int(w * 0.6)
    y2 = int(h * 0.8)

    print("BBox coordinates:", x1, y1, x2, y2)

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Person Detector - Dummy Box", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
