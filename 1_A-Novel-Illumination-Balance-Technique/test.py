import numpy as np
import cv2

img = cv2.imread('rose.jpg')

blue, green, red = cv2.split(img)    # Split the image into its channels
img_gs = cv2.imread('rose.jpg', cv2.IMREAD_GRAYSCALE)    # Convert image to grayscale

# cv2.imshow('rose.jpg',red) # Display the red channel in the image
# cv2.imshow(blue) # Display the red channel in the image
# cv2.imshow(green) # Display the red channel in the image
# cv2.imshow(img_gs) # Display the grayscale version of image
window_name = 'rose'
cv2.imshow(window_name, img) 
cv2.waitKey(0)

print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape)) 