import cv2

img=cv2.imread("1.jpg",1)
r,g,b=cv2.split(img)

cv2.imshow("Red",r)
cv2.imshow("Green",g)
cv2.imshow("Blue",b)

merged=cv2.merge([r,g,b])
cv2.imshow("RGB",merged)

cv2.waitKey(0)
cv2.destroyAllWindows()