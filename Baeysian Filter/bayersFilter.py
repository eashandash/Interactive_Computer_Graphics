import numpy as np
from random import randint
import cv2


img_1 = np.zeros((100,100,3), np.uint8)
img_2 = np.zeros((100,100,3), np.uint8)


img_1[:] = (0,0,0)      
img_2[:] = (0,0,0) 


for i in range(0,100):
    for j in range(0,100):
        if i%2==0:
            if j%2==0 :
                img_1[i][j]= (0,0,randint(0,255))
            else:
                img_1[i][j]= (0,randint(0,255),0)  

        else:
            if j%2==0 :
                img_1[i][j]= (0,randint(0,255),0)
            else:
                img_1[i][j]= (randint(0,255),0,0)  


#Given the size of the image is 100

for i in range(1,99):
    for j in range(1,99):
        
        if i%2==0:
            if j%2==0 :
                red_component = img_1[i][j];
                
                green_component = (img_1[i+1][j] + img_1[i][j-1] + img_1[i][j+1] + img_1[i-1][j])/4

                blue_component = (img_1[i+1][j+1] + img_1[i+1][j-1] + img_1[i-1][j+1] + img_1[i-1][j-1])/4

                img_2[i][j] = blue_component + green_component + red_component
            else:
            	red_component = (img_1[i][j-1] + img_1[i][j+1])/2

                blue_component = (img_1[i+1][j] + img_1[i-1][j])/2;

                green_component = (img_1[i+1][j+1] + img_1[i+1][j-1] + img_1[i-1][j+1] + img_1[i-1][j-1] + img_1[i][j])/5
                
                img_2[i][j] = blue_component + green_component + red_component
        else:
            if j%2==0 :
                red_component = (img_1[i+1][j] + img_1[i-1][j])/2;

                green_component = (img_1[i+1][j+1] + img_1[i+1][j-1] + img_1[i-1][j+1] + img_1[i-1][j-1] + img_1[i][j])/5
                
                blue_component = (img_1[i][j-1] + img_1[i][j+1])/2

                img_2[i][j] = blue_component + green_component + red_component
            else:   
            	red_component = (img_1[i+1][j+1] + img_1[i+1][j-1] + img_1[i-1][j+1] + img_1[i-1][j-1])/4

                green_component = img_1[i][j];
                
                blue_component = (img_1[i+1][j] + img_1[i][j-1] + img_1[i][j+1] + img_1[i-1][j])/4

                img_2[i][j] = blue_component + green_component + red_component             


cv2.imshow('img_1',img_1)
cv2.imshow('img_2',img_2)

