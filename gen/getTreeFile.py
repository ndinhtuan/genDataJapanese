import os
import os.path

def getTreeFile(nameFolder) :

    os.chdir(nameFolder)
    labels = [i for i in os.listdir('.') if os.path.isdir(i)]

    listPathFiles = []

    for i in labels :

        allFiles = [os.path.join(os.path.abspath(i), f) for f in os.listdir(i) if os.path.isfile(os.path.join(os.path.abspath(i), f))]
        listPathFiles.append(allFiles)

    os.chdir('..')
    return listPathFiles, labels
