import numpy as np
from numpy import sum as a_sum #array_sum
from numpy import prod as a_prod #array_prod
from numpy import pi
from numpy import cos, sin
from numpy import empty, zeros

import matplotlib.pyplot as plt

def dct_2(x_vec,k_vec):
    """
    Returns the n-D DCT II basis function with wavenumber(s) defined by 
    k_vec evaluated at point(s) x_vec
    ---Inputs---
    x_vec : {2 mode numpy array}
        array defining the coordinate(s) at which to calculate values of DCTII basis function
        dimension of first mode gives number of points
        dimension of second mode gives number of spatial dimension
    k_vec : {1 mode numpy array)
        wavenumbers for each dimension
    ---Outputs---
    res : {1 mode numpy array}
        values of basis function on points defined in x_vec
    """
    if (x_vec.shape[1] != k_vec.shape[0]):
        print('ERROR: for d>1, x_vec.shape[1] must be equal to k_vec.shape[0]')
        return

    res_array = cos(pi*x_vec*k_vec) #shape (n_points, n_dim)
    #take product of cosine function for each dimension
    res = a_prod(res_array,axis=-1) #shape (n_points,)
    return res
    
points = empty((100,1))
points [:,0] = np.linspace(0,1,100)
wn = np.array([1])
evals = dct_2(points,wn)
plt.plot(points,evals)
plt.show()

