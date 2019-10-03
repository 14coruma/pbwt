#!/usr/local/bin/python3
# Algorithm 3 (ReportLongMatches)

# Report matches within X ending at K longer than L
def ReportLongMatches(X, k, L, pre_arr, div_arr):
    M = len(X)
    u = 0
    v = 0
    a = []
    b = []

    for i in range(0,M):
        if div[i] > k - L:
            if u > 0 and v > 0:
..........
        if div[i] > q:
            q = div[i]
        if X[pre[i]][k] == 0:
            a.append(pre[i]) # Same as a[u] = pre[i]
            d.append(p) # Same as d[u] = p
            u = u + 1
            p = 0
        else:
            b.append(pre[i]) # Same as b[v] = pre[i]
            e.append(q) # Same as e[v] = q
            v = v + 1
            q = 0
    return (a+b), (d+e)

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
for k in range(0,N-1):
    pre,div = BuildPrefixAndDivergenceArrays(X,k,pre,div)
    pre_arr.append(pre)
    div_arr.append(div)
RepportLongMatches(X, k, L, pre_arr, div_arr)
