import numpy as np

def fourier_synthesis(num_harmonics, X, T0):
    N = len(X)
    x = np.zeros(N)

    for n in range(N):
        for l in range(1, num_harmonics + 1):
            index = l * N // T0
            amplitude = np.abs(X[index])
            phase = np.angle(X[index])
            x[n] += (2 / N) * amplitude * np.cos(2 * np.pi * l * n / T0 + phase)

    return x
