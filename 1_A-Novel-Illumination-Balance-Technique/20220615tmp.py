import cv2
import numpy as np

# input image & show out
input_img = cv2.imread('testtp.jpg')

mark_img = input_img

cv2.imshow('Input Image', input_img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', img_gray)
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

# 文件路徑，用於記錄輪廓框座標
txt_file = open('./contours.txt', 'w')

# 邊緣檢測，得到的輪廓列表
contours, _2 = cv2.findContours(bm_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 根據輪廓列表，迴圈在原始影象上繪製矩形邊界
for i in range(len(contours)):
    cnt = contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    mark_img = cv2.rectangle(mark_img, (x, y), (x+w, y+h), (0, 0, 0), -2)
    txt_file.write('{}: [{},{}  {},{}  {},{}  {},{}]\n'.format(i+1, x, y, x, y+h, x+w, y, x+w, y+h))

cv2.imwrite('./Marked Image.jpg', mark_img)
txt_file.close()

cv2.imshow('Marked Image', mark_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





