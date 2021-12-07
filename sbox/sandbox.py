from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import ase
from ase import io

import sheetsparse as ss
from sheetsparse import map, bases, dictionaries

#construct relative path from full path
#(only since driven by make from another directory)
pristine_file_path = str(Path(__file__).parent) + '/../data/POSCAR_4-4_hex_pristine.txt'
deformed_file_path = str(Path(__file__).parent) + '/../data/POSCAR_4-4_hex_deformed.txt'

#read in pristine and relaxed coordinates
pristine_atoms = ase.io.read(pristine_file_path,format='vasp')
deformed_atoms = ase.io.read(deformed_file_path,format='vasp')

#transform deformed atoms into pristine atoms box
deformed_positions_old = deformed_atoms.get_positions()
deformed_cell_old = deformed_atoms.get_cell()

#get upper layer of pristine coordinates
pristine_positions = pristine_atoms.get_positions()
pristine_mean_z = np.mean(pristine_positions[:,2]) #approximately equal to z of midplane
pristine_upper_sheet = pristine_positions[np.where(pristine_positions[:,2] > pristine_mean_z)]
pristine_upper_sheet_mean_z = np.mean(pristine_upper_sheet[:,2]) #mean z-coordinate of upper plane
pristine_upper_sheet[:,2] -= pristine_upper_sheet_mean_z*np.ones(pristine_upper_sheet.shape[0])
#set pristine upper sheet ot have z values centered about z=0

#get upper layer of deformed coordinates
deformed_positions = deformed_atoms.get_positions()
deformed_mean_z = np.mean(deformed_positions[:,2]) #approximately equal to z of midplane
deformed_upper_sheet = deformed_positions[np.where(deformed_positions[:,2] > deformed_mean_z)]
deformed_upper_sheet_mean_z = np.mean(deformed_upper_sheet[:,2]) #mean z-coordinate of upper plane
deformed_upper_sheet[:,2] -= deformed_upper_sheet_mean_z*np.ones(deformed_upper_sheet.shape[0])
#set deformed upper sheet ot have z values centered about z=0

#correct for fact that pristine and deformed coordinates have slightly
#different boxes by mapping deformed coordinates to pristine box
#(only x and y positions though)
deformed_upper_sheet[:,:2] = ss.map.n_clinic_to_n_clinic(deformed_upper_sheet[:,:2],
                                                         deformed_atoms.get_cell()[:2,:2],
                                                         pristine_atoms.get_cell()[:2,:2])

#create displacement field
disp_field = deformed_upper_sheet - pristine_upper_sheet #vector displacement of each atom

#run represent
#ss.represent(pristine_upper_sheet[:,:2],pristine_atoms.get_cell()[:2,:2],disp_field)
ss.represent(pristine_upper_sheet[:,:2],pristine_atoms.get_cell()[:2,:2],disp_field,
             method='regression')

"""
#plots to show how prisitine and deformed positions roughly align
plt.plot(pristine_upper_sheet[:,0],pristine_upper_sheet[:,1],'ok')
plt.plot(deformed_upper_sheet[:,0],deformed_upper_sheet[:,1],'or')
plt.show()
"""



