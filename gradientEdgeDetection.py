import cv2

img=cv2.imread("1.jpg",0)

laplace=cv2.Laplacian(img,cv2.CV_32F)
sobelX=cv2.Sobel(img,cv2.CV_32F,1,0,ksize=5)
sobelY=cv2.Sobel(img,cv2.CV_32F,0,1,ksize=5)

cv2.imshow("Laplacian",laplace)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobelY",sobelY)
cv2.waitKey(0)
cv2.destroyAllWindows()