
The required trajectory files are located in the ``data/`` directory.

The trajectory files are stored using Git Large File Storage (Git LFS).
This means that after cloning the repository, you must download the
actual trajectory data before using it.

If Git LFS is not installed, install it first:

git lfs install

Then retrieve the trajectory files:

git lfs pull

Alternatively, you can regenerate the trajectory by rerunning the LAMMPS
simulation scripts provided in the repository.
