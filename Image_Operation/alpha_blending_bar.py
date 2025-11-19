import cv2 
import numpy as np 

win_name = "Alpha blending"
trackbar_name = "fade"

def onChange(x):
    alpha = x / 100 
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0 )
    cv2.imshow(win_name, dst)

img1 = cv2.imread("imgs/고양이.jpg")
img2 = cv2.imread("imgs/강아지.jpeg")

img1 = cv2.resize(img1,(128,128))
img2 = cv2.resize(img2,(128,128))

cv2.imshow(win_name, img1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()
