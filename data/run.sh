#!/bin/bash

set -e

# Change accordingly
lmp=/home/simon/Softwares/lammps-27Jun2024/src/lmp_mpi

mpirun -np 8 ${lmp} -in equilibrate.lmp
mpirun -np 8 ${lmp} -in production.lmp
