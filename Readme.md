# WORKING WITH NBIS
Download the NBIS  latest release software from the following [link](https://www.nist.gov/itl/iad/image-group/products-and-services/image-group-open-source-server-nigos#Releases) on your UBUNTU


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
+ this will extract all the data from the given set of finger print data sets

# NOTE:
+ This Readme and Project is still in the initial phase and the initial readme is not completed yet



  
