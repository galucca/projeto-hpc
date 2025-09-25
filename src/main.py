from mpi4py import MPI
import pydicom
import numpy as np
import os, json, time
from utils import process_dicom

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

DATA_DIR = "data_sample/"
RESULTS_FILE = "results/metrics.json"

def get_dicom_files():
    return [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith(".dcm")]

def main():
    files = get_dicom_files()
    chunk = len(files) // size
    start = rank * chunk
    end = len(files) if rank == size - 1 else (rank + 1) * chunk
    my_files = files[start:end]

    t0 = time.time()
    results = [process_dicom(f) for f in my_files]
    t1 = time.time()

    all_results = comm.gather(results, root=0)

    if rank == 0:
        flat = [r for sub in all_results for r in sub]
        os.makedirs("results", exist_ok=True)
        with open(RESULTS_FILE, "w") as f:
            json.dump(flat, f, indent=2)
        print(f"[MASTER] Processados {len(flat)} arquivos em {t1 - t0:.2f}s")

if __name__ == "__main__":
    main()
