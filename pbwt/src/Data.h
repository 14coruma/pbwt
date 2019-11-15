#ifndef DATA_H
#define DATA_H

using namespace std;

class Data {
    private:
        char* m_filename;
        int m_length;
        int m_count;
        bool** m_data;

        void loadDataFromFile();

    public:
        Data(char* filename, int length, int count);

        char* getFilename() { return m_filename; }
        int getLength() { return m_length; }
        int getCount() { return m_count; }
        bool** getDataPtr() { return m_data; }
        bool getDataVal(int i, int j) { return m_data[i][j]; }
};

#endif
