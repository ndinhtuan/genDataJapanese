import os
from .getNameFolder import getNameFile
import cv2
import numpy as np

def generateData(srcFolder) :

    listFile, allSubdirs, allShortSubdirs = getNameFile(srcFolder)
    allData = None
    for subDir, label in zip(allSubdirs, allShortSubdirs):

        tmp = generateDataForOneLabel(subDir, int(label))
        if allData is None:
            allData = tmp
            continue
        allData = np.concatenate((allData, tmp), axis=0)

    return allData

def generateDataForOneLabel(subDir, label) :

    os.chdir(subDir)
    allFile = [f for f in os.listdir('.') if os.path.isfile(os.path.join(subDir, f))]
    result = np.empty(len(allFile), dtype=object)

    for i in range(0, len(allFile)):
        tmp = cv2.imread(allFile[i], 0)
        tmp = np.reshape(tmp, tmp.shape[0] * tmp.shape[1])
        tmp = np.array([tmp])
        tmp = np.concatenate((tmp, [[label]]), axis=1)
        result[i] = tmp

    return np.array([i for i in result])
