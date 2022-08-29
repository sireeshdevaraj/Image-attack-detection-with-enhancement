import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt
for image in os.listdir('./not_transformed'):
    img = cv.imread(f'./not_transformed/{image}',0)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    output = 20*np.log(np.abs(fshift))
    cv.imwrite(f'./test_results_of_fft/{image}', output)
    #plt.subplot(122),plt.imshow(output, cmap = 'gray')
