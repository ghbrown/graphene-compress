
"""
disp = compute distorted - pristine coordinates #(n_points, n_dim)
transform pristine coordinates to unit interval

k_max_array = empty((n_dim,n_dim))
#k_max_array[i,j] gives the maximum wavenumber in the jth dimension for the displacement in dimension i

for i_d, dim_disp in enumerate(disp.T): #loop over displacement in each dimension
    #k_max_array[i_d,:] = using dim_disp and pristine, get some estimates on the maximum frequency from raw coordinates (in each dimension) for dictionary construction

return k_max_array
"""


