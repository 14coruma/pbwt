#!/usr/bin/env python3
# Algorithm 5 (UpdateZmatches)
import alg_2

# This algorithm doesn't make sense, since u&v are not arrays in algorithm 2

def w(k,i,val,u,v):
    if val == 0:

# Report any set-maximal matches of z to X ending at k and update to (k+1)
def UpdateZmatches(X, z, pre_arr, div_arr, u_arr, v_arr, f, g, e):
    fp = 

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
    u_arr = [0]
    v_arr = [0]
    pre = range(0,M)
    div = [0] * M 
    pre_arr.append(pre)
    div_arr.append(div)
    for k in range(0,N):
        pre,div,u,v = alg_2.PreDivArraysWithUV(X,k,pre,div)
        pre_arr.append(pre)
        div_arr.append(div)
        u_arr.append(u)
        v_arr.append(v)
    f = 0
    g = 0
    e = 0
    (f,g,e) = UpdateZmatches(X, z, pre_arr, div_arr, u_arr, v_arr, f, g, e)
    #for match in matches:
    #    print(match)
    #for i in range(len(X)):
    #    for j in range(len(X[0])):
    #        print(X[i][j], end=' ')
    #    print()

if __name__ == "__main__":
    main()
