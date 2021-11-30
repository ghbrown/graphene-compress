import numpy as np
from numpy import prod as a_prod #array product
from numpy import pi
from numpy import cos, sin

"""
basis function evaluation routines
"""


def dct_2(u_array,k_vec):
    """
    Returns the evaluation of d-dimensional DCT II basis function on the unit
    d-cube with wavenumber(s) defined by k_vec
    (d is the number of dimensions in which the points of u_array live)
    ---Inputs---
    u_array: {2 mode numpy array}
        coordinates of points (mapped to unit d-cube by linear transformation)
        dimension of first mode gives number of points
        dimension of second mode gives number of spatial dimensions (d)
    k_vec : {1 mode numpy array)
        wavenumbers for each dimension
    ---Outputs---
    res : {1 mode numpy array}
        values of basis function on points defined in u_array
    """
    if (u_array.shape[1] != k_vec.shape[0]):
        print('ERROR: for d>1, u_array.shape[1] must be equal to k_vec.shape[0]')
        return

    res_array = cos(2*pi*u_array*k_vec) #shape (n_points, n_dim)
    #take product of cosine function values of each dimension
    res = a_prod(res_array,axis=-1) #shape (n_points,)
    return res
    
