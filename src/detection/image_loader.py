import os
import cv2

frames_dir = "data/frames"

images = sorted(os.listdir(frames_dir))

print("Total images found:", len(images))

# sirf first image open karke dikha do
first_image_path = os.path.join(frames_dir, images[0])

img = cv2.imread(first_image_path)

cv2.imshow("First Extracted Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
