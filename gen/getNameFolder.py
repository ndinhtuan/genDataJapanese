import os

def getNameFile(src):

    os.chdir(src) # change current location of file
    allSubdirs = [os.path.abspath(d) for d in os.listdir('.') if os.path.isdir(d)] # path.abspath full of src file, lisdir : list directories, isdir : d is directory ?
    allShortSubdirs = [d for d in os.listdir('.') if os.path.isdir(d)] #lisdir('.') list directory in current list, if want to
                                                                    # list in other directory, need to pass full src directory

    listFile = []

    for dirs in allSubdirs :
        os.chdir(dirs)
        allSub = [os.path.abspath(d) for d in os.listdir('.') if os.path.isfile(os.path.join(dirs, d))]
        listFile.append(allSub)

    return listFile, allSubdirs, allShortSubdirs
