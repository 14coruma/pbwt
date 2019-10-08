#!/usr/bin/env python3
# Algorithm 4 (ReportSetMaximalMatches)
import alg_2
from operator import itemgetter
from itertools import groupby

# Report set maximal matches in X
def ReportSetMaximalMatches(X, pre_arr, div_arr):
    M = len(X)
    N = len(X[0])

    for k in range(N):
        # Set up 'sentinel' at end of divergence array
        div_arr[k].append(k+1)

        for i in range(M):
            m = i-1
            n = i+1
            match_continues = False

            # Scan down the array
            if div_arr[k][i] <= div_arr[k][i+1]:
                while div_arr[k][m+1] <= div_arr[k][i]:
                    if X[pre_arr[k][m]][k] == X[pre_arr[k][i]][k]:
                        match_continues = True
                        break
                    m = m-1

            if match_continues: # next i
                continue

            if div_arr[k][i] >= div_arr[k][i+1]:
                while div_arr[k][n] <= div_arr[k][i+1]:
                    if X[pre_arr[k][n]][k] == X[pre_arr[k][i]][k]:
                        match_continues = True
                        break
                    n = n+1
            
            if match_continues: # next i
                continue

            for j in range(m+1,i):
                if div_arr[k][i] < k: # Avoid 0 length matches
                    yield pre_arr[k][i], pre_arr[k][j], div_arr[k][i], k
            for j in range(i+1,n):
                if div_arr[k][i+1] < k: # Avoid 0 length matches
                    yield pre_arr[k][i], pre_arr[k][j], div_arr[k][i+1], k

def DisplaySetMaximalMatches(X, matches):
    text = ''
    matches = sorted(matches, key=itemgetter(0,2))
    for i, sub_matches in groupby(matches, key=itemgetter(0)):
        text += "Set maximal matches for row %s:\n" % i
        row_i = X[i]
        text += str(i) + '|' + ''.join(map(str, row_i)) + '\n'
        for _, j, k1, k2 in sub_matches:
            row_j = X[j]
            text += str(j) + '|' + ''.join(map(str, row_j[:k1]))
            text += '\033[4m\033[1m' + ''.join(map(str, row_j[k1:k2])) + '\033[0m'
            text += ''.join(map(str, row_j[k2:])) + '\n'
        text += '\n'
    print(text)

def main():
    X = [[0, 1, 0, 1, 0, 1],
         [1, 1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 0],
         [1, 1, 0, 0, 0, 1],
         [0, 1, 0, 1, 1, 0]]
    M=len(X)
    N=len(X[0])

    # Build all pre and div arrays, storing them in pre_arr, div_arr
    pre_arr = []
    div_arr = []
    pre = range(0,M)
    div = [0] * M 
    pre_arr.append(pre)
    div_arr.append(div)
    for k in range(0,N):
        pre,div = alg_2.BuildPrefixAndDivergenceArrays(X,k,pre,div)
        pre_arr.append(pre)
        div_arr.append(div)
    matches = ReportSetMaximalMatches(X, pre_arr, div_arr)
    DisplaySetMaximalMatches(X, matches)

if __name__ == "__main__":
    main()
