#include <iostream>
#include <limits>
#include <iomanip>
using namespace std;

double calculateTax(double income) {
    double taxBracket = 0.0;

    if (income > 0 && income < 50000) {
        taxBracket = income * 0.01;
    } else if (income >= 50000 && income < 75000) {
        taxBracket = 50000 * 0.01 + (income - 50000) * 0.02;
    } else if (income >= 75000 && income < 100000) {
        taxBracket = 50000 * 0.01 + 25000 * 0.02 + (income - 75000) * 0.03;
    } else if (income >= 100000 && income < 250000) {
        taxBracket = 50000 * 0.01 + 25000 * 0.02 + 25000 * 0.03 + (income - 100000) * 0.04;
    } else if (income >= 250000 && income < 500000) {
        taxBracket = 50000 * 0.01 + 25000 * 0.02 + 25000 * 0.03 + 150000 * 0.04 + (income - 250000) * 0.05;
    } else if (income >= 500000) {
        taxBracket = 50000 * 0.01 + 25000 * 0.02 + 25000 * 0.03 + 150000 * 0.04 + 250000 * 0.05 + (income - 500000) * 0.06;
    }

    return taxBracket;
}

int main() {
    cout << "1913 Tax Income Calculator" << endl;
    
    while (true) {
        double income = 0.0;

        cout << "Enter income ($): ";
        if (!(cin >> income)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter a valid numeric value." << endl;
            continue;
        }

        if (income < 0) {
            cout << "Income cannot be negative. Please enter a non-negative value." << endl;
            continue;
        }

        double tax = calculateTax(income);
        cout << fixed << setprecision(2);
        cout << "Tax: $" << tax << endl;

        char choice;
        cout << "Do you want to calculate tax for another income? (y/n): ";
        cin >> choice;

        if (choice != 'y' && choice != 'Y') {
            break;
        }
    }

    return 0;
}
