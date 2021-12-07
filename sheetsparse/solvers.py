
import numpy as np
from numpy.linalg import norm, lstsq

def regression(dict_list,data):

    d_data = data.shape[1] #dimension of data
    weights_list = [0]*d_data
    for i_d,dict_cur in enumerate(dict_list):
        data_cur = data[:,i_d] #select one dimension of data
        print('dictionary shape:',dict_cur.shape)
        weights_cur,residual = lstsq(dict_cur,data_cur,rcond=None)[:2]
        print(f'cond(dictionary): {np.linalg.cond(dict_cur)}')
        print(f'norm of displacement: {norm(data_cur)}')
        print(f'representation error: {residual[0]}')
        weights_list[i_d] = weights_cur
    return weights_cur

