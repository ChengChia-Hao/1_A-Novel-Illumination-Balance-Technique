import cv2
path = '.\geeksforgeeks.png '

img = cv2.imread('rose.jpg') 
  
# Window name in which image is displayed 
window_name = 'image'
blue, green, red = cv2.split(img)
img_gs = cv2.imread('rose.jpg', cv2.IMREAD_GRAYSCALE)

# Using cv2.imshow() method  
# Displaying the image  
cv2.imshow('rose normal', img) 
cv2.waitKey()
cv2.imshow('rose red',red)
cv2.waitKey()
cv2.imshow('rose blue',blue)
cv2.waitKey()
cv2.imshow('rose green',green)
cv2.waitKey()
cv2.imshow('rose gs',img_gs)
cv2.waitKey()
cv2.imshow('rose blue',blue)
cv2.waitKey()