# TRANSFORMATIONS AND ENHANCEMENTS

## MORPHOLOGICAL OPERATIONS:
+ Morphology is a broad set of image processing operations that process images based on shapes. Morphological operations apply a structuring element to an input image, creating an output image of the same size
+ Basic Definition: In morphological processing of images, pixels are added or removed from the images
### DILATION:
+ Morphological dilation makes objects more visible and fills in small holes in objects. Lines appear thicker, and filled shapes appear larger.

### EROSION:
+ Morphological erosion removes floating pixels and thin lines so that only substantive objects remain. Remaining lines appear thinner and shapes appear smaller.

### MASK:
+ Image masking is a process of graphics software like Photoshop to hide some portions of an image and to reveal some portions.

### OPENING:
+ The opening operation erodes an image and then dilates the eroded image

### CLOSING:
+ Morphological closing is a dilation followed by an erosion

### GRADIENT:
+  a morphological gradient is the difference between the dilation and the erosion of a given image. It is an image where each pixel value (typically non-negative) indicates the contrast intensity in the close neighborhood of that pixel.

### TOPHAT:
+ A top hat (also known as a white hat) morphological operation is the difference between the original (grayscale/single channel) input image and the opening. opening operation – we do erosion (increase black background) then perform dilation (to regrow original object)

### BASIC THRESHOLDING OPERATIONS WITH CV2
+    cv.THRESH_BINARY
+    cv.THRESH_BINARY_INV
+    cv.THRESH_TRUNC
+    cv.THRESH_TOZERO
+    cv.THRESH_TOZERO_INV


### ADAPTIVE THRESHOLDING
+ we used one global value as a threshold. But this might not be good in all cases, e.g. if an image has different lighting conditions in different areas. In that case, adaptive thresholding can help. Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.

+ In addition to the parameters described above, the method cv.adaptiveThreshold takes three input parameters:

+ The adaptiveMethod decides how the threshold value is calculated:

+ cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
+ cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.

#### Sample Morphological operations performed on a random fingerprint
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/sample.png)
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/Figure_1.png)

## DISCRETE COSINE TRANSFORMATION
+ Discrete Cosine Transform is used in lossy image compression i.e., it's large amount of information is stored in very low frequency component of a signal and rest other frequency having very small data which can be stored by using very less number of bits
### ORIGINAL IMAGE:
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/sample.jpg)
### COMPRESSED IMAGE:
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/dct_capy_compressed.png)
## FAST FOURIER TRANSFORMATION
+ The Fast Fourier Transform (FFT) is commonly used to transform an image between the spatial and frequency domain.
+ FFT fully transforms images into the frequency domain
+ The FFT decomposes an image into sines and cosines of varying amplitudes and phases, which reveals repeating patterns within the image.
+ Low frequencies represent gradual variations in the image; they contain the most information because they determine the overall shape or pattern in the image. High frequencies correspond to abrupt variations in the image; they provide more detail in the image, but they contain more noise.
+  the lowest frequencies are often shown by a large peak in the center of the data.
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/fft_capy.png)

## Histogram equalisation technique
+ In histogram equalisation we distribute the intensities of the pixels such that the image looks brighter if the image is too darker to visualize and the image can be adjusted and can be made darker if it is too brighter to visualize. This can be performed in python by using OpenCV.

### IMAGE TRANSFORMATION:
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/img_before_after_eq.jpg)

### HISTOGRAM BEFORE:
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/hist_before_eq.jpg)

### HISTOGRAM AFTER:
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/hist_after_eq.jpg)


## LOGARITHMIC TRANSFORMATION:
+ During log transformation, the dark pixels in an image are expanded as compare to the higher pixel values. 
+ The higher pixel values are kind of compressed in log transformation.
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/log_before_after.png)

## BLURRING:
+ Blurring is simply blurring the clear image by reducing its edges
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/blurring.png)

## NOISE REDUCTION:
+ Image noise is random variation of brightness or color information in the images captured. It is degradation in image signal caused by external sources.
+ Images containing multiplicative noise have the characteristic that the brighter the area the noisier it.
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/Noise%20reduction.png)

## POWER LAW TRANSFORMATION:
+ This type of transformation is used for enhancing images for different type of display devices.
+ The gamma of different display devices is different.
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/powerlaw.png)

## Image binarization : 
+ Binary images are formed based on the given threshold value
+ The pixel values greater than or equal to the given threshold value are set to 1 i.e. white and rest will be set to 0 i.e. dark
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/Binary.png)

## Image negatives: 
+ Negative of an image can be formed by subtracting each pixel value of input image from L-1
+ L indicates the number of levels in the input image
+ For a 8 bit image the number of pixel values are 256
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/c_negative.png)

## Sharpness and edge detection:
+ Masks and filters can be used to detect edges and enhance the sharpness of image by increasing the edges
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/sharpened_unsharpened.png)
