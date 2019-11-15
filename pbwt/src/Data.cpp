#include "Data.h"
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

// Data Constructor
Data::Data(char* filename, int length, int count) {
    m_filename = filename;
    m_length = length;
    m_count = count;
    loadDataFromFile();
}

void Data::loadDataFromFile() {
    m_data = new bool*[m_count];
    ifstream file(m_filename);

    for (int row = 0; row < m_count; row++) {
        string line;
        getline(file, line);
        if (!file.good())
            break;

        stringstream iss(line);

        m_data[row] = new bool[m_length];
        for (int col = 0; col < m_length; ++col) {
            string val;
            getline(iss, val, ',');
            if (!iss.good())
                break;

            stringstream convertor(val);
            convertor >> m_data[row][col];
        }
    }
}
