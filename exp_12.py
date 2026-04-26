# Experiment 12: Threshold and Region-Based Segmentation

import cv2

img = cv2.imread('input.jpg',0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
