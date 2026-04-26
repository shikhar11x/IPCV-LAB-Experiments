# Experiment 13: Shape Representation and Chain Code.

import cv2

img = cv2.imread('input_image.jpg',0)
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    print("Boundary points:", len(cnt))
