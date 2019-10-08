#!/usr/bin/env python3
# Algorithm 2 (BuildPrefixAndDivergenceArrays)

def BuildPrefixAndDivergenceArrays(X, k, pre, div):
    M = len(X)
    u = 0
    v = 0
    p = k+1
    q = k+1
    a = []
    b = []
    d = []
    e = []

    for i in range(0,M):
        if div[i] > p:
            p = div[i]
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

def PreDivArraysWithUV(X, k, pre, div):
    M = len(X)
    u = 0
    v = 0
    p = k+1
    q = k+1
    a = []
    b = []
    d = []
    e = []

    for i in range(0,M):
        if div[i] > p:
            p = div[i]
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
    return (a+b), (d+e), u, v

def DisplayPrefixAndDivergenceArrays(X,k,pre,div):
    text = ''
    for index, match_start in zip(pre,div):
        row = X[index]
        text += str(index) + '|'
        for i,col in enumerate(row[:k+1]):
            if match_start == i:
                text += '\033[4m\033[1m'
            text += str(col)
        if match_start < len(row) - 1:
            text += '\033[0m'
        text += ' '
        for i,col in enumerate(row[k+1:]):
            text += str(col)
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

    pre = range(0,M)
    div = [0] * M 
    for k in range(0,N-1):
        pre,div = BuildPrefixAndDivergenceArrays(X,k,pre,div)
        DisplayPrefixAndDivergenceArrays(X,k,pre,div)
    print(pre)
    print(div)

if __name__ == "__main__":
    main()
