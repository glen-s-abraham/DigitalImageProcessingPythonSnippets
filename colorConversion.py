import cv2

img=cv2.imread('1.jpg',1)
cv2.imshow("RGB",img)

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("RGB to Gray",gray)

hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow("RGB to HSV",hsv)


cv2.waitKey(0)
cv2.destroyAllWindows()