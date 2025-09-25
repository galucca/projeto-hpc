# Projeto HPC — Processamento Paralelo de Imagens DICOM

## Visão geral
Este projeto implementa um pipeline paralelo para processamento de imagens médicas no formato DICOM.  
Operações:
- Anonimização (remoção de metadados sensíveis)
- Compressão (simulada via NumPy)
- Cálculo de estatísticas (dimensões, histograma)

Rodamos localmente (teste) e em cluster (Santos Dumont) usando MPI.

---

## Requisitos
- Python 3.10+ (testado com 3.13)
- Bibliotecas:
  - mpi4py
  - pydicom
  - numpy

Instalação:
```bash
pip install -r env/requirements.txt
```

---

## Como rodar (local)
```bash
bash scripts/build.sh
bash scripts/run_local.sh
```

---

## Como rodar (Santos Dumont)
```bash
sbatch scripts/job_cpu.slurm
# ou
sbatch scripts/job_gpu.slurm
```

---

## Resultados
- Logs e métricas em `results/`
- Gráficos e tabelas no relatório (`report/RELATORIO.pdf`)
"# projeto-hpc" 
