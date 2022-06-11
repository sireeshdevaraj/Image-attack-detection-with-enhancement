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




# NOTE:
+ This Readme and Project is still in the initial phase and the initial readme is not completed yet



  
