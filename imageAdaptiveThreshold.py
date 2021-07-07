import cv2

img=cv2.imread('1.jpg',0)
#adapitveThreshold(src<img>,threshold_value<int>,method<mean,guassian_mean>,
#threshold_method<bin,bin_inv>,neighbourHoodWidth<int>,neighbourHoodHeight<int>)
thresh = cv2.adaptiveThreshold(img, 200,cv2.ADAPTIVE_THRESH_MEAN_C, 
		 cv2.THRESH_BINARY_INV, 21, 10)
cv2.imshow("Binary",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
