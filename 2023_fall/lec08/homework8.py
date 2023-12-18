import numpy as np

def dft_matrix(N):

    W = np.zeros((N, N), dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            W[k, n] = np.exp(-2j * np.pi * k * n / N)
    
    return W


