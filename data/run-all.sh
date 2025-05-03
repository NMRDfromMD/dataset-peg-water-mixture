#!/bin/bash

set -e

# Change accordingly
lmp=/home/simon/Softwares/lammps-27Jun2024/src/lmp_mpi

for n_peg in 30
do
    folder=nb_peg_${n_peg}/
    cd $folder
        mpirun -np 8 ${lmp} -in equilibrate.lmp
	mpirun -np 8 ${lmp} -in production.lmp
    cd .. 
done
