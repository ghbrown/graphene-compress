import itertools
import numpy as np
from numpy import arange, array, ones, unique
from numpy import prod as a_prod


def create_dictionary(k_max_array,basis_function,u_array):
    #TODO: add support for non-tensor product spaces/cubes using
    #      "Multidimensional pseudo-spectral methods on lattice grids"
    """
    generates a dictionary for each dimension of the data
    each dictionary has as it's columns the basis function evaluated
    one points in unit d-cube for some collection of k_vectors
    ---Inputs---
    k_max_array : {numpy array}
        array containing the maximum wavenumbers, shape (d, d_data),
            d_data could be 1 for scalar functions, or d for vector valued
            functions
        k_max_array[i,j] gives the maximum wavenumber in the jth dimension
            for the ith component of the data
    basis_function : {function pointer}
        function 
    u_array : {numpy array}
        coordinates transformed into unit n-cube, shape (n_points, d)
    ---Outputs---
    dicts : {list}
        list of sparse approximation dictionaries for each dimension of  data
        dicts[i] is the sparse approximation dictionary of the data in
            dimension i
    """

    if (unique(k_max_array).shape[0] = 1):
        pass #you can save som computation when k_max_array has a single value
        #since all the dictionaries will be the same
        

    n_points = u_array.shape[0]
    d = u_array.shape[1] #number of dimensions of points
    d_data = k_max_array.shape[0] #number of dimensions of data
    dicts = [0]*d_data #one dictionary per dimension of data
    for i_d,k_max_vec in enumerate(k_max_array): #loop over dimensions
        k_range_array = [arange(elem+1,dtype='f') for elem in k_max_vec]
        k_perm_iterator = itertools.product(*k_range_array) #iterator of tensor
        #product of ranges/rows in k_range_array
        n_perms = a_prod(k_max_vec+ones(d)).astype(int) #total number of permutations from tensor product

        dict_cur = np.empty((n_points,n_perms))
        for i_k,k_vec in enumerate(k_perm_iterator): #loop over k_vectors
            dict_cur[:,i_k] = basis_function(u_array,array(list(k_vec))) #basis(k_vec) at all points

        dicts[i_d] = dict_cur #insert current dictionary into list
    return dicts


