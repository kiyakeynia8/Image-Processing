import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input/Balloons.PNG")

mask = cv2.inRange(cv2.cvtColor(image, cv2.COLOR_BGR2HSV), np.array([160,0,0]), np.array([180,255,255]))
mask = (mask/255).astype(int)
result = cv2.merge([mask * image[:,:,0], mask * image[:,:,1], mask * image[:,:,2]])

cv2.imwrite("output/3_result.png", result)