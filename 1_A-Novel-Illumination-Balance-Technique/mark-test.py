import cv2
import numpy as np
img = cv2.imread('test.jpg', 0)

cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), -1)

cv2.imshow('markerd', img)
cv2.waitKey(0)

# test count with for autocorrelation
# im2,contours, hier = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# for c in contours:
#     # get the bounding rect
#     x, y, w, h = cv2.boundingRect(c)
#     # draw a white rectangle to visualize the bounding rect
#     cv2.rectangle(output_img, (x, y), (x + w, y + h), 255, 1)

# cv2.imshow('output',output_img)
# cv2.waitKey(0)