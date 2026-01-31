import cv2
import numpy as np

image = cv2.imread(r"F:\eagle.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)

eroded = cv2.erode(gray, kernel, iterations=1)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Eroded Image", eroded)#BHANUTEJA REDDY

cv2.waitKey(0)
cv2.destroyAllWindows()
