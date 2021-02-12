import numpy as np
import pycuda.autoinit
import pycuda.gpuarray as gpua

import skcuda.linalg as linalg
linalg.init()

# Matrix Inverse
def matrix_inverse(A, cuda = True):
    m, n = A.shape
    transpose = False
    pinv = None
    
#     A is m-by-n and the rank of A is equal to m (m ≤ n) then A has right inverse A_P = At * inv(A * At)
#     A is m-by-n and the rank of A is equal to n (n ≤ m) then A has left inverse A_P = A * inv(At * A)

    if m > n:
        A = np.ascontiguousarray(A.T)
        transpose = True
    # By default this calculates the right inverse
    At = np.ascontiguousarray(A.T)
    if cuda:
        A_gpu = gpua.to_gpu(A)
        At_gpu = gpua.to_gpu(At)

        inv = linalg.inv(linalg.dot(A_gpu, At_gpu))
        pinv = linalg.dot(At_gpu, inv).get()
    else:
        inv = np.linalg.inv(A.dot(At))
        pinv = At.dot(inv)
        
    if transpose:
        pinv = pinv.T
        
    return pinv
