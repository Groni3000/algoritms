import random as _
import numpy as np

'''
Type "n" and this script will build a numpy-spiral-matrix with "int32" elements from 1 to n^2.
'''

n=int(input("Type:"))
res=np.ones((n,n), dtype='int32')

for k in range(n//2 + 1):
    for i in range(0+k,n-k):
        if k>1:
            res[0+k][i]=res[0+k][0+k-1]+i-k+1
        elif k==0:
            res[0+k][i]=res[0+k][0]+i-k
        else:
            res[0+k][i]=res[0+k][0]+i-k+1

    for i in range(0+k,n-k):
        res[i][n-1-k]=res[0+k][n-1-k]+i-k

    for i in range(0+k,n-k):
        res[n-1-k][n-1-i]=res[n-1-k][n-1-k]+i-k

    for i in range(0+k+1,n-1-k):
        res[n-1-i][0+k]=res[n-1-k][0+k]+i-k
    k+=1

print(res)