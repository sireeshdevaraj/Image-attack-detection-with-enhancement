## Detailed explanation about the implementation of Densenet using pytorch

+ Task is to classify the images as live or fake
+ Data inputing:
+ Using torchvision.datasets module from torchvision library we converted raw images of fingerprints into tensors and given as input to the model
+ To achieve faster training of model, by using torch.utils, converted the data into dataloader object.
+ Loss function used is crossEntropyLoss and the optimizer used is stochastic gradient descent.
+ Number of classes involved in classification are 2(live, fake)
+ Number of epochs are taken to be 10.
+ We got an accuracy of 86%
+ Accuracy can be improved by increasing the size of data set and number of epochs
## Some of the output images predcted by the model:
