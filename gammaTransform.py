import cv2
import numpy as np

img=cv2.imread("1.jpg",1)
gamma=1.2

#normalize image between 0-1 and apply gamma transform 
gammaCorrection=(img/255)**gamma

#scale back the image into 0-255 and generate an array
gammaCorrection=np.array(255*gammaCorrection,dtype=np.uint8)

cv2.imshow("Original image",img)
cv2.imshow("Gamma tranform",gammaCorrection)
cv2.waitKey(0)
cv2.destroyAllWindows()
