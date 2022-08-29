import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
for image in os.listdir('./not_transformed'):
    img = cv2.imread(f'./not_transformed/{image}',0) # Load an color image in grayscale
    mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV) #mask returns a Array of two values with threshold value and the the second value is the thresholded image.
    cv2.imwrite(f'./test_results_of_morphological/mask_{image}', mask[1])
    #For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value

    kernal = np.ones((5,5), np.uint8) #Return a new array of given shape and type, filled with ones.
    #(5,5) -- type of array
    # np.uint8 -- datatype of the values in array
    # int8 and unit8 --> unsigned and signed integers

    dilation = cv2.dilate(mask[1], kernal, iterations=2)
    cv2.imwrite(f'./test_results_of_morphological/dilation_{image}', dilation)
    # The first parameter is the original image,
    # kernel is the matrix with which image is convolved and 
    # third parameter is the number of iterations, which will determine how much you want to erode/dilate a given image.
    erosion = cv2.erode(mask[1], kernal, iterations=1)
    cv2.imwrite(f'./test_results_of_morphological/erosion_{image}', erosion)
    opening = cv2.morphologyEx(mask[1], cv2.MORPH_OPEN, kernal)
    cv2.imwrite(f'./test_results_of_morphological/opening_{image}', opening)
    closing = cv2.morphologyEx(mask[1], cv2.MORPH_CLOSE, kernal)
    cv2.imwrite(f'./test_results_of_morphological/closing_{image}', closing)
    morphgradient = cv2.morphologyEx(mask[1], cv2.MORPH_GRADIENT, kernal)
    cv2.imwrite(f'./test_results_of_morphological/morpgradient_{image}', morphgradient)
    tophat = cv2.morphologyEx(mask[1], cv2.MORPH_TOPHAT, kernal)
    cv2.imwrite(f'./test_results_of_morphological/tophat_{image}', tophat)


    #images = [mask[1], dilation, erosion, opening, closing, morphgradient, tophat]
    #for i in images:
    #    print(f"{i}_{image}")
    #    cv2.imwrite(f'./test_results_of_morphological/{i}_{image}', i)