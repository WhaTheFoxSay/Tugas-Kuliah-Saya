#include <iostream>
using namespace std;

int main() {
    int point, cost, oleh;
    cin >> point;
    cin >> cost;
    oleh = point / 12;
    if (oleh >= cost) {
        cout << "Buy it!";
    }
    else {
        cout << "Try again";
    }

    return 0;
}
