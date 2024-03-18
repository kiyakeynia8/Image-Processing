import cv2
import numpy as np

image = cv2.imread("input/watermelon.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(image)

h = h.astype(np.float32)

for i in range(h.shape[0]):
    for j in range(h.shape[1]):
        if 30 < h[i,j] < 90: # Green
            h[i,j] = 0
        elif h[i,j] < 30 or h[i,j] > 150: # Red
            h[i,j] += 60
            if h[i,j] > 180:
                h[i,j] -= 180

h = h.astype(np.uint8)

result = cv2.merge([h, s, v])
result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

cv2.imwrite("output/1_result.png", result)