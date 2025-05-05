# LAMMPS Input Script
# LAMMPS version: 27Jun2024
# Author: Simon Gravelle
# License: GNU General Public License v3.0
# Project: NMRfromMD – https://nmrdfrommd.github.io
# Description: Parameter file for simulating a PEG-water mixture

# Mass
mass 		6 15.9994 # H2O O
mass 		7 1.008 # H2O H

# Pair Coeff
pair_coeff 	6 6 0.185199 3.1589
pair_coeff 	7 7 0.0 0.0

# Bond coeff
bond_coeff 	6 0 0.9572

# Angle coeff
angle_coeff 9 0 104.52 0 0