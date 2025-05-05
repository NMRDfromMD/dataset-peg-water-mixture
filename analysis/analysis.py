#!/usr/bin/env python
# coding: utf-8

import os
import MDAnalysis as mda
from nmrdfrommd import NMRD

from utilities import save_result, get_git_repo_path

git_path = get_git_repo_path()
data_dir = os.path.join(git_path, "data")
topology_file = os.path.join(data_dir, "topology.data")
trajectory_file = os.path.join(data_dir, "dump.xtc")

u = mda.Universe(topology_file, trajectory_file)
all_atoms = u.select_atoms("all")

nmr = NMRD(
    u=u,
    atom_group=all_atoms,
    number_i=1)
nmr.run_analysis()

save_result(nmr, name=f"T{T}")