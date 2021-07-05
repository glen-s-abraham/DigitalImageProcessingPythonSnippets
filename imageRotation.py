import cv2

img=cv2.imread("1.jpg")
rotate90=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.ROTATE_90_COUNTERCLOCKWISE cv2.ROTATE_90_CLOCKWISE cv2.ROTATE_180
cv2.imshow("Original",img)
cv2.imshow("Rotated",rotate90)

cv2.waitKey(0)
cv2.destroyAllWindows()
