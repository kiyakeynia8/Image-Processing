import numpy as np
import cv2

image = cv2.imread("image adres",0)
rows, cols = image.shape
result = np.zeros((rows,cols),dtype=np.uint8)

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small = image[i-1:i+2, j-1:j+2]
        average = np.mean(small)
        result[i,j] = average

cv2.imwrite("result1.png",result)