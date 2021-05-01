from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import cv2
import numpy as np

val = 0
vec = 0
i = 0 
j = 0
k = 0
l = 0 

for i in range(0,8):
    for j in range (0,8):
        if(i == 0):
            img = imread('a'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_a'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"a"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0

        if(i == 1):
            img = imread('b'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_b'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"b"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0

        if(i == 2):
            img = imread('c'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_c'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"c"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0

        if(i == 3):
            img = imread('d'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_d'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"d"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0

        if(i == 4):
            img = imread('e'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_e'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"e"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0

        if(i == 5):
            img = imread('f'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_f'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"f"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0

        if(i == 6):
            img = imread('g'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_g'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"g"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0
        if(i == 7):
            img = imread('h'+str(j+1)+'.jpg')
            fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2,2),visualize=True,multichannel=True)
            plt.imsave('hog_image'+'_h'+str(j+1)+'.jpg', hog_image, cmap="gray")
            #print(fd)

            for k in range(0,len(fd)):
                vec = vec + (fd[k]*fd[k])
            vec = (vec**(0.5))
            print(vec)
            file1 = open("val_1.txt","a")
            file1.write("\n"+"h"+str((j+1))+".jpg"+"        "+str(int(vec)))
            #for l in range(0,len(fd)):
            #   val = val + ((fd[l])/(vec))
            #print(val)
            #val = 0
            #vec = 0

        j = j+1
    i = i+1


cv2.waitKey(0)          
cv2.destroyAllWindows() 

