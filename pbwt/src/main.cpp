#include "PBWT.h"
#include <iostream>

using namespace std;

int main() {
    bool** arr = new bool*[2];
    arr[0] = new bool[2];
    arr[1] = new bool[2];
    arr[0][0] = 0;
    arr[0][1] = 0;
    arr[1][0] = 0;
    arr[1][1] = 1;
    PBWT pbwt(2, 2, arr);
    cout << pbwt.getLength() << ' ' << pbwt.getCount() << endl;
    return 0;
}
