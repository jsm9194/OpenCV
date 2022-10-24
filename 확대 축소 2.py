import cv2
img = cv2.imread('../images/cat.jpg')
dst_pyrUp = cv2.pyrUp(img) # img x 4
dst_pyrDown = cv2.pyrDown(img) # img x 1/4
cv2.imshow('img', img)
cv2.imshow('pyrUp', dst_pyrUp)
cv2.imshow('pyrDown', dst_pyrDown)
cv2.waitKey(0)
cv2.destroyAllWindows()