import numpy as np
from numpy import empty, array, eye
from numpy import linspace
from numpy.random import rand
import matplotlib.pyplot as plt

import sheetsparse as ss
from sheetsparse import map, bases
from sheetsparse.map import n_clinic_to_unit_cube
from sheetsparse.bases import dct_2

#1-D unit interval
dim = 1 #number of spatial dimensions
points = empty((100,dim))
x_max = 6
points [:,0] = linspace(0,x_max,100)
u_points =  n_clinic_to_unit_cube(points,x_max*np.eye(dim)) #points on unit interval
wn = array([1]) #wavenumber
evals = dct_2(points,wn) #function values on u_points of a single dct_2 mode wn
plt.plot(points,evals,'k',label=(r'$k_x =' + str(wn[0]) + r'$'))
plt.xlabel(r'$x$')
plt.ylabel(r'$\cos(2 \pi k_x x)$')
plt.legend()
plt.show()

"""
surfcolor = 'brown' #set color of trisurf plots
#2-D unit square
dim = 2
points = rand(1000,dim)
wn = array([3,0])
evals = dct_2(points,wn,eye(dim))
X = points[:,0]
Y = points[:,1]
Z = evals
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_trisurf(X,Y,Z,color=surfcolor)
#effective axis equal
max_range = array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
#effective axis equal
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_zlabel(r'$\cos(2 \pi k_1 (\mathbf{L}^{-1}\mathbf{x})_1) \cos(2 \pi k_2 (\mathbf{L}^{-1}\mathbf{x})_2)$')
plt.title('basis: [1,0],[0,1]')
plt.show()

#2-D parallelogram
box_vecs = np.array([[1,0],
                    [1,1]])
points = rand(1000,dim)
points = (box_vecs.T@points.T).T
wn = array([3,0])
evals = dct_2(points,wn,box_vecs)
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
X = points[:,0]
Y = points[:,1]
Z = evals
ax.plot_trisurf(X,Y,Z,color=surfcolor)
#effective axis equal
max_range = array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
#effective axis equal
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_zlabel(r'$\cos(2 \pi k_1 (\mathbf{L}^{-1}\mathbf{x})_1) \cos(2 \pi k_2 (\mathbf{L}^{-1}\mathbf{x})_2)$')
plt.title('basis: [1,0],[1,1]')
plt.show()
"""
