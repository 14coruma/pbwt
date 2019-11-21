#ifndef PBWT_H
#define PBWT_H

#include <vector>

using namespace std;

class PBWT {
    private:
        int m_length;
        int m_count;
        int** m_pref;
        int** m_div; 

        bool m_ext;
        int** m_u_arr;
        int** m_v_arr;
        int* m_c;

        void BuildPrefAndDiv(bool** data);
        void KPrefAndDiv(bool** data, int k);
        void InitPrefAndDiv();
        int IdxDest(int idx, bool val, int k); // w(i,bool) in the paper
        void KQueryMatches(bool* query, int k, bool** data,
                vector<vector<int> >& matches, int& f, int& g, int& e);

    public:
        PBWT(int length, int count, bool** data, bool ext);
        vector<vector<int> > QueryMaximalMatches(bool* query, bool** data);

        int getLength() { return m_length; }
        int getCount() { return m_count; }
        int getPrefVal(int i, int j) { return m_pref[i][j]; }
        int getDivVal(int i, int j) { return m_div[i][j]; }
        int getUVal(int i, int j) { return m_u_arr[i][j]; }
        int getVVal(int i, int j) { return m_v_arr[i][j]; }
        int getCVal(int i) { return m_c[i]; }

};

#endif
