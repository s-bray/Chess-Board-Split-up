import cv2
from matplotlib import pyplot as plt 
import numpy as np 

val = 0
i = 0 
j = 0
k = 0 

for i in range(0,8):
    for j in range (0,8):
        if(i == 0):
            img = cv2.imread('a'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256])
            for k in range(0,256):
                val = val + histr[k]
            #val = val + histr[256]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"a"+str((j+1))+".jpg"+"        "+str(int(val)))
        if(i == 1):
            img = cv2.imread('b'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
 
            for k in range(0,256):
                val = val + histr[k]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"b"+str((j+1))+".jpg"+"        "+str(int(val)))
        if(i == 2):
            img = cv2.imread('c'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
 
            for k in range(0,256):
                val = val + histr[k]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"c"+str((j+1))+".jpg"+"        "+str(int(val)))
        if(i == 3):
            img = cv2.imread('d'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
 
            for k in range(0,256):
                val = val + histr[k]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"d"+str((j+1))+".jpg"+"        "+str(int(val)))
        if(i == 4):
            img = cv2.imread('e'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
 
            for k in range(0,256):
                val = val + histr[k]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"e"+str((j+1))+".jpg"+"        "+str(int(val)))
        if(i == 5):
            img = cv2.imread('f'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
 
            for k in range(0,256):
                val = val + histr[k]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"f"+str((j+1))+".jpg"+"        "+str(int(val)))
        if(i == 6):
            img = cv2.imread('g'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
 
            for k in range(0,256):
                val = val + histr[k]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"g"+str((j+1))+".jpg"+"        "+str(int(val)))
        if(i == 7):
            img = cv2.imread('h'+str(j+1)+'.jpg')
            b,g,r = (img[300, 300])
            histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
 
            for k in range(0,256):
                val = val + histr[k]
            file1 = open("rgb_values.txt","a")
            file1.write("\n"+"h"+str((j+1))+".jpg"+"        "+str(int(val)))

        j = j+1
    i = i+1


cv2.waitKey(0)          
cv2.destroyAllWindows() 
