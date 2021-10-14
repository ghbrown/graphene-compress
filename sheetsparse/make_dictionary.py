
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
