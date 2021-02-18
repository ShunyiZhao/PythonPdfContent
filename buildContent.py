import os
import sys
import markdown2
import pypandoc
from utils import isPdf
from PdfDir import PdfDir

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("You must use this programme with 1 argument!")
        exit(1)

    if sys.argv[1] == "testOri":
        currDir = PdfDir(ROOT_PATH)
        currDir.printCurrPdfName()
        print("*********************************")
        print(currDir.getCurrDirName())
        print("*********************************")
        currDir.printCurrDirObjList()
        print("*********************************")
        print(currDir.buildIterContent())
        print("*********************************")
        mdIterContent = currDir.buildIterMdContent()
        #print(mdIterContent)
        with open("content.md", 'w', encoding='utf-8') as md:
            md.write(mdIterContent)

    if sys.argv[1] == "build":
        currDir = PdfDir(ROOT_PATH)
        mdIterContent = currDir.buildIterMdContent()
        htmlObj = markdown2.markdown(mdIterContent)
        with open("content.html", 'w', encoding='utf-8') as htmlContent:
            htmlContent.write(htmlObj)

    if sys.argv[1] == "buildpdf":
        currDir = PdfDir(ROOT_PATH)
        mdIterContent = currDir.buildIterMdContent()
        with open("content.md", 'w', encoding='utf-8') as md:
            md.write(mdIterContent)

        pypandoc.convert_file("content.md", 'pdf', format="md", outputfile="content.pdf")