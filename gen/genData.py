import cv2
import numpy as np
import random as rd
import os

def genOneImage(srcImage, angle, scale, transX, transY, dstSave, name):

    imgSrc = cv2.imread(srcImage, 0)
    row,col = imgSrc.shape
    center = tuple(np.array([row,col])/2)
    matAngle = cv2.getRotationMatrix2D(center, angle, scale)
    dstAngle = cv2.warpAffine(imgSrc, matAngle, (col, row), None, 1, 1, 1)

    matTrans = np.float32([[1, 0, transX], [0, 1, transY]])
    dstTrans = cv2.warpAffine(dstAngle, matTrans, dstAngle.shape, None, 1, 1, 1)

    imgDst = cv2.resize(dstTrans, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(dstSave + "/image{}.png".format(name), imgDst)

def genImage(labels, listPathFiles, numImages, fileLocation) :

    angle = [i for i in range(-15, 15)]
    scale = [i for i in range(80, 120)]
    tmp = cv2.imread(listPathFiles[0][0], 0)
    print tmp.shape
    transX = [i for i in range(-int(tmp.shape[0] / 6), int(tmp.shape[0] / 6))]
    transY = [i for i in range(-int(tmp.shape[1] / 6), int(tmp.shape[1] / 6))]

    if not os.path.exists(fileLocation):
        os.makedirs(fileLocation)

    os.chdir(fileLocation)
    for (label, listFile) in zip(labels, listPathFiles):

        if not os.path.exists(label):
            os.makedirs(label)
        paraDstSave = os.path.abspath(label)

        h = 0
        for _file in listFile :

            for i in range(numImages) :
                paraAngle = rd.choice(angle)
                paraScale = rd.choice(scale) / 100.0
                paraTransX = rd.choice(transX)
                paraTransY = rd.choice(transY)
                genOneImage(_file, paraAngle, paraScale, paraTransX, paraTransY, paraDstSave, i + h)
            h += numImages

    os.chdir('..')
