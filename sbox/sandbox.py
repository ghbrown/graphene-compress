
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import ase
from ase import io

import sheetsparse as ss
from sheetsparse import map, bases, dictionaries


#use path relative to this file
geo_file_path = str(Path(__file__).parent) + '/../data/POSCAR_4-4.txt'
atoms = ase.io.read(geo_file_path,format='vasp') #this read isn't working

#test map
n = 20
d = 2
box_vecs = np.array([[1,0],
                     [1,1]])
                     
rand_points = np.random.rand(*(n,d))
points_orig = ((box_vecs.T)@(rand_points.T)).T
u_out = map.n_clinic_to_unit_cube(points_orig,box_vecs)

x_orig = points_orig[:,0]
y_orig = points_orig[:,1]

plt.plot(x_orig, y_orig,'o')
plt.axis('equal')
plt.show()

x_u = u_out[:,0]
y_u = u_out[:,1]

plt.plot(x_u, y_u,'o')
plt.axis('equal')
plt.show()

#test bases
bases.dct_2(u_out,np.array([0,1]))

#test dictionary
k_max = 20
k_max_array = k_max*np.ones((d,d))
dicts = dictionaries.create_dictionary(k_max_array,bases.dct_2,u_out)
print(len(dicts))
