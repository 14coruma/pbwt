#include "PBWT.h"
#include <iostream>
using namespace std;

// PBWT Constructor
PBWT::PBWT(int length, int count, bool** data) {
    m_length = length;
    m_count = count;

    BuildPrefAndDivArrays(data);
}

void PBWT::BuildPrefAndDivArrays(bool** data) {
    for (int i = 0; i < m_count; i++) {
        for (int j = 0; j < m_length; j++) {
            cout << data[i][j] << ' ';
        }
        cout << endl;
    }
}
