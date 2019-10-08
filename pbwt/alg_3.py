#!/usr/bin/env python3
# Algorithm 3 (ReportLongMatches)
import alg_2

# Report matches within X ending at K longer than L
def ReportLongMatches(X, k, L, pre_arr, div_arr):
    M = len(X)
    u = 0
    v = 0
    a = [0] * len(X[0])
    b = [0] * len(X[0])

    for i in range(M):
        if div_arr[k][i] > k - L:
            if u > 0 and v > 0:
                yield k, a[0:u], b[0:v]
            u = 0
            v = 0
        if X[pre_arr[k][i]][k] == 0:
            a[u] = pre_arr[k][i] # Same as a[u] = pre[i]
            u = u + 1
        else:
            b[v] = pre_arr[k][i] # Same as b[v] = pre[i]
            v = v + 1
    if u > 0 and v > 0:
        yield k, a[0:u], b[0:v]

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
    L = 4
    for k in range(0,N):
        matches = ReportLongMatches(X, k, L, pre_arr, div_arr)
        print('Matches k={0}, L={1}:'.format(k, L))
        for match in matches:
            print(match)
    for i in range(len(X)):
        for j in range(len(X[0])):
            print(X[i][j], end=' ')
        print()

if __name__ == "__main__":
    main()
