from gen.getTreeFile import getTreeFile
from gen.genData import genImage
import cv2

#listPathFiles, labels = getTreeFile('imageout')
#tmp = cv2.imread(listPathFiles[0][0], 0)
#genImage(labels, listPathFiles, 700, 'train')
#genImage(labels, listPathFiles, 300, 'test')
img = cv2.imread("/home/tuan/Desktop/Katakana/test/0/image0.png")
if img.data is None:
    print "Cannot read image";
print cv2.BORDER_CONSTANT
print img
