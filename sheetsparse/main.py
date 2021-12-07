
import numpy as np
from numpy import eye, ones, empty
from numpy import prod as a_prod
from numpy import round as n_round
from numpy.linalg import norm
from . import map, bases, dictionaries, solvers

import matplotlib.pyplot as plt

def represent(x_array,box,data,k_max=None,method='regression'):
    """
    ---Inputs---
    x_array : {2 mode numpy array}
        array defining the "real" coordinate(s) of points at which data is evaluated
        shape (n_points, d)
        dimension of first mode gives number of points
        dimension of second mode gives number of spatial dimensions (d)
    box : {2 mode numpy array}
        square array of shape (d, d) defining the region in which points x_array live,
            each row is a box vector
    data : {numpy array}
        array of shape (n_points,d_data) where d_data is the dimensionality of the data
            for example d_data is one if the function is a scalar defined on points of
            x_array (like temperature) or d if f_eval represents the evaluation of a
            displacement field on the points of x_array
    TODO: k_max docs
    ---Outputs---
    TODO: determine exactly what output will be, something with coefficients
    """

    d = x_array.shape[1] #dimension in which points live
    d_data = data.shape[1] #dimension of data
    n_points = x_array.shape[0] #number of points

    if (n_points != data.shape[0]):
        print('ERROR: number of positional points and number of data points are not equal')

    if (d != len(box.shape)):
        print('ERROR: dimension of points (x_array.shape[1]) must be equal to dimension of box')

    if (method not in ['NFXT','regression']):
        print('ERROR: method type must be in {\'NFXT\', \'regression\'}')

    I_d = eye(d) #identity matrix of dimension d

    #map data points to unit d-cube
    u_array = map.n_clinic_to_n_clinic(x_array,box,I_d)

    #set maximum wavenumbers
    if (isinstance(k_max,(int,float))): #uniform max wavenumber
        k_max_array = int(k_max)*ones((d_data,d))
    if (k_max is None): #estimate dimension dependent max wavenumbers
        #perform rough estimate of maximum wavenumbers based on uniform point density assumption
        #renders spatially dependent estimates, but no dependence on dimension of data
        k_max_array = empty((d_data,d))
        side_lengths = norm(box,axis=1) #lengths of lattice vectors
        prod_side_lengths = a_prod(side_lengths) #product of side lengths
        for i_d in range(d):
            #estimate how many points lie along each dimension of box
            n_points_d = n_points*(side_lengths[i_d]/prod_side_lengths)
            cur_k_max = n_round(n_points_d).astype(int)
            k_max_array[:,i_d] = cur_k_max*ones(d_data)
    print(k_max_array)

    #solve for basis function coefficients (either by NFFT/NFCT/etc. or regression)
    if (method == 'NFXT'): #use fast X transfrom to compute basis weights
        pass #integrate PyNFFT
    elif (method == 'regression'): #evaluate basis functions and use regression to get weights
        #construct dictionary (from basis functions and estimates of maximum wavenumber)
        dict_list,k_vec_arrays = dictionaries.create_dictionaries(k_max_array,bases.dct_2,u_array)
        solvers.regression(dict_list,data)
        
        



    """
    plt.plot(u_array[:,0],u_array[:,1],'ok')
    plt.show()
    """


    #solve sparse representation problem (one per dimension)
