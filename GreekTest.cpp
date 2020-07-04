#include <iostream>
#include <string>
#include <fstream>
#include "GreekAlphabet.h"

int main()
{
    UseUnicodeInVSCode();
    
    std::string test = Greek::Tau;
    std::cout << test << std::endl;
    std::cout << Greek::lambda <<std::endl;
    std::cout << std::string("2").append(Greek::pi) <<std::endl;
    std::cout<<Greek::mu<<std::endl;

    test+=Greek::tau;
    std::cout<<test<<std::endl;
    std::ofstream fout;
    fout.open(".\\GreekTest.txt");
    fout<<test<<std::endl;
    fout<<Greek::Alpha<<Greek::Beta<<std::endl;
    fout.close();
    return 0;
}