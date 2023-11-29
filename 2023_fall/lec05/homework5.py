import numpy as np
import matplotlib.pyplot as plt

def center_of_gravity(x):
    n = len(x) - 1
    indices = np.arange(n + 1)
    
    numerator = np.dot(indices, x)
    denominator = np.sum(x)
    
    c = numerator / denominator
    
    return c

def matched_identity(x):
    N = len(x)
    I = np.eye(N)
    return I


def sine_and_cosine(t_start, t_end, t_steps):
    t = np.linspace(t_start, t_end, t_steps)
    x = np.cos(t)
    y = np.sin(t)

    return t, x, y
