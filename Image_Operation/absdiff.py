import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img1 = cv2.imread("./imgs/back1.png")
img2 = cv2.imread("./imgs/back2.png")

diff = cv2.absdiff(img1, img2)

img1_rgb, img2_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
diff_rgb = cv2.cvtColor(diff, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(5, 5))


plt.subplot(1,3,1)
plt.imshow(img1_rgb)
plt.title("version1")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(img2_rgb)
plt.title("version2")
plt.axis("off")


plt.subplot(1,3,3)
plt.imshow(diff_rgb)
plt.title("different")
plt.axis("off")


plt.show()