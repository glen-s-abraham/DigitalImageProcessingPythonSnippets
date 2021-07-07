import cv2
import numpy as np
import matplotlib.pyplot as plt

# THRESH_BINARY
# THRESH_BINARY_INV
# THRESH_MASK
# THRESH_OTSU
# THRESH_TOZERO
# THRESH_TOZERO_INV
# THRESH_TRIANGLE
# THRESH_TRUNC

img=cv2.imread('1.jpg',0)
ret,binThreshold=cv2.threshold(img, 168, 255, cv2.THRESH_TRUNC)
cv2.imshow("Binary",binThreshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
