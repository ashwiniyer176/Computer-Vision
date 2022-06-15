import os
import sys
import random
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
from shutil import copyfile

annotations = glob('C:/Datasets/BCCD_Dataset/Annotations/*.xml')

df = []
cnt = 0

for file in annotations:
    prev_filename = file.split('/')[-1].split('.')[0] + '.jpg'

    filename = str(cnt) + '.jpg'
    row = []
    parsedXML = ET.parse(file)

    for node in parsedXML.getroot().iter('object'):
        blood_cells = node.find('name').text
        xmin = int(node.find('bndbox/xmin').text)
        xmax = int(node.find('bndbox/xmax').text)
        ymin = int(node.find('bndbox/ymin').text)
        ymax = int(node.find('bndbox/ymax').text)
        row = [prev_filename, filename, blood_cells, xmin, xmax, ymin, ymax]
        df.append(row)
        cnt += 1

data = pd.DataFrame(df, columns=[
                    'prev_filename', 'filename', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax'])
data[['filename', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax']].to_csv(
    'blood_cell_detection.csv', index=False)
