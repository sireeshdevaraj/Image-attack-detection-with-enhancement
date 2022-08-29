import cv2 as cv
import numpy as np
import time as t
import matplotlib.pyplot as plt
import os
for image in os.listdir('./not_transformed'):
    img = cv.imread(f'./not_transformed/{image}',2)
    thres = 200
    thres_value, binary = cv.threshold(img,thres,255,cv.THRESH_BINARY)
    plt.imshow(binary)
    plt.savefig(f'./test_results_of_binary/{image}')
