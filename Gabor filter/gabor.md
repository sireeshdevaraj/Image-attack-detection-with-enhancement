# Gabor Filtering
+ a linear filter used for texture analysis
+  analyzes whether there is any specific frequency content in the image in specific directions in a localized region around the point or region of analysis.
+ We classify textures based on Gabor filter banks. Frequency and orientation representations of the Gabor filter are similar to those of the human visual system.

+ The images are filtered using the real parts of various different Gabor filter kernels. The mean and variance of the filtered images are then used as features for classification, which is based on the least squared error for simplicity.