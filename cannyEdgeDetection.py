import cv2

img=cv2.imread("1.jpg",0)

canny=cv2.Canny(img,100,120)

cv2.imshow("Canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()