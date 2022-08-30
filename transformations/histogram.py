import numpy as np
import cv2 as cv
import time
import os
from matplotlib import pyplot as plt
for image in os.listdir('./not_transformed'):
    img = cv.imread(f'./not_transformed/{image}',0)
    equ = cv.equalizeHist(img)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.savefig(f'./test_results_of_histogram/{image}')
	