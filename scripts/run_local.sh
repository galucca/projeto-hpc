#!/usr/bin/env bash
set -e
echo "Rodando localmente com 4 processos MPI..."
mpirun -np 4 python src/main.py
