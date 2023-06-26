// taxes.cpp > taxes.zip  ass02
// tax calculator
// calculate tax income of a given ammount based on 1963's
// CS11 Luis Garcia

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double income = 0.0;
    double taxBracket = 0.0;

    cout << "1913 Tax Income Calculator" << endl;
    cout << "For ($)? ";
    cin >> income;

    if (income > 0 && income < 50000) {
        taxBracket += income * 0.01;
    }

    if (income >= 50000 && income < 75000) {
        taxBracket += (50000 - 0) * 0.01 + (income - 50000) * 0.02;
    }

    if (income >= 75000 && income < 100000) {
        taxBracket += (50000 - 0) * 0.01 + (75000 - 50000) * 0.02 + (income - 75000) * 0.03;
    }

    if (income >= 100000 && income < 250000) {
        taxBracket += (50000 - 0) * 0.01 + (75000 - 50000) * 0.02 + (100000 - 75000) * 0.03 + (income - 100000) * 0.04;
    }

    if (income >= 250000 && income < 500000) {
        taxBracket += (50000 - 0) * 0.01 + (75000 - 50000) * 0.02 + (100000 - 75000) * 0.03 + (250000 - 100000) * 0.04 + (income - 250000) * 0.05;
    }

    if (income >= 500000) {
        taxBracket += (50000 - 0) * 0.01 + (75000 - 50000) * 0.02 + (100000 - 75000) * 0.03 + (250000 - 100000) * 0.04 + (500000 - 250000) * 0.05 + (income - 500000) * 0.06;
    }

    cout << "Tax: $" << fixed << setprecision(2) << taxBracket << endl;


    return 0;
}