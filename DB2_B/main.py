import os, sys
from PIL import Image

for i in os.listdir("./"):
    if i[-3:] == "tif" or i[-3:] == "bmp" :
       # print "is tif or bmp"
       outfile = i[:-3] + "jpeg"
       im = Image.open(i)
       out = im.convert("RGB")
       out.save(outfile, "JPEG", quality=90)
       os.remove(i) #remove the TIF files ,we don't need them anymore