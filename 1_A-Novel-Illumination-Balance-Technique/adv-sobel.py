import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lines.png')

plt.imshow(img, cmap='gray')
plt.show()

kernel = np.array([[0, -1, 0],
                   [1, 0, 1],
                   [0, -1, 0]])
kernel = np.ones((7, 7), np.uint8)
other = cv2.erode(img, kernel, iterations = 1)
_,thresh = cv2.threshold(other,10,255,cv2.THRESH_BINARY)
result = cv2.bitwise_and(img, cv2.bitwise_not(thresh))
cv2.imshow("Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst = cv2.filter2D(img, -1, kernel)
cv2.imwrite("filtered.png", dst)