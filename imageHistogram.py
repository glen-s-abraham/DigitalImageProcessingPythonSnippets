import cv2
import matplotlib.pyplot as plt

img=cv2.imread("1.jpg",0)

#histogram=cv2.calcHist(img,[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
#plt.plot(histogram)
plt.show()