import cv2 as cv
import numpy as np
import time as t
import matplotlib.pyplot as plt
img_in = input("Give an exact path of the input image:")
img = cv.imread(img_in,2)
thres = int(input("enter a threshold value:"))
thres_value, binary = cv.threshold(img,thres,255,cv.THRESH_BINARY)
o_dir = input("enter a directory path to save the processed binary image:") 
plt.imshow(img)
plt.title("given input image")
plt.show()
plt.imshow(binary)
plt.title("processed binary image at a threshold value= "+ str(thres))
plt.savefig(o_dir + 'binary_img.png')
plt.show()
print("Binary image produced successfully")
t.sleep(0.5)
print("processed binary image is stored at the given directory path")
t.sleep(0.5)
