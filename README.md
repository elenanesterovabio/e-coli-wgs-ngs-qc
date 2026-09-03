# NGS Quality Control and Analysis of *E. coli* WGS Data

## Overview

This project demonstrates a basic NGS quality-control workflow for
paired-end whole-genome sequencing (WGS) data from *Escherichia coli*.

The project focuses on working with FASTQ sequencing data, performing
custom sequence and quality analysis in Python/Biopython, using standard
NGS quality-control software, and validating paired-end read consistency.

## Dataset

- **Organism:** *Escherichia coli*
- **SRA accession:** SRR31439393
- **Platform:** Illumina NextSeq 1000
- **Sequencing strategy:** Whole Genome Sequencing (WGS)
- **Source:** Genomic DNA
- **Layout:** Paired-end
- **Number of spots:** 1,457,207
- **Reported GC content:** 50.9%
- **Data source:** NCBI Sequence Read Archive (SRA)

The available data consist of deposited FASTQ sequencing reads rather
than raw sequencing-instrument output.

## Workflow

```text
NCBI SRA
   ↓
SRA Toolkit
   ↓
SRA validation
   ↓
Paired-end FASTQ
   ↓
FASTQ structure validation
   ↓
Python / Biopython analysis
   ↓
FastQC analysis of R1 and R2
   ↓
Paired-end read validation
   ↓
QC interpretation
```

## Tools and Technologies

### Data acquisition and processing

- **NCBI Sequence Read Archive (SRA)** — source of the sequencing data
- **SRA Toolkit** — `prefetch`, `fasterq-dump`, and `vdb-validate`
- **Linux / WSL** — command-line data processing and file management

### Sequence analysis

- **Python** — custom FASTQ analysis
- **Biopython** — FASTQ parsing and sequence analysis using `SeqIO`
- **Jupyter Notebook** — interactive analysis and documentation

### Quality control

- **FastQC v0.12.1** — quality assessment of R1 and R2 FASTQ files

### Version control

- **Git**

## Analysis

The custom Python/Biopython analysis includes:

- FASTQ structure inspection
- nucleotide composition
- N-content distribution across read positions
- per-base Phred quality analysis
- read length distribution
- GC content calculation
- paired-end read validation

FastQC was used independently to assess the quality of both R1 and R2
FASTQ files.

The detailed interpretation of the FastQC results is provided in
[`docs/fastqc_analysis.md`](docs/fastqc_analysis.md).

## Filtering and Trimming

No aggressive quality or adapter trimming was performed in this project.

The decision was based on the initial QC assessment and is documented
in the final analysis.

Repository Structure

e-coli-wgs-ngs-qc/
│
├── README.md
│
├── notebooks/
│   └── e-coli-wgs-ngs-qc.ipynb
│
├── scripts/
│   └── e-coli-wgs-ngs-qc.py
│
├── docs/
│   └── fastqc_analysis.md
│
└── results/
    └── fastqc/
        ├── SRR31439393_1_fastqc.html
        ├── SRR31439393_1_fastqc.zip
        ├── SRR31439393_2_fastqc.html
        └── SRR31439393_2_fastqc.zip

## Project Files

### Jupyter Notebook

[`notebooks/e-coli-wgs-ngs-qc.ipynb`](notebooks/e-coli-wgs-ngs-qc.ipynb)

Contains the custom Python/Biopython analysis of the FASTQ data,
including sequence statistics, quality analysis, and paired-end
validation.

### FastQC Analysis

[`docs/fastqc_analysis.md`](docs/fastqc_analysis.md)

Contains the detailed interpretation and comparison of the FastQC
results for R1 and R2.

### FastQC Reports

The original FastQC HTML reports and associated ZIP files are stored in
[`results/fastqc/`](results/fastqc/).

## Reproducibility

The project uses publicly available sequencing data and documents the
main steps of data acquisition, FASTQ processing, quality control, and
analysis.

The repository separates the analysis notebook, QC documentation, and
generated FastQC results to make the workflow easy to follow.