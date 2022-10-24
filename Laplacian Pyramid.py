import cv2
import numpy as np

img = cv2.imread('../images/cat.jpg')
smaller = cv2.pyrDown(img)
bigger = cv2.pyrUp(smaller)
laplacian = cv2.subtract(img, bigger)
restored = bigger + laplacian
merged = np.hstack((img, laplacian, bigger, restored))
# img_show("Laplacian Pyramid", merged, (16, 4))
# cv2.imshow("Laplacian Pyramid" , merged)
cv2.imshow('img', img)
cv2.imshow('smaller', smaller)
cv2.imshow('bigger', bigger)
cv2.imshow('laplacian', laplacian)
cv2.imshow('restored', restored)

cv2.waitKey(0)
cv2.destroyAllWindows()