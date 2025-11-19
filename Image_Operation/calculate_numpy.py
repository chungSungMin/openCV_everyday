import cv2 
import numpy as np 

""" cv2에서 연산을 제공하는 이유 
cv2에서 연산을 제공하는 이유는 이미지 끼리 연산을 하다 보면 255를 넘어가거나 0 보다 작아지는 
결과를 볼 수 있다. 이러한 결과 단순 연산을 하게 되면 우리가 원하는 결과랑 매우 다른 결과를 얻을 수 
있기 때문에 안정장치가 마련되어있는 cv2 의 라이브러리를 사용하는게 조금더 안정적이다.
"""


a = np.uint8([[200,50]]) 
b = np.uint8([[100,100]]) # shape : [1,2]

add1 = a + b 
sub1 = a - b 
mul1 = a * 2 
sub1 = a / 3

add2 = cv2.add(a,b)
sub2 = cv2.subtract(a,b)
mul2 = cv2.multiply(a, 2)
sub2 = cv2.divide(a,3)

print(add1, add2)
print(sub1, sub2)
print(mul1, mul2)
print(sub1, sub2)
