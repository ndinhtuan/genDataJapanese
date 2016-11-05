from gen.generateImage import genSuperGroupImage, genGroupImage
from gen.getNameFolder import getNameFile
from gen.genData import generateData
import cv2
import numpy as np

#listFile, allSubdirs, allShortSubdirs = getNameFile('imageout')
#print len(allShortSubdirs), len(allShortSubdirs)
#genSuperGroupImage(listFile, allSubdirs)
allData = generateData('imageout')
np.save('data.npy', allData)
