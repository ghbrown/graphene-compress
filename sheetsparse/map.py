
import numpy as np
from numpy.linalg import inv

#maps coordinates between user/input domain and n-cube
#(where basis functions naturally live) and back

def n_clinic_to_n_clinic(x_array,box,new_box):
    """
    Maps points defined on one n_clinic cell to another n_clinic cell
    ---Inputs---
    x_array : {2 mode numpy array}
        array defining the "real" coordinate(s) of points at which data is evaluated
        shape (n_points, d)
        dimension of first mode gives number of points
        dimension of second mode gives number of spatial dimensions (d)
    box : {2 mode numpy array}
        square array of shape (d, d) defining the region in which points x_array live,
            each row is a box vector
    new_box: {2 mode numpy array}
        square array of shape (d, d) defining the the box to which points of x_array 
            should be mapped
    ---Outputs---
    new_array : {numpy array}
        coordinates x_array transformed into new_box, shape (n_points, d)
    """

    if ((len(box.shape) != 2) or (len(new_box.shape) != 2)):
        print('ERROR: box and new_box must be 2 mode numpy arrays')
        return
    elif ((box.shape[0] != box.shape[1]) and (new_box.shape[0] != new_box.shape[1])):
        print('ERROR: box and new_box arrays must be square')
        return

    # let the columns of V be made of box vectors, and columns of W be made of
    # new_box vectors
    # we then seek the linear transformation L such that
    # L V = W
    # L = W V^{-1}

    #box/new_box variables have cell vectors as rows, above formulation has thema s columns
    V = box.T
    W = new_box.T

    L = W @ np.linalg.inv(V) #linear map from old box vectors to new box vectors

    #transform coordinates
    new_array_transposed = L@(x_array.T) #transform every coordinate into new_box
    new_array = new_array_transposed.T #shape (n_points, n_dim)
    return new_array
    

def n_clinic_to_unit_cube(x_array,box):
    """
    ---Inputs---
    x_array : {2 mode numpy array}
        array defining the "real" coordinate(s) at which to calculate values of
            basis functions
        shape (n_points, d)
        dimension of first mode gives number of points
        dimension of second mode gives number of spatial dimensions (d)
    box : {2 mode numpy array}
        square array of shape (d, d) defining the region in which points x_array live,
            each row is a vector
    ---Outputs---
    u_array : {numpy array}
        coordinates transformed into unit n-cube, shape (n_points, d)
    """

    if (len(box.shape) != 2):
        print('ERROR: box must be 2 mode numpy array')
        return
    elif (box.shape[0] != box.shape[1]):
        print('ERROR: box array must be square')
        return

    # given box vectors in columns of V, let L be the mapping from unit n-cube to box
    # L I = V  --> L = V
    # then L^{-1} maps from "real" box coordinates to the unit n-cube
    # L^{-1} V = I

    V = box.T #box variable has cell vectors stored in rows, above formulation has them as columns of V
    L = V
    L_inv = inv(L)

    #transform coordinates
    u_array_transposed = L_inv@(x_array.T) #transform every coordinate into unit n-cube
    u_array = u_array_transposed.T #shape (n_points, n_dim)
    return u_array



