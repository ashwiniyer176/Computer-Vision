import os
from collections import defaultdict
import shutil

SOURCE = "C:/Datasets/Large Scale Fish Dataset/NA_Fish_Dataset"
DESTINATION = "C:/Datasets/Fish Dataset"
RATIO = 0.33


class DataOperations:
    def __init__(self, sourcePath, testRatio=0.25, destinationPath=None):
        '''
        Args:
        destinationPath: Path of the directory where train and test are to be saved.
        sourcePath: Path of the directory where the dataset is saved.
        testRatio: Ratio of test split, by default it is 0.25 test and 0.75 train.
        '''
        self.sourcePath = sourcePath
        self.destinationPath = destinationPath
        self.testRatio = testRatio

    def returnClasses(self):
        if(os.path.exists(self.sourcePath)):
            return os.listdir(self.sourcePath)

    def getOrCreateDestination(self, path):
        if(os.path.exists(path)):
            return path
        else:
            os.mkdir(path)
            return path

    def createSplits(self):
        if(self.destinationPath == None):
            self.destinationPath = self.sourcePath
        if(os.path.exists(self.destinationPath)):
            self.trainPath = self.getOrCreateDestination(
                self.destinationPath+"/train")
            self.testPath = self.getOrCreateDestination(
                self.destinationPath+"/test")
        else:
            self.getOrCreateDestination(self.destinationPath)
            self.trainPath = self.getOrCreateDestination(
                self.destinationPath+"/train")
            self.testPath = self.getOrCreateDestination(
                self.destinationPath+"/test")
            self.moveImages()

    def moveImages(self):
        self.splits = defaultdict(list)
        classes = self.returnClasses()
        for classLabel in classes:
            os.mkdir(self.testPath+"/"+classLabel)
            os.mkdir(self.trainPath+"/"+classLabel)
            images = os.listdir(self.sourcePath+"/"+classLabel)
            numberOfImages = int(self.testRatio*len(images))
            for i in range(numberOfImages):
                self.splits[classLabel].append(images[i])
            print(classLabel, ":", numberOfImages)

        # Copying test images
        for x in self.splits:
            for image in self.splits[x]:
                shutil.copy(self.sourcePath+"/"+x+"/" +
                            image, self.testPath+"/"+x+"/")

        # Copying train images
        for c in classes:
            images = os.listdir(self.sourcePath+"/"+c)
            for img in images:
                if(img not in self.splits[c]):
                    shutil.copy(self.sourcePath+"/"+c+"/" +
                                img, self.trainPath+"/"+c+"/")


if(os.path.exists(DESTINATION)):
    shutil.rmtree(DESTINATION)
g = DataOperations(SOURCE, RATIO, DESTINATION)
g.createSplits()
