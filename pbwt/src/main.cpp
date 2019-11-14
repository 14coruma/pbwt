#include "PBWT.h"
#include <iostream>

using namespace std;

int main() {
    bool** arr = new bool*[2];
    arr[0] = new bool[2];
    arr[1] = new bool[2];
    arr[0][0] = 1;
    arr[0][1] = 1;
    arr[1][0] = 0;
    arr[1][1] = 0;
    PBWT pbwt(2, 2, arr);
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << pbwt.getPrefVal(i,j) << ' ';
        }
        cout << endl;
    }
    return 0;
}
