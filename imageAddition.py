import cv2

img1=cv2.imread("1.jpg",1)
img2=cv2.imread("2.jpg",1)

img2=cv2.resize(img2,img1.shape[0:2])
combined=cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow("Image",combined)
cv2.waitKey(0)
cv2.destroyAllWindows()