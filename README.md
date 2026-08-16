
# NGS Quality Control and Analysis of *E. coli* WGS Data

## Overview

This project demonstrates the analysis of publicly available
Illumina whole-genome sequencing data from *Escherichia coli*
using Python, Biopython, Linux command-line tools, and
standard bioinformatics software.

The main goal is to perform quality control and basic
characterization of paired-end FASTQ sequencing data.

## Dataset

- **Organism:** *Escherichia coli*
- **SRA accession:** SRR31439393
- **Platform:** Illumina NextSeq 1000
- **Sequencing strategy:** Whole Genome Sequencing (WGS)
- **Source:** Genomic DNA
- **Layout:** Paired-end
- **Number of spots:** 1,457,207
- **Total bases:** 253.1M
- **Reported GC content:** 50.9%

**Data source:** NCBI Sequence Read Archive (SRA)

## Data Acquisition

The sequencing data were downloaded from NCBI SRA
using the SRA Toolkit.

The accession was downloaded using `prefetch` and
converted from SRA format to paired-end FASTQ files
using `fasterq-dump`.

The downloaded SRA archive was validated using
`vdb-validate`.

## FASTQ Validation

The downloaded FASTQ files were inspected using Linux command-line
tools.

### FASTQ Structure

The first record of `SRR31439393_1.fastq` was inspected using:

```bash
head -n 4 ~/SRR31439393/SRR31439393_1.fastq

## Nucleotide Composition

The nucleotide composition of the R1 FASTQ file was calculated
using Biopython.

The analysis iterated through all 1,457,207 reads and counted
each nucleotide.

The following nucleotide composition was obtained:

| Nucleotide | Count | Percentage |

| A | 30,915,901 | 24.38% |
| C | 32,256,342 | 25.44% |
| G | 32,581,456 | 25.70% |
| T | 30,822,345 | 24.31% |
| N | 210,491 | 0.17% |

The analysis was performed using a streaming approach with
`SeqIO.parse()`, allowing the FASTQ file to be processed
read by read without loading the entire dataset into memory.

## Current Status

- [x] Select public NGS dataset
- [x] Download SRA data
- [x] Validate SRA data
- [x] Convert SRA data to FASTQ
- [ ] Perform FASTQ quality control
- [ ] Analyze Phred quality scores
- [ ] Analyze read length distribution
- [ ] Calculate GC content
- [ ] Perform quality filtering
- [ ] Run FastQC
- [ ] Summarize results
