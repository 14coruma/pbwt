#ifndef PBWT_H
#define PBWT_H

class PBWT {
    private:
        int m_length;
        int m_count;

    public:
        PBWT(int length, int count, bool** data);

        void BuildPrefAndDivArrays(bool** data);

        int getLength() { return m_length; }
        int getCount() { return m_count; }
};

#endif
