#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include"PdfDir.h"

using std::cout;
using std::endl;
using std::vector;
using std::string;

PdfDir::PdfDir(){
    this -> currDirPath = "";
}

PdfDir::PdfDir(string currDirPathInput, int dirLevelInput){
    currDirPath = currDirPathInput;
    dirLevel = dirLevelInput;
}