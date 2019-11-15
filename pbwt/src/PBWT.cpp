#include "PBWT.h"
#include <iostream>
#include <vector>

using namespace std;

// PBWT Constructor
PBWT::PBWT(int length, int count, bool** data) {
    m_length = length;
    m_count = count;

    BuildPrefAndDiv(data);
}

void PBWT::BuildPrefAndDiv(bool** data) {
    InitPrefAndDiv();
    
    // Iterate over columns, finding Pref and Div at each position
    for (int k = 1; k <= m_length; k++) {
        PBWT::KPrefAndDiv(data, k);
    }
}

void PBWT::InitPrefAndDiv() {
    m_pref = new int*[m_count+1];
    m_div = new int*[m_count+1];

    for (int row = 0; row <= m_count; row++) {
        m_pref[row] = new int[m_length];
        m_pref[row][0] = row;
        m_div[row] = new int[m_length];
        m_div[row][0] = 0;
    }
}

void PBWT::KPrefAndDiv(bool** data, int k) {
    int u = 0, v = 0, p = k, q = k;
    vector<int> a, b, d, e;

    for (int i = 0; i < m_count; i++) {
        if (m_div[i][k-1] > p) {
            p = m_div[i][k-1];
        }
        if (m_div[i][k-1] > q) {
            q = m_div[i][k-1];
        }
        if (data[m_pref[i][k-1]][k-1] == 0) {
            a.push_back(m_pref[i][k-1]);
            u++;
            d.push_back(p);
            p = 0;
        } else {
            b.push_back(m_pref[i][k-1]);
            v++;
            e.push_back(q);
            q = 0;
        }
    }
    for (int i = 0; i < u; i++) {
        m_pref[i][k] = a[i];
        m_div[i][k] = d[i];
    }
    for (int i = 0; i < v; i++) {
        m_pref[u+i][k] = b[i];
        m_div[u+i][k] = e[i];
    }
}
