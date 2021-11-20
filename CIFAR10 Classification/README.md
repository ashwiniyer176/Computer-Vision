# Image Classification on RGB Images
Image Classification is a fundamental task that attempts to comprehend an entire image as a whole. The goal is to classify the image by assigning it to a specific label. Typically, Image Classification refers to images in which only one object appears and is analyzed. In contrast, object detection involves both classification and localization tasks, and is used to analyze more realistic cases in which multiple objects may exist in an image. 

## Dataset

The dataset used is the CIFAR10 Image Classification Dataset from PyTorch. The dataset consists of 32x32 RGB images of various class labels. The 10 class labels are:

1. Airplane
2. Automobile
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

## Network Architecture - Convolutional Neural Networks

The network architecture used was a basic CNN model, with Max Pooling and ReLU Activation functions. Input images are resized to an optimal size and then fed into the **Convolutional layer**. These images are converted to their pixel values, which can be imagined as a three-dimensional matrix for the purpose of visualization. The **Convolutional layer** has a kernel. This kernel is generally a small matrix of specified kernel size mxnx3 (3 for RGB images). 
<br>

**Rectified Linear Unit (ReLU)** is the activation layer used in CNNs.The activation function is applied to increase non-linearity in the CNN. Images are made of different objects that are not linear to each other.


**Max Pooling:** A limitation of the feature map output of Convolutional Layers is that they record the precise position of features in the input. This means that small movements in the position of the feature in the input image will result in a different feature map. This can happen with re-cropping, rotation, shifting, and other minor changes to the input image. A common approach to addressing this problem from signal processing is called down sampling. This is where a lower resolution version of an input signal is created that still contains the large or important structural elements, without the fine detail that may not be as useful to the task.

## Future Work

Transfer Learning based approaches using ResNets or AlexNet can be experimented with to see what sort of results are obtained.