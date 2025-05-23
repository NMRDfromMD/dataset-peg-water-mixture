"""This Python script creates a box of PEG and water molecules"""

import numpy as np

from utilities import PEGgenerator, place_molecules, write_topol, write_conf, write_lammps, prepare_lammps

# fix the number of polymer
Number_polymer = 30
EOperH2O = 0.5
Nseg = 5

atomsPEG, bondsPEG, anglesPEG, dihedralsPEG = PEGgenerator(Nseg)

# Estimate and print the molar mass
nC = np.sum(atomsPEG.T[1] == 1) # number of carbon per Peg
nO = np.sum((atomsPEG.T[1] == 2) | (atomsPEG.T[1] == 4)) # number of oxygen per Peg
nH = np.sum((atomsPEG.T[1] == 3) | (atomsPEG.T[1] == 5)) # number of hydrogen per Peg
molarmass = nC*12+nO*16+nH*1
print('PEG of molar mass '+str(molarmass)+' g/mol')
Number_water = np.int32(nO*Number_polymer/EOperH2O)
print('The total number of water molecules is '+str(Number_water))
print('The total number of PEG molecules is '+str(Number_polymer))

print('The total number of H-PEG is '+str(nH*Number_polymer))
print('The total number of H-H2O is '+str(2*Number_water))

# Create the GROMACS files
atoms, bonds, angles, dihedrals, atoName, resName, Lx, Ly, Lz = place_molecules(Number_polymer, Number_water, atomsPEG, bondsPEG, anglesPEG, dihedralsPEG)
# write_topol(Number_polymer, Number_water)
# write_conf(atoms, atoName, resName, Lx, Ly, Lz)

print('The total number of atoms is', str(len(atoms)))

# Convert to LAMMPS
atoms, bonds, angles, dihedrals = prepare_lammps(atoms, bonds, angles, dihedrals)
write_lammps(atoms, bonds, angles, dihedrals, Lx, Ly, Lz)
