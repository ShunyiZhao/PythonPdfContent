import os

from utils.utils import isTargetType
from utils.utils import isTargetTypeList

class MultiTypesDir(object):

    def __init__(self, currPathName, dirLevel=0, typeList=["pdf"]):
        '''
        The init function of this class
        arguments:
            currPathName(string): 
        '''
        self.currPathName = currPathName
        self.dirLevel = dirLevel
        self.typeList = typeList
        self.dirObjList = []
        self.fileNameList = []

        itemNameList = sorted(os.listdir(currPathName))

        for itemName in itemNameList:
            # ignore some folders
            if itemName == "__pycache__" or itemName == "images" or itemName == ".git" or itemName == "content.pdf":
                continue
            
            absItemPath = os.path.join(self.currPathName, itemName)

            if os.path.isdir(absItemPath) is True:
                self.dirObjList.append(MultiTypesDir(absItemPath, dirLevel=(self.dirLevel+1), typeList=self.typeList))
            elif isTargetTypeList(absItemPath, self.typeList):
                self.fileNameList.append(absItemPath)

    def getCurrDirName(self):
        '''
        print the name of current path
        '''
        return self.currPathName

    def printCurrPdfName(self):
        '''
        print pdf name in curr dir
        '''
        for name in self.fileNameList:
            print(name)

    def printCurrDirObjList(self):
        '''
        print dirs in current dir
        '''
        for name in self.dirObjList:
            print(name.getCurrDirName())

    def buildIterMdContent(self):
        '''
        build a content as markdown
        '''
        strResult = ""
        currName = os.path.split(self.currPathName)[-1]
        for i in range(4 * self.dirLevel):
            strResult += " "
        strResult += "* "
        strResult += currName + "\n"

        # add the pdf names
        for fileName in self.fileNameList:
            name = os.path.split(fileName)[-1]
            name = name.replace("[", "")
            name = name.replace("]", "")
            strTem = ""
            for i in range(4 * (self.dirLevel + 1)):
                strTem += " "
            strTem += "* "
            strTem += '[' + name + ']'
            outputName = fileName.replace('\\', '/')
            #outputName = pdfName.replace(' ', '\ ')
            strTem += '(' + outputName + ')'
            strTem += '\n'
            strResult += strTem

        # add dirs
        for dirObj in self.dirObjList:
            strResult += dirObj.buildIterMdContent()
        return strResult