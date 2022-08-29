import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time as t
import os
for image in os.listdir('./not_transformed'):
    img_1 = cv.imread(f'./not_transformed/{image}')
    img = cv.cvtColor(img_1, cv.COLOR_BGR2RGB)
    avg_blur = cv.blur(img, (10,10))
    plt.imshow(avg_blur)
    plt.savefig(f'./test_results_of_convolution/average_blur_{image}')
    gaus_blur = cv.GaussianBlur(img,(5,5),0)
    plt.imshow(gaus_blur)
    plt.savefig(f'./test_results_of_convolution/gaussian_blur_{image}')
    medBlur = cv.medianBlur(img,7)
    plt.imshow(medBlur)
    plt.savefig(f'./test_results_of_convolution/median_blur_{image}')
    bilateral = cv.bilateralFilter(img,5,6,6)
    plt.imshow(bilateral)
    plt.savefig(f'./test_results_of_convolution/bilateral_filtering_{image}')
    img_new = cv.medianBlur(img,5)
    plt.imshow(img_new)
    plt.savefig(f'./test_results_of_convolution/without_noise_{image}')
    gaus_blur = cv.GaussianBlur(img, (5,5), 0)
    res_img = cv.addWeighted(img, 1.5,gaus_blur ,-0.5, 0)
    plt.imshow(res_img)
    plt.savefig(f'./test_results_of_convolution/after_sharpening_{image}')


