import cv2


	
img=cv2.imread('1.jpg',1)
print(img.shape)
cv2.imshow("Original",img)

img=cv2.resize(img,None,img.size,fx=0.5,fy=0.5)
print(img.shape)
cv2.imshow("Half",img)

img=cv2.resize(img,None,img.size,fx=4,fy=4)
print(img.shape)
cv2.imshow("Double",img)

cv2.waitKey(0)
cv2.destroyAllWindows()