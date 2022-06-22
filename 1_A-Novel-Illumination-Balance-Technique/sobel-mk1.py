import cv2
import numpy as np

# input image & show out
input_img = cv2.imread('tp1.png')
cv2.imshow('Input Image', input_img)
img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

#sobel edge Detector horizontal and vertical (advantage 45 degree and 135 degree)
sobelx_img = cv2.Sobel(img_gray, -3, 1, 0)
sobely_img = cv2.Sobel(img_gray, -3, 0, 1)

absX = cv2.convertScaleAbs(sobelx_img)
absY = cv2.convertScaleAbs(sobely_img)

xy_img = cv2.addWeighted(absX,0.5, absY, 0.5, 0.5)

cv2.imshow('abs X',absX)
cv2.waitKey(0)
cv2.imshow('abs Y',absY)
cv2.waitKey(0)

cv2.imshow('X Y Result',xy_img)
cv2.waitKey(0)

cv2.destroyAllWindows

# Binary edge map

ret, bm_img= cv2.threshold(xy_img, 25, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Edge Map", bm_img)
cv2.waitKey(0)

# marked edge map

kernel = np.ones((3, 3), np.uint8)
dilation_img = cv2.dilate(bm_img, kernel, iterations=1)

cv2.imshow("Dilation-Image", dilation_img)
cv2.waitKey(0)

# light distribution image

mark_img_array = np.array(dilation_img)
print(dilation_img.shape) # (471, 469)
# w = dilation_img.size[0]
# h = dilation_img.size[1]
# print(w)
# print(h)





