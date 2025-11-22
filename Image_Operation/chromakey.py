import numpy as np 
import cv2 
import matplotlib.pyplot as plt 


img1 = cv2.imread("./imgs/chromakey.jpeg")
img2 = cv2.imread("./imgs/background.jpeg")
img2 = cv2.resize(img2, (500,500))

height1, width1 = img1.shape[:2]
height2, width2 = img2.shape[:2]


print(f"height1 : {height1}, weight1 : {width1}")
print(f"height2 : {height2}, weight2 : {width2}")

x = (width2 - width1) // 2 
y = height2 - height1
w = x + width1
h = y + height1

chromakey = img1[:10, :10, :]
offset = 20

hsv_chroma = cv2.cvtColor(chromakey, cv2.COLOR_BGR2HSV)
hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

chroma_h = hsv_chroma[:,:,0] # H 채널의 2D 채널을 가져온 상태
lower = np.array([chroma_h.min() - offset, 100, 100])
upper = np.array([chroma_h.max() + offset, 255, 255])


mask = cv2.inRange(hsv_img, lower, upper)
mask_inv = cv2.bitwise_not(mask)

roi = img2[y:h, x:w]
fg = cv2.bitwise_and(img1, img1, mask=mask_inv)
bg = cv2.bitwise_and(roi, roi, mask=mask)
img2[y:h, x:w] = fg + bg

cv2.imshow("chromakey", img1)
cv2.imshow("added", img2)
cv2.waitKey()
cv2.destroyAllWindows()
