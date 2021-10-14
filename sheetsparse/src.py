
import numpy as np
import ase


#read in generic graphene geometry using ASE

#transform coordinates to unit cell rather or transform basis functions to real space cell
#def dct_basis_fun(x,k,latvecs)
#    evaluates the kth DCT basis function at point(s) x given that the atoms are in a cell with
#    lattice vectors latvecs
"""
given unit cell with basis vectors at angle theta, with unit cell height h
and unit cell length l+h*sin(theta)
positions in the real space cell may be transformed to a square cell with side length h by letting
         /        
    l_1 /         
       / theta    
      /__________ 
       l_2

h = l1/sin(theta)
x_unit = (s/l)*(x_real-y_real*cos(theta))
y_unit = (s/h)*y
"""

#compressors act on objects in standardized format

#result is specified basis and coefficients

#constructor routine takes basis values and (m,n) (to internally construct pristine coordinates) to reconstruct distorted coordinates

#how will order of basis stuff affect things, linearity, convolution, etc.
