import numpy as np
from numpy import sum as a_sum #array_sum
from numpy import prod as a_prod #array_prod
from numpy import pi
from numpy import cos, sin

import matplotlib.pyplot as plt

def dct_2(x_vec,k_vec):
    N = x_vec.shape[0] #number of items in array
    k_array = np.tile(k_vec,(N,1))
    res_array = cos(pi*x_vec*k_vec)
    if (len(x_vec.shape) == 2):
        res = a_prod(res_array,axis=1)
    else:
        res = res_array
    return res
    
"""
N = 100
a = np.empty((N,3))
"""
a = np.linspace(0,1,100)
plt.plot(a,dct_2(a,2))
plt.show()

