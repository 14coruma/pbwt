#include "PBWT.h"
#include <iostream>
#include <vector>

using namespace std;

// PBWT Constructor
PBWT::PBWT(int length, int count, bool** data, bool ext) {
    m_length = length;
    m_count = count;
    m_ext = ext;

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
    m_pref = new int*[m_count];
    m_div = new int*[m_count];
    if (m_ext) {
        m_u_arr = new int*[m_count+1];
        m_v_arr = new int*[m_count+1];
        m_c = new int[m_length];
    }

    for (int row = 0; row <= m_count; row++) {
        m_pref[row] = new int[m_length+1];
        m_pref[row][0] = row;
        m_div[row] = new int[m_length+1];
        m_div[row][0] = 0;
    }
    if (m_ext) {
        for (int row = 0; row <= m_count; row++) {
            m_u_arr[row] = new int[m_length+1];
            m_u_arr[row][0] = 0;
            m_v_arr[row] = new int[m_length+1];
            m_v_arr[row][0] = 0;
        }
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
        if (m_ext) {
            m_u_arr[i][k] = u;
            m_v_arr[i][k] = v;
        }
        if (data[m_pref[i][k-1]][k-1] == 0) {
            a.push_back(m_pref[i][k-1]);
            d.push_back(p);
            p = 0;
            u++;
        } else {
            b.push_back(m_pref[i][k-1]);
            v++;
            e.push_back(q);
            q = 0;
        }
    }
    if (m_ext) {
        m_c[k-1] = u;
        m_u_arr[m_count][k] = u;
        m_v_arr[m_count][k] = v;
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
