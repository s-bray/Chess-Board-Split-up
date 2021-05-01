import cv2
import sys
import os




nRows = 8
# Number of columns
mCols = 8

# Reading image
img = cv2.imread('/home/shobhik/Mini_proj_chess/images/chess.jpg')
#print img

#cv2.imshow('image',img)

# Dimensions of the image
sizeX = img.shape[1]
sizeY = img.shape[0]



for i in range(0,nRows):
    for j in range(0, mCols):
        roi = img[i*sizeY/nRows:i*sizeY/nRows + sizeY/nRows ,j*sizeX/mCols:j*sizeX/mCols + sizeX/mCols]
        
        #cv2.imshow('rois'+str(i)+str(j), roi)
        if(i == 0):
            cv2.imwrite('a'+str(j)+".jpg", roi)
        if(i == 1):
            cv2.imwrite('b'+str(j)+".jpg", roi)
        if(i == 2):
            cv2.imwrite('c'+str(j)+".jpg", roi)
        if(i == 3):
            cv2.imwrite('d'+str(j)+".jpg", roi)
        if(i == 4):
            cv2.imwrite('e'+str(j)+".jpg", roi)
        if(i == 5):
            cv2.imwrite('f'+str(j)+".jpg", roi)
        if(i == 6):
            cv2.imwrite('g'+str(j)+".jpg", roi)
        if(i == 7):
            cv2.imwrite('h'+str(j)+".jpg", roi)








cv2.waitKey()
