import numpy as np
from numpy import prod as a_prod #array_prod
from numpy import pi
from numpy import cos, sin

#only used for testing
import matplotlib.pyplot as plt
from numpy import empty, zeros, eye
from numpy.random import rand

def dct_2(x_vec,k_vec,box=None):
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
    box : {2 mode numpy array}
        square array of shape (dim, dim) defining the simulation box, each row is a vector
    ---Outputs---
    res : {1 mode numpy array}
        values of basis function on points defined in x_vec
    """
    if (x_vec.shape[1] != k_vec.shape[0]):
        print('ERROR: for d>1, x_vec.shape[1] must be equal to k_vec.shape[0]')
        return

    if (box is None):
        box = eye(k_vec.shape[0]) #construct box as identity of proper shape
    elif (len(box.shape) != 2):
        print('ERROR: box must be 2 mode numpy array')
        return
    elif (box.shape[0] != box.shape[1]):
        print('ERROR: box array must be square')
        return

    #perform mapping


    res_array = cos(pi*x_vec*k_vec) #shape (n_points, n_dim)
    #take product of cosine function values of each dimension
    res = a_prod(res_array,axis=-1) #shape (n_points,)
    return res
    
#1-D
points = empty((100,1))
points [:,0] = np.linspace(0,1,100)
wn = np.array([1])
evals = dct_2(points,wn)
#plt.plot(points,evals)
#plt.show()

#2-D
points = rand(1000,2)
wn = np.array([6,1])
evals = dct_2(points,wn)
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_trisurf(points[:,0],points[:,1],evals)
plt.show()

