import os, git
import numpy as np


def get_git_repo_path():
    current_path = os.getcwd()
    repo = git.Repo(current_path, search_parent_directories=True)
    return repo.git.rev_parse("--show-toplevel")

def save_result(data, n, name):
    """Save or update correlation function results into a .npy file."""
    
    # Create directory if it doesn't exist
    output_dir = f"{name}"
    os.makedirs(output_dir, exist_ok=True)
    saving_file = os.path.join(output_dir, f"result{n}.npy")
    
    # Extract relevant data
    t = data["t"]
    f = data["f"]
    C = data.["gij"][0]
    R1 = data["R1"]
    R2 = data["R2"]
    N = data.group_j.atoms.n_atoms
    
    # Save updated data
    result = {
        "t": t,
        "f": f,
        "C": C,
        "N": N,
        "R1": R1,
        "R2": R2
    }
    np.save(saving_file, result)
