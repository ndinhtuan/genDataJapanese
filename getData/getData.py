for gen.getTreeFile import getTreeFile
import cv2
import numpy as np

def getData(nameFile) :

    listPathFiles, labels = getTreeFile(nameFile)
    data = None
    for (label, listFile) in zip(labels, listPathFiles) :
        x = cv2.Canny(cv2.imread(listFile, 0))
        x = x.reshape(1, x.shape[0] * x.shape[1]) * (1.0 / 255)
        x = np.concatenate((x, np.array([[label]])), axis=1)

        if (data is None) :
            data = x
        else :
            data = np.concatenate((data, x), axis=0)

    return data
