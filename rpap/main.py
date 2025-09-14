import cv2 as cv
import numpy as np
img=cv.imread("7/cv/rpap/pa.png")
cv.namedWindow("win",cv.WINDOW_NORMAL)
cv.resizeWindow("win", 960,540)
cv.moveWindow("win",0,0)
img2=cv.cvtColor(img,cv.COLOR_BGR2HSV)
w,h=img2.shape[:2]
map1=np.zeros((w,h),np.float32)
map2=np.zeros((w,h),np.float32)
for i in range(w):
    for j in range(h):
        map1[i,j]=h-1-j
        map2[i,j]=w-1-i
while True:
    m=cv.getRotationMatrix2D((680,880),i,0.4)
    imgmv=cv.warpAffine(img2,m,(w,h))
    cv.imshow("win",imgmv)
    if i>360: i=1
    else: i=i+1
    key=cv.waitKey(1)
    if key==27: break
cv.destroyAllWindows()