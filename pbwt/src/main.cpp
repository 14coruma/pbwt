#include "PBWT.h"
#include "Data.h"
#include <iostream>

using namespace std;

int main() {
    Data data((char*) "./src/test_data.csv", 6, 8);    
    int length = data.getLength();
    int count = data.getCount();
    bool** data_ptr = data.getDataPtr();
    PBWT pbwt(length, count, data_ptr, true);
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < length; j++) {
            cout << data.getDataVal(i,j) << ' ';
        }
        cout << endl;
    }
    cout << endl;
    // for (int i = 0; i < count; i++) {
        // for (int j = 0; j < length+1; j++) {
            // cout << pbwt.getPrefVal(i,j) << ' ';
        // }
        // cout << endl;
    // }
    // cout << endl;
    // for (int i = 0; i < count+1; i++) {
        // for (int j = 0; j < length+1; j++) {
            // cout << pbwt.getUVal(i,j) << ' ';
        // }
        // cout << endl;
    // }
    // cout << endl;
    // for (int i = 0; i < count+1; i++) {
        // for (int j = 0; j < length+1; j++) {
            // cout << pbwt.getVVal(i,j) << ' ';
        // }
        // cout << endl;
    // }
    // cout << endl;
    // for (int i = 0; i < length; i++) {
        // cout << pbwt.getCVal(i) << ' ';
    // }
    // cout << endl;

    bool query[6] = {1,1,1,0,1,1};
    vector<vector<int> > matches = pbwt.QueryMaximalMatches(query, data_ptr);
   
    cout << "m_c: ";
    for (int i = 0; i < 6; i++) {
        cout << pbwt.getCVal(i) << " ";
    }
    cout << endl;
    cout << "Query: ";
    for (int i = 0; i < 6; i++) {
        cout << query[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < matches.size(); i++) {
       for (int j = 0; j < 3; j++) {
           cout << matches[i][j] << ' ';
       }
       cout << endl;
    }
    return 0;
}
