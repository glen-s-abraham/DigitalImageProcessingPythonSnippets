import cv2

img=cv2.imread("1.jpg")

gaussian=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bilateral=cv2.bilateralFilter(img,15,75,75)

cv2.imshow("gaussian",gaussian)
cv2.imshow("median",median)
cv2.imshow("bilateral",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
