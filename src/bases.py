import numpy as np
from numpy import prod as a_prod #array_prod
from numpy import pi
from numpy import cos, sin
from numpy.linalg import inv

#only used for testing
import matplotlib.pyplot as plt
from numpy import empty, zeros, eye
from numpy.random import rand

def dct_2(x_array,k_vec,box):
    """
    Returns the evaluation of n-D DCT II basis function (mapped from
    n-cube to box) with wavenumber(s) defined by k_vec
    ---Inputs---
    x_array : {2 mode numpy array}
        array defining the "real" coordinate(s) at which to calculate values of DCT II basis function
        dimension of first mode gives number of points
        dimension of second mode gives number of spatial dimensions
    k_vec : {1 mode numpy array)
        wavenumbers for each dimension
    box : {2 mode numpy array}
        square array of shape (dim, dim) defining the region in which points x_array liv, each row is a vector
    ---Outputs---
    res : {1 mode numpy array}
        values of basis function on points defined in x_array
    """
    if (x_array.shape[1] != k_vec.shape[0]):
        print('ERROR: for d>1, x_array.shape[1] must be equal to k_vec.shape[0]')
        return

    if (box is None):
        box = eye(k_vec.shape[0]) #construct box as identity of proper shape
    elif (len(box.shape) != 2):
        print('ERROR: box must be 2 mode numpy array')
        return
    elif (box.shape[0] != box.shape[1]):
        print('ERROR: box array must be square')
        return

    # given box vectors in columns of V, let L be the mapping from unit n-cube to box
    # L I = V  --> L = V
    # then L^{-1} maps from "real" box coordinates to the unit n-cube
    # L^{-1} V = I
    V = box.T #box vectors stored in rows, above formulation has them as columns of V
    L = V
    L_inv = inv(L)

    #transform coordinates
    x_array_unit_transposed = L_inv@(x_array.T) #transform every coordinate into unit n-cube
    x_array_unit = x_array_unit_transposed.T #shape (n_points, n_dim)

    res_array = cos(2*pi*x_array_unit*k_vec) #shape (n_points, n_dim)
    #take product of cosine function values of each dimension
    res = a_prod(res_array,axis=-1) #shape (n_points,)
    return res
    
#1-D unit interval
dim = 1
points = empty((100,dim))
points [:,0] = np.linspace(0,1,100)
wn = np.array([1])
evals = dct_2(points,wn,np.eye(dim))
#plt.plot(points,evals)
#plt.show()

#2-D unit square
dim = 2
points = rand(1000,dim)
wn = np.array([3,0])
evals = dct_2(points,wn,np.eye(dim))
"""
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_trisurf(points[:,0],points[:,1],evals)
plt.show()
"""

#2-D parallelogram
box_vecs = np.array([[1,0],
                    [1,1]])
points = rand(1000,dim)
points = (box_vecs.T@points.T).T
wn = np.array([3,0])
evals = dct_2(points,wn,box_vecs)
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
X = points[:,0]
Y = points[:,1]
Z = evals
ax.plot_trisurf(X,Y,Z)
#effective axis equal
max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
#effective axis equal
plt.show()
