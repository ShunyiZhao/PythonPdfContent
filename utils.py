import os
import sys

def isPdf(fileName):
    pathSplited = os.path.split(fileName)
    name = pathSplited[-1]
    nameStrs = name.split(".")
    strType = nameStrs[-1]

    return cmpType(strType, "pdf") or cmpType(strType, "PDF")

def cmpType(strFileType, strTargetType):
    if strFileType == strTargetType:
        return True
    
    return False

def isTargetType(strFileName, strTargetType):
    strNameSplited = os.path.split(strFileName)
    strName = strNameSplited[-1]
    strType = strName.split(".")[-1]

    return cmpType(strType, strTargetType)

def isTargetTypeList(strFileName, listTargetType):
    for strTargetType in listTargetType:
        if isTargetType(strFileName, strTargetType):
            return True

    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("This programme must use 2 arguments!")
        exit(1)

    if sys.argv[1] == "testIsPdf":
        assert(isPdf(os.path.join("[3]Semi-supervised", "[2021]MetaPseudoLabels.pdf")) is True)
        assert(isPdf("buildContent.py") is not True)