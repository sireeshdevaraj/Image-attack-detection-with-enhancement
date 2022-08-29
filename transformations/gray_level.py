import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt
import time as t
for image in os.listdir('./not_transformed'):
    img = cv.imread(f'./not_transformed/{image}')
    img_g = cv.imread(f'./not_transformed/{image}',0)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    c_negative = abs(255-img)
    g_negative = abs(255-img_g)
    plt.imshow(img)
    plt.savefig(f'./test_results_of_gray_level/negative_input_image_{image}')
    plt.imshow(c_negative)
    plt.savefig(f'./test_results_of_gray_level/negative_output_image_{image}')
    plt.imshow(img_g, cmap='gray')
    plt.savefig(f'./test_results_of_gray_level/negative_input_gray_scale_{image}')
    plt.imshow(g_negative, cmap='gray')
    plt.savefig(f'./test_results_of_gray_level/negative_output_gray_scale_{image}')
# LOG TRANSFORMATON OCCURS
    c = 255 / np.log(1 + np.max(img))
    log_image = c * (np.log(img + 1))
    log_image = np.array(log_image, dtype = np.uint8)
    plt.imshow(log_image)
    plt.savefig(f'./test_results_of_gray_level/nlog_transformation_{image}')

# POWER LAW TRANSFORMATION
    gamma = 2
    im_res = np.array(255*(img/255)**gamma, dtype = np.uint8)
    plt.imshow(im_res)
    plt.savefig(f'./test_results_of_gray_level/power_law_{image}')
