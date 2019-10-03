#!/usr/local/bin/python3
# Algorithm 1 (BuildPrefixArray)

def BuildPrefixArray(X,k, pref):
    M = len(X)
    u = 0
    v = 0
    a = []
    b = []

    for i in range(0,M):
        if X[pref[i]][k] == 0:
            a.append(pref[i]) # Same as a[u] = pref[i]
            u = u + 1
        else:
            b.append(pref[i]) # Same as b[u] = pref[i]
            v = v + 1
    return a + b

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

pref = range(0,M)
for i in range(0,N-1):
    pref = BuildPrefixArray(X,i,pref)
print(pref)
