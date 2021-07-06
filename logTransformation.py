import cv2
import numpy as np

img=cv2.imread("1.jpg",1)

c=255/np.log(np.max(img))
log_transform=c*np.log(img+1)
log_transform=np.array(log_transform,dtype=np.uint8)
cv2.imshow("Original image",img)
cv2.imshow("Log tranform",log_transform)
cv2.waitKey(0)
cv2.destroyAllWindows()
