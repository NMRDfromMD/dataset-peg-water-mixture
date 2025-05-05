
import os, time
import numpy as np
import MDAnalysis as mda
from nmrdfrommd import NMRD
import matplotlib.pyplot as plt

from utilities import save_result, get_git_repo_path

git_path = get_git_repo_path()
data_dir = os.path.join(git_path, "data")
topology_file = os.path.join(data_dir, "production.data")
trajectory_file = os.path.join(data_dir, "production.xtc")

u = mda.Universe(topology_file, trajectory_file)
H_PEG = u.select_atoms("type 3 5")
H_H2O = u.select_atoms("type 7")
H_ALL = H_PEG + H_H2O

for n in [5, 20, 80, 320, 1280]:

    ti = time.time()

    nmr_all = NMRD(
        u=u,
        atom_group=H_ALL,
        neighbor_group = H_ALL,
        number_i=n)
    nmr_all.run_analysis()
    save_result(nmr_all, n, f"nmr_all")

    nmr_intra_H2O = NMRD(
        u=u,
        atom_group=H_H2O,
        type_analysis="intra_molecular",
        number_i=n)
    nmr_intra_H2O.run_analysis()
    save_result(nmr_intra_H2O, n, f"nmr_intra_H2O")

    nmr_intra_PEG = NMRD(
        u=u,
        atom_group=H_PEG,
        type_analysis="intra_molecular",
        number_i=n)
    nmr_intra_PEG.run_analysis()
    save_result(nmr_intra_PEG, n, f"nmr_intra_PEG")

    nmr_inter_H2O = NMRD(
        u=u,
        atom_group=H_H2O,
        type_analysis="inter_molecular",
        number_i=n)
    nmr_inter_H2O.run_analysis()
    save_result(nmr_inter_H2O, n, f"nmr_inter_H2O")

    nmr_inter_PEG = NMRD(
        u=u,
        atom_group=H_PEG,
        type_analysis="inter_molecular",
        number_i=n)
    nmr_inter_PEG.run_analysis()
    save_result(nmr_inter_PEG, n, f"nmr_inter_PEG")

    tf = time.time()
    print("time", np.round(tf-ti,1))