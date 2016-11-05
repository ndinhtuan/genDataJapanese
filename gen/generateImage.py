import numpy as np
import cv2

def rotateImage(image, angle, scale):
    row,col = image.shape
    center=tuple(np.array([row,col])/2)
    rot_mat = cv2.getRotationMatrix2D(center,angle, scale)
    tmp = np.zeros((100, 100))
    new_image = cv2.warpAffine(image, rot_mat, (col,row), None, 1, 1, 1)
    return new_image

def genImage(srcImage, h, subDir):

    for i in range(-30, 30):
        for j in [1, 1.01, 1.03, 1.05, 1.07 ]:
            h += 1
            newImage = rotateImage(srcImage, i, j)
            cv2.imwrite(subDir + "/image{}.png".format(h), newImage)
    return h

def genGroupImage(listSrc, subDir) :
    h = 0
    for fileImage in listSrc:
        oldImage = cv2.imread(fileImage, 0)
        h = genImage(oldImage, h, subDir)

def genSuperGroupImage(listSuperGroup, allSubdirs):

    for listGroup, subDir in zip(listSuperGroup, allSubdirs):
        genGroupImage(listGroup, subDir)
