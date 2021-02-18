#pragma once
#include<iostream>
#include<vector>
#include<string>

using std::vector;
using std::string;

class PdfDir{
private:
    int dirLevel;
    string currDirPath;
    vector<string> vecFolderName;
    vector<string> vecPdfFileName;
public:
    //constructor 
    PdfDir();
    PdfDir(string currDirPath, int dirLevel);

    //get methods
    string getCurrDirPath();
    vector<string> getVecFolderName();
    vector<string> getVecPdfFileName();

    //build content
    string buildMdIterContent();
};