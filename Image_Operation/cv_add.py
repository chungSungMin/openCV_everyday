import cv2 
import numpy as np 
"""
    mask의 경우 4번쨰 인자로 들어가게 됩니다. 그리고 mask의 인덱스값이 0이라면 해당 인덱스의 경우 
    연산을 수행하지 않고 그 외의 값을 갖는 위치에 대해서만 연산을 진행하게 됩니다.
"""


a = np.array([[1,2]], dtype=np.uint8)
b = np.array([[100,200]], dtype=np.uint8)

mask = np.array([[1,0]], dtype=np.uint8)

"""
    만일 cv2.add()의 3번쨰 인자에 b라는 변수를 넣게 되면 b의 값을 그대로 가져오는 대신 해당 결과가 b에 저장이 된다. 그래서 c와 b값이 동일해진다.
    만일 기존 b값을 유지하고 싶다면 c1 = cv2.add(a, b, b.copy(), mask) 를 사용하는게 가장 안전한 방법이다.
"""
c1 = cv2.add(a, b, b, mask) # [[101, 200]]
print(c1)

c2 = cv2.add(a, b, a , mask) # [[102, 2]]

c3 = cv2.add(a, b, None, mask) # [[203, 0]]

print(c2)
print(c3)