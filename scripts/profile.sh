#!/usr/bin/env bash
set -e
/usr/bin/time -v mpirun -np 4 python src/main.py
