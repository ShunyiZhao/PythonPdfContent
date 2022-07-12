import os

from utils.utils import isPdf

class PdfDir(object):

    def __init__(self, currPathName, dirLevel=0):
        '''
        The init function of this class
        arguments:
            dirLevel: the level of this dir
        '''
        self.currPathName = currPathName
        itemNameList = sorted(os.listdir(currPathName))
        self.dirObjList = []
        self.pdfList = []
        self.dirLevel = dirLevel

        for itemName in itemNameList:

            if itemName == "__pycache__" or itemName == "images" or itemName == ".git" or itemName == "content.pdf":
                continue
            
            absItemPath = os.path.join(self.currPathName, itemName)

            if os.path.isdir(absItemPath) is True:
                self.dirObjList.append(PdfDir(absItemPath,dirLevel=(self.dirLevel+1)))
            elif isPdf(absItemPath):
                self.pdfList.append(absItemPath)

    def getCurrDirName(self):
        '''
        print the name of current path
        '''
        return self.currPathName

    def printCurrPdfName(self):
        '''
        print pdf name in curr dir
        '''
        for name in self.pdfList:
            print(name)

    def printCurrDirObjList(self):
        '''
        print dirs in current dir
        '''
        for name in self.dirObjList:
            print(name.getCurrDirName())

    def buildIterContent(self):
        '''
        build the iter content string
        '''
        strResult = ""
        currName = os.path.split(self.currPathName)[-1]
        for i in range(4 * self.dirLevel):
            strResult += " "
        strResult += currName + "\n"

        # add the pdf names
        for pdfName in self.pdfList:
            pdfName = os.path.split(pdfName)[-1]
            strTem = ""
            for i in range(4 * (self.dirLevel + 1)):
                strTem += " "
            strTem += pdfName
            strTem += '\n'
            strResult += strTem

        # add dirs
        for dirObj in self.dirObjList:
            strResult += dirObj.buildIterContent()
        return strResult

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
        for pdfName in self.pdfList:
            name = os.path.split(pdfName)[-1]
            name = name.replace("[", "")
            name = name.replace("]", "")
            strTem = ""
            for i in range(4 * (self.dirLevel + 1)):
                strTem += " "
            strTem += "* "
            strTem += '[' + name + ']'
            outputName = pdfName.replace('\\', '/')
            #outputName = pdfName.replace(' ', '\ ')
            strTem += '(' + outputName + ')'
            strTem += '\n'
            strResult += strTem

        # add dirs
        for dirObj in self.dirObjList:
            strResult += dirObj.buildIterMdContent()
        return strResult