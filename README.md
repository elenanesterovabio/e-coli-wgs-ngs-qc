
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

test
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
