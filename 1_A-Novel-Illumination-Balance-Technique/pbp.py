import cv2
import numpy as np

input_img = cv2.imread('testcopy.jpg')
gray_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

# -------------------------------------------------
# print("Gray:",gray_img[1,1])
# for i in range(w):
#     for j in range(h):


# for i in range(h):
#     for j in range(w):
#         print("Gray:",gray_img[h,w],end=",")
# print("-")  


# -------------------------------------------------



#sobel edge Detector horizontal and vertical (advantage 45 degree and 135 degree)
sobelx_img = cv2.Sobel(gray_img, -3, 1, 0)
sobely_img = cv2.Sobel(gray_img, -3, 0, 1)

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







# Object Mark Phase

def mark (a , b ):
    uy=a
    dy=0
    lx=b
    rx=0
    a+=1
    while([a,b]>=1):
        a+=1
        dy=a
        if([a,b]>=1):
            b+=1
            rx=b
    return uy, dy, lx, rx
        
            
        




# h=horizontal w=vertical
h, w = bm_img.shape
print("height:",h) 
print("width:",w) 
copyInput_img=input_img
copybm_img=bm_img

results = list(map(int, copybm_img[i]))
print(type(results))

# print("gray level=", bm_img[100]) #[row, column] 
# print("Gray:",gray_img[150])
for i in range(h):
    
    for j in range(w):
        loc =  int[i,j]
        while loc>0 :
            mark(i, j)
            y1,y2,x1,x2 = mark()
cv2.rectangle(bm_img, (x1,y1), (x2, y2), (255), -2) 
cv2.imshow("Binary Edge Map", bm_img)
cv2.waitKey(0)

