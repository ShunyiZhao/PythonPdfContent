import os
import sys
import markdown2
import pypandoc
from utils import isPdf
from PdfDir import PdfDir
from MultiTypesDir import MultiTypesDir

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("You must use this programme with 1 argument!")
        exit(1)

    if len(sys.argv) == 2 and sys.argv[1] == "testOri":
        currDir = PdfDir(ROOT_PATH)
        currDir.printCurrPdfName()
        
        mdIterContent = currDir.buildIterMdContent()
        #print(mdIterContent)
        with open("content.md", 'w', encoding='utf-8') as md:
            md.write(mdIterContent)

    if len(sys.argv) == 2 and sys.argv[1] == "build":
        currDir = PdfDir(ROOT_PATH)
        mdIterContent = currDir.buildIterMdContent()
        htmlObj = markdown2.markdown(mdIterContent)
        with open("content.html", 'w', encoding='utf-8') as htmlContent:
            htmlContent.write(htmlObj)

    if len(sys.argv) == 2 and sys.argv[1] == "buildpdf":
        currDir = PdfDir(ROOT_PATH)
        mdIterContent = currDir.buildIterMdContent()
        with open("content.md", 'w', encoding='utf-8') as md:
            md.write(mdIterContent)

        pypandoc.convert_file("content.md", 'pdf', format="md", outputfile="content.pdf", extra_args=['-V', 'geometry:margin=1.5cm'])

    if len(sys.argv) > 2 and sys.argv[1] == "buildMultiContent":
        typeList = sys.argv[2:]
        print(typeList)

        currDir = MultiTypesDir(ROOT_PATH, dirLevel=0, typeList=typeList)
        mdIterContent = currDir.buildIterMdContent()
        
        with open("content.md", 'w', encoding='utf-8') as md:
            md.write(mdIterContent)

        pypandoc.convert_file("content.md", 'pdf', format="md", outputfile="content.pdf", extra_args=['-V', 'geometry:margin=1.5cm'])