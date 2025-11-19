import cv2 
import numpy as np 
import matplotlib.pyplot  as plt 

img1 = cv2.imread("imgs/고양이.jpg")
img2 = cv2.imread("imgs/강아지.jpeg")

img1 = cv2.resize(img1,(128,128))
img2 = cv2.resize(img2,(128,128))

img3 = img1 + img2 
img4 = cv2.add(img1, img2)

imgs = {
    "img1" : img1, "img2" : img2,
    "img3" : img3, "img4" : img4
    }

for i, (k,v) in enumerate(imgs.items()) : 
    plt.subplot(2,2,i+1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
    plt.xticks([]); plt.yticks([]) 
plt.show()   
