import cv2 
import numpy as np 

img = cv2.imread("sun.jpeg")

y, x = 100, 200
w, h = 50, 50
roi = img[y:y+h, x:x+w]

cv2.rectangle(roi, (0,0), (h-1,w-1), (0,255,0))
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()