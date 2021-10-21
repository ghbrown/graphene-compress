import itertools
import numpy as np
from numpy import arange
from numpy import prod as a_prod

def create_dictionaries(k_max_array,coords_u):
    """
    generates a dictionary for each dimension of the data which contains
    wavenumbers up to those in k_max_array
    ---Inputs---
    k_max_array : {numpy array}
        array containing the maximum wavenumbers, shape (n_dim, n_dim),
        k_max_array[i,j] gives the maximum wavenumber in the jth dimension
        for the displacement in dimension i
    coords_u : {numpy array}
        coordinates transformed into unit n-cube, shape (n_points, n_dim)
    ---Outputs---
    dicts : {list}
        list of sparse approximation dictionaries for each dimension,
        dicts[i] is the sparse approximation dictionary of the displacement
        in dimension i
    """

    n_points = coords_u.shape[0]
    n_dim = coords_u.shape[1]
    dicts = []*n_dim
    for i_d,k_max_vec in enumerate(k_max_array): #loop over dimensions
        k_range_array = [arange(elem+1,dtype='f') for elem in k_max_vec]
        k_perm_iterator = itertools.product(*k_range_array) #iterator of tensor
        #product of ranges/rows in k_range_array
        n_perms = a_prod(k_max_vec) #total number of permutations from tensor product

        dict_cur = np.empty((n_points,n_perms))
        for k_vec in k_perm_iterator:
            #add basis evaluations at points with wavenumbers in k_vec
            pass

        dicts[i_d] = dict_cur #insert current dictionary into list
    return dicts


"""
#here is the code you'll need to generate this stuff
>>> import itertools
>>> a = [[1,2,3],[4,5,6],[7,8,9,10]]
>>> list(itertools.product(*a))
[(1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 4, 10), (1, 5, 7), (1, 5, 8), (1, 5, 9), (1, 5, 10), (1, 6, 7), (1, 6, 8), (1, 6, 9), (1, 6, 10), (2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 4, 10), (2, 5, 7), (2, 5, 8), (2, 5, 9), (2, 5, 10), (2, 6, 7), (2, 6, 8), (2, 6, 9), (2, 6, 10), (3, 4, 7), (3, 4, 8), (3, 4, 9), (3, 4, 10), (3, 5, 7), (3, 5, 8), (3, 5, 9), (3, 5, 10), (3, 6, 7), (3, 6, 8), (3, 6, 9), (3, 6, 10)]
"""

"""
import itertools
takes in k_max_array, and transformed pristine coordinates
dicts = []*n_dim
for i_d,k_max_vec in enumerate(k_max_array):
    #example k_max_vec = [3,2]
    # example k_perms = [ [1,1], [1,2], [2,1], [2,2], [3,1], [3,2] ] 
    k_perms = use the code above after generating a range() per element of k_max_vec 
    
    for each permutation in k_perms:
       set a column of dict array to be be basis(pristine,permutation)
    dict = np.empty((n_atoms,prod(k_max_vec)))

return dicts
"""


k_maxes = np.array([[1,2,3],
                    [2,2,2],
                    [4,5,1]])
create_dictionaries(k_maxes,0)




