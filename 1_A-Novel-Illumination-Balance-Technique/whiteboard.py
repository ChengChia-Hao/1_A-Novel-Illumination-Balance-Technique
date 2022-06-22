from time import process_time_ns
import cv2
from collections import Counter

input_img = cv2.imread('tp1.png')
img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)


# print(input_img.shape)
# w = img_gray.shape[0]
# h = img_gray.shape[1]
w, h =img_gray.shape
print(img_gray.shape)
uml = -1

# print(img_gray[55][120])

# set unmark area to biggest gray level to one of biggest


        



