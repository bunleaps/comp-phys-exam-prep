import random
import numpy as np

N = 1000

A = np.random.rand(N,N)
B = np.random.rand(N,N)

def maxmult(A,B):
  C = np.zeros([N,N] ,float)
  for i in range(N):
    for j in range(N):
      for k in range(N):  
        C[i,j] += A[i,k]*B[k,j]
  return C  

C = maxmult(A,B)

print(C[0][0])
