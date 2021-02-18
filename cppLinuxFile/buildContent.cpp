#include<iostream>
#include<fstream>

using std::cout;
using std::cerr;
using std::cin;
using std::endl;

int main(int argc, char **argv){
    if (argc < 2){
        cerr << "You must use this programme with 1 argument or more!" << endl;
        exit(1);
    }

    system("ls");

    return 0;
}