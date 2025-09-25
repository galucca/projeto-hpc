🚀 Projeto HPC — Processamento Paralelo de Imagens DICOM
📌 Visão Geral

Este projeto implementa um pipeline paralelo para processamento de imagens médicas no formato DICOM, com foco em alto desempenho e escalabilidade.
O sistema foi projetado para rodar tanto em ambiente local (testes) quanto em clusters de supercomputação como o Santos Dumont (LNCC).

🔧 Operações Implementadas

🔒 Anonimização → remoção de metadados sensíveis (ex.: dados do paciente)

📦 Compressão → simulação via NumPy

📊 Cálculo de estatísticas → dimensões, histogramas e métricas básicas

📂 Estrutura do Projeto
projeto-hpc/
├── data_sample/        # Geração de imagens DICOM de exemplo
├── scripts/            # Scripts de execução (local e cluster)
├── results/            # Saída dos experimentos (logs e métricas)
├── report/             # Relatórios técnicos em PDF
├── src/                # Código-fonte principal
├── env/requirements.txt# Dependências do projeto
└── README.md           # Este arquivo

⚙️ Requisitos

Python ≥ 3.10 (testado com 3.13)

Bibliotecas necessárias:

mpi4py

pydicom

numpy

📦 Instalação das dependências:

pip install -r env/requirements.txt

▶️ Como Executar
🔹 Execução Local (teste em máquina pessoal)
bash scripts/build.sh
bash scripts/run_local.sh

🔹 Execução no Cluster (Santos Dumont - SLURM)

Enviar job para CPU:

sbatch scripts/job_cpu.slurm


Enviar job para GPU:

sbatch scripts/job_gpu.slurm

📊 Resultados

📁 Logs e métricas → results/

📑 Relatório técnico com gráficos, tabelas e análises → report/RELATORIO.pdf

📌 Referências

DICOM Standard

MPI for Python (mpi4py)

Santos Dumont Supercomputer

🔹 Projeto desenvolvido como estudo de Computação de Alto Desempenho (HPC) aplicado à Engenharia Clínica e Saúde Pública.