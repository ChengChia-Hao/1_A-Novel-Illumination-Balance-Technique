import cv2
img = cv2.imread('test.jpg')
h, w = img.shape


up=max()
dn=min()
lft=max()
rt=min()
for i in range(h):
    for j in range(w):
        if img[h,w] == 255 :
            if img[h-1,w] == 255 :
                if h-1 < up :
                    up = h-1
            elif img[h+1,w] == 255 :
                if h+1 > dn :
                    dn = h+1
            