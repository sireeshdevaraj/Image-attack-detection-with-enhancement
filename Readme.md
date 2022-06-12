# WORKING WITH NBIS
Download the NBIS  latest release software from the following [link](https://www.nist.gov/itl/iad/image-group/products-and-services/image-group-open-source-server-nigos#Releases) on your UBUNTU

It is recommended to have a ubuntu version 20.04 or older. You might experience errors while installing NBIS on ubuntu 22.04 (The latest one).

Open terminal in the the downloaded directory

+ define the setup folder where you want to install the software
+  ` ./setup.sh /home/kuuhaku/Desktop/NBIS_TOOL  --STDLIBS --64`
+ make sure you have the GCC installed before running the setup
+ `sudo apt install gcc-9` 
+ `sudo make config`
+ if you get a error of make is not found then follow my steps
  + first update the sudo apt with sudo apt-get update
  + `sudo apt-get install -y make`
  + `sudo apt install build-essential`
+ `make it`
+ `make install LIBNBIS=yes`

you can check the NBIS_installation_folder, you can find all the required files inside the directory

+ Download the Sample data sets to [test](http://bias.csr.unibo.it/fvc2004/databases.asp)
+ If the Data Sets are in `*.tif` ,you may need to convert these to `*.jpeg`
+ Just a Quick info on **tif** vs **jpeg**
 + TIF means TAG IMAGE FILE FORMAT
 + TIFF files are much larger than JPEGs, but they're also lossless. TIFF files are perfect for images that require big editing jobs in Photoshop or other photo editing software.
+ Convert the TIF files to JPG by running the `main.py` file in the Data Set which can convert all the files at once
+ Extracting Data from given Data sets
+ Copy and place the data set directory inside our `NBIS_INSTALLED_FOLDER`
+ cd into our Dataset `/Desktop/nbis_tool/DB1_B` and run the following shell script `for file in *.jpg; do ../bin/mindtct /home/kuuhaku/Desktop/nbis_tool/DB1_B/"$file" /home/kuuhaku/Desktop/nbis_tool/output/"$file"; done`
+ this will extract all the data from the given set of finger print data sets.
+ You have the Data now and can try to get the match score of two fingerprint data `../bin/bozorth3 -m1 101_2.jpg.xyt 102_6.jpg.xyt`
+ Gives out the score betweent the given two fingerprints!!

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
+ During log transformation, the dark pixels in an image are expanded as compare to the higher pixel values. The higher pixel values are kind of compressed in log transformation.
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/log_before_after.png)

## BLURRING:
+ Blurring is simply blurring the clear image by reducing its edges
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/blurring.png)

## NOISE REDUCTION:
+ Image noise is random variation of brightness or color information in the images captured. It is degradation in image signal caused by external sources.
+ Images containing multiplicative noise have the characteristic that the brighter the area the noisier it.
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/Noise%20reduction.png)

## POWER LAW TRANSFORMATION:
+ This type of transformation is used for enhancing images for different type of display devices. The gamma of different display devices is different.
![](https://github.com/sireeshdevaraj/Image-attack-detection-with-enhancement/blob/master/assets/powerlaw.png)


# NOTE:
+ This Readme and Project ARE still in the initial phase and the readme is not completed yet



  
