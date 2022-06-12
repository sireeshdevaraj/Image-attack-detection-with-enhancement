# FAST FOURIER TRANSFORMATION
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('assets/sample.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('OUTPUT'), plt.xticks([]), plt.yticks([])
plt.show()

#The fast Fourier transform (FFT) is an efficient implementation of DFT and is used, apart from other fields, in digital image processing. FFT is applied to convert an image from the image (spatial) domain to the frequency domain.
#It is the faster version of DFT.