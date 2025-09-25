#!/bin/bash
#SBATCH --job-name=dicom_cpu
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --partition=cpu

module load mpi python/3.10

srun python src/main.py
