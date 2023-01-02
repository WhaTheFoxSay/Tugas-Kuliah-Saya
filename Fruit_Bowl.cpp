#include <iostream>
using namespace std;

int main() {
    int fruit;
    //take input
    cin>>fruit;

    //your code goes here
    int half;
    half = 2;
    int banana;
    banana = fruit / half;
    int apple;
    apple = fruit - banana;
    int pie;
    pie = 3;
    int make;
    make = apple / pie;
    float sisa;
    sisa = make - apple;
    cout<<make;
    return 0;
}
