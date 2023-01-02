#include <iostream>
#include <sstream>
using namespace std;

int main() {
int ba, ru, ga, ya;
cin >> ba >> ru >> ga >> ya;
int rem = (ba % 15) + (ru % 15) + (ga % 15) + (ya % 15);
cout << rem << endl;
	return 0;
}
