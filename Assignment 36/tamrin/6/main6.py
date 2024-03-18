import cv2

image = cv2.imread("input/man.jpg")
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if 40 < image_HSV[i,j,0] < 160 :
            image_HSV[i,j,0] += 120
            if image_HSV[i,j,0] >= 180:
                image_HSV[i,j,0] -= 180
   
result = cv2.cvtColor(image_HSV, cv2.COLOR_HSV2BGR)

cv2.imwrite("output/6_result.png", result)