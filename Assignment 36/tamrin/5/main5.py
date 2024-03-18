import cv2
import numpy as np
import matplotlib.pyplot as plt

image_b = cv2.imread('input/123346.jpg')
image_s = cv2.imread('input/SuperMan.jpg')
image_s = cv2.resize(image_s, (image_b.shape[1], image_b.shape[0]))
image_HAV = cv2.cvtColor(image_s, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(image_HAV)

for i in range(image_b.shape[0]):
    for j in range(image_b.shape[1]//2):
        if 35 < h[i, j] < 75 and v[i, j] > 55:
            image_s[i,j] = image_b[i, j]

    for j in range(image_b.shape[1]//2, image_b.shape[1]):
        if 30 < h[i, j] < 90 and v[i, j] > 140:
            image_s[i,j] = image_b[i, j]

for i in range(image_b.shape[0]//2, image_b.shape[0]):
    for j in range(image_b.shape[1]//2, image_b.shape[1]):
        if 35 < h[i, j] < 75 and v[i, j] > 55:
            image_s[i,j] = image_b[i, j]

cv2.imwrite("output/5_result.png",image_s)