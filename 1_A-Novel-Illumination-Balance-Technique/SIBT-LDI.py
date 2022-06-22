import cv2
import numpy as np

# input image & show out
input_img = cv2.imread('text-imagefortest.png')

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

# file for contours
txt_file = open('./contours.txt', 'w')

# edge detect
contours, _2 = cv2.findContours(bm_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw rectangle in contours edge
for i in range(len(contours)):
    cnt = contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    mark_img = cv2.rectangle(mark_img, (x, y), (x+w, y+h), (0, 0, 0), -2)
    txt_file.write('{}: [{},{}  {},{}  {},{}  {},{}]\n'.format(i+1, x, y, x, y+h, x+w, y, x+w, y+h))

cv2.imwrite('./Marked Image.jpg', mark_img)
txt_file.close()

cv2.imshow('Marked Image', mark_img)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# LDI Phase
# h1, w1 =img_gray.shape
# print(img_gray.shape)


LDI_img = img_gray


#  get pvf pvl

m = mark_img.shape[0]
print(m)



for i in range(len(contours)):
    cnt = contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    pfy = y
    pfx = x
    ply = y + h
    plx = x + w
    print(i+1,':','x(pfx),y(pfy),x+w(plx),y+h(ply)' , pfx, pfy, plx, ply)
    # print(x,":",pfy,ply)
    # pvf = int(input_img[pfy][x][2])
    # pvl = int(input_img[ply][x][2])
    # # ``````````````````````````````````````````````````````````````````````````````````````````````
    # pvf = int(img_gray[pfy][x])
    # pvl = int(img_gray[ply][x])
    # for numy in range(ply-pfy):
    #     k=numy+1
   
    # # LDI_img[pfy+k-1][x]=img_gray[pfy-1][x]+{img_gray[ply-1][x] - img_gray[pfy-1]}/5
    # # LDI_img[f1][x]=img_gray[f2][x]+ eq
        
    #     f1=pfy+k-1
    #     f2=pfy-1
    #     f3=ply-1
    #     f4=pfy-1

    #     eq1=img_gray[f3][x] - img_gray[f4]
    #     eq2= eq1 / 5
    #     eq = eq2 * k

    # # # resLDI=img_gray[f2][x]+ eq
    # # # LDI_img[f1][x]= resLDI
    #     LDI_img[f1][x] = img_gray[f2][x]
    #     resLDI = LDI_img[f1][x]
    #     result = resLDI + eq
    #     # print(result)
    # # ``````````````````````````````````````````````````````````````````````````````````````````````


        # while(x<=322):
        #     x=x+1
    # ``````````````````````````````````````````````````````````````````````````````````````````````
    pvf = int(img_gray[pfy][x])
    pvl = int(img_gray[ply][x])
    for numx in range(plx-pfx):
        for numy in range(ply-pfy):
    # for numy in range(ply-pfy):
    #     for numx in range(plx-pfx):
            ax = numx + pfx
            # ax = numx 
            k= numy + 1
            # k= numy 
   
    # LDI_img[pfy+k-1][x]=img_gray[pfy-1][x]+{img_gray[ply-1][x] - img_gray[pfy-1]}/5
    # LDI_img[f1][x]=img_gray[f2][x]+ eq
        
            f1=pfy+k-1
            f2=pfy-1
            f3=ply+1
            f4=pfy-1
            m=img_gray.shape[0]
            eq1=img_gray[f3][ax] - img_gray[f4][ax]
            eq2= eq1 / m
            eq = eq2 * k

    # # resLDI=img_gray[f2][x]+ eq
    # # LDI_img[f1][x]= resLDI
            LDI_img[f1][ax] = img_gray[f2][ax]
            resLDI = LDI_img[f1][ax]
            result = resLDI + eq
        # print(result)
    # ``````````````````````````````````````````````````````````````````````````````````````````````
    





# cv2.imshow('GRAY',img_gray)
cv2.imshow('LDI',LDI_img)
cv2.waitKey(0)
# print(type(LDI_img[1][1]))    
print(result)    
    
    
    

    







# -------------------------------
# for i in range(w1):
#     for j in range(h1):
        # pv = int(mark_img[i][j][2])
        # pvf = 0
        # pvl = 0
        # ------------------------------------------------------------
        # while(pv == 0):
        #     tmpj = j 
        #     pvf = j
        #     pvl = tmpj
        #     tmpj += 1
        #     pv = int(mark_img[i][tmpj][2])
        #     print(pvf,pvl)

# ------------------------------------------------------------------------------------------------
        # nh = j
        # pf = j
        # num+=1
        # pv = int(mark_img[i][j][2])
        # print(pv)
        # print( 'rount:', i ,'runtime:',  num)
        # while ( pv == 0 ):
        #     nh+=1
        #     nhpv = int(mark_img[i][nh][2])
        
# ------------------------------------------------------------------------------------------------
        # mkpv = int (mark_img[i][j])
        # if (255 == mkpv) :
        #     nh+=1
        #     mkpv = int (mark_img[i][nh])
        #     while(0 == mkpv):
        #         pvl = nh - 1
        #         nh = 0
        #         print(pvf,pvl)
        #           break