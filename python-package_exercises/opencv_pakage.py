import numpy as np
import cv2 as cv
img = cv.imread('img_agri.jpg')
img=cv.resize(img,(300,300))
imggray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thres=cv.threshold(imggray,50,255,0)
contours, hierarchy = cv.findContours(thres, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print("number of contour="+str(len(contour)))
print(contour[0])
cv.drawContours(img,contour,-1,(0,0,255),2)
cv.imshow("image",img)
cv.waitkey(0)
cv.destroyAllWindows()