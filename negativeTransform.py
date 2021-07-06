import cv2

img=cv2.imread("1.jpg",1)
#mathematical tranform L-r
#negative=255-img
#bitwise operation
negative=cv2.bitwise_not(img)

cv2.imshow("Original image",img)
cv2.imshow("Negative tranform",negative)
cv2.waitKey(0)
cv2.destroyAllWindows()