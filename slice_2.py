import cv2
import sys
import os


if not os.path.exists('patches'):
    os.makedirs('patches')



nRows = 8
# Number of columns
mCols = 8

# Reading image
img = cv2.imread('chess1.jpg')
#print img

#cv2.imshow('image',img)

# Dimensions of the image
sizeX = img.shape[1]
sizeY = img.shape[0]



for i in range(0,nRows):
    for j in range(0, mCols):
        roi = img[i*sizeY/nRows:i*sizeY/nRows + sizeY/nRows ,j*sizeX/mCols:j*sizeX/mCols + sizeX/mCols]
        path = '/home/shobhik'
        #cv2.imshow('rois'+str(i)+str(j), roi)
        if(i == 0):
            cv2.imwrite(os.path.join(path , 'a'+str(j+1)+".jpg"), roi)
        if(i == 1):
            cv2.imwrite(os.path.join(path , 'b'+str(j+1)+".jpg"), roi)
        if(i == 2):
            cv2.imwrite(os.path.join(path , 'c'+str(j+1)+".jpg"), roi)
        if(i == 3):
            cv2.imwrite(os.path.join(path , 'd'+str(j+1)+".jpg"), roi)
        if(i == 4):
            cv2.imwrite(os.path.join(path , 'e'+str(j+1)+".jpg"), roi)
        if(i == 5):
            cv2.imwrite(os.path.join(path , 'f'+str(j+1)+".jpg"), roi)
        if(i == 6):
            cv2.imwrite(os.path.join(path , 'g'+str(j+1)+".jpg"), roi)
        if(i == 7):
            cv2.imwrite(os.path.join(path , 'h'+str(j+1)+".jpg"), roi)








cv2.waitKey()
