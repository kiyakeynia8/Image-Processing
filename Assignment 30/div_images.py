import cv2

image_1 = cv2.imread("input/e.tif",0)
image_2 = cv2.imread("input/f.tif",0)
image_1 = cv2.resize(image_1,[300,400])
image_2 = cv2.resize(image_2,[300,400])

result = image_1 / image_2

cv2.imshow("result",result)
cv2.waitKey()