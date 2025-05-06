import numpy as np
import MDAnalysis as mda
from nmrdfrommd import NMRD

datapath = "../data/"

u = mda.Universe(datapath+"production.data",
                 datapath+"production.xtc")

n_TOT = u.atoms.n_residues
n_H2O = u.select_atoms("type 6 7").n_residues
n_PEG = u.select_atoms("type 1 2 3 4 5").n_residues
print(f"The total number of molecules is {n_TOT} ({n_H2O} H2O, {n_PEG} PEG)")

timestep = np.int32(u.trajectory.dt)
total_time = np.int32(u.trajectory.totaltime)

print(f"The timestep is {timestep} ps")
print(f"The total simulation time is {total_time//1000} ns")

H_PEG = u.select_atoms("type 3 5")
H_H2O = u.select_atoms("type 7")
H_ALL = H_PEG + H_H2O

nmr_all = NMRD(
    u=u,
    atom_group=H_ALL,
    neighbor_group = H_ALL,
    number_i=40)
nmr_all.run_analysis()

T1 = np.round(nmr_all.T1, 2)

print(f"The NMR relaxation time is T1 = {T1} s")