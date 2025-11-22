import cv2 
import numpy as np 

img1 = cv2.resize(cv2.imread("imgs/강아지.jpeg"), (128, 128))
img2 = cv2.resize(cv2.imread("imgs/고양이.jpg"), (128, 128))


alpha = 0.5 

blended = img1 * alpha + img2 * (1-alpha)
blended = blended.astype(np.uint8)
cv2.imshow("blended1", blended)

blended = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)
cv2.imshow("blended2", blended)

cv2.waitKey(0)
cv2.destroyAllWindows()