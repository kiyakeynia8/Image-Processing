import cv2

image = cv2.imread("input/spiderman.jpg")
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         if image_HSV[i,j,0] < 25:
#             image_HSV[i,j,0] += 60
#         if image_HSV[i,j,0] > 170:
#             image_HSV[i,j,0] -= 120

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image_HSV[i,j,0] < 15:
            image_HSV[i,j,0] += 15
        if image_HSV[i,j,0] > 170:
            image_HSV[i,j,0] -= 150
   
result = cv2.cvtColor(image_HSV, cv2.COLOR_HSV2BGR)

# cv2.imwrite("output/7_result_1.png", result)
cv2.imwrite("output/7_result_2.png", result)