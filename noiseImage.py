import cv2
import numpy as np

img=cv2.imread('1.jpg')

gauss=np.random.normal(0,1,img.size)
gauss=gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

gaussImage=cv2.add(img,gauss)
speckleImage=img+img*gauss

cv2.imshow("gaussian",gaussImage)
cv2.imshow("speckle",speckleImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
