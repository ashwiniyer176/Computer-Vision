# Detecting Alzheimer's from MRI Scans
Alzheimer's disease is a progressive neurologic disorder that causes the brain to shrink (atrophy) and brain cells to die. Alzheimer's disease is the most common cause of dementia — a continuous decline in thinking, behavioral and social skills that affects a person's ability to function independently. The early signs of the disease include forgetting recent events or conversations. As the disease progresses, a person with Alzheimer's disease will develop severe memory impairment and lose the ability to carry out everyday tasks. The objective is to detect the various levels of Alzheimer's present in a patient using MRI scans. The model thus predicts the stage at which the patient is.

## Dataset

The dataset used is the [Alzheimer's Dataset (4 Class of Images)](https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images) from Kaggle. The 4 class labels are:

1.**Mild Demented**

2.**Moderate Demented**

3.**Non Demented**

4.**Very Mild Demented**


## Network Architecture - Convolutional Neural Networks

The network architecture used was a basic CNN model, with Max Pooling and ReLU Activation functions. The loss function, Cross Entropy, was provided with weights as the dataset used is an imbalanced one.

## Future Work

Transfer Learning based approaches using ResNets or AlexNet can be experimented with to see what sort of results are obtained.