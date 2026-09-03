# FastQC Analysis

FastQC v0.12.1 was used to assess the quality of the paired-end FASTQ
files SRR31439393_1.fastq (R1) and SRR31439393_2.fastq (R2).

The detailed analysis below summarizes the FastQC results for both
paired-end reads and compares the main QC metrics.

---

## R1

### Basic Statistics

- Number of reads: 1,457,207
- Total bases: 126.7 Mb
- Read length: 35–99 bp
- GC content: 51%

### Per-base sequence quality — PASS

Phred quality remained high across read positions, with no pronounced
decline toward the end of the reads.

The per-base Phred quality distribution was calculated using all
available reads and observed read positions. No quality or length
filtering was applied before this analysis.

### Per-tile sequence quality — FAIL

FastQC detected localized quality variation associated with specific
sequencing tiles. This indicates localized variation in sequencing
quality rather than globally poor read quality.

### Per-base sequence content — FAIL

A pronounced nucleotide composition bias was observed during
approximately the first 20 bp of the reads. After this region,
nucleotide frequencies stabilized at approximately 25% for each base.

### Per-sequence GC content — WARN

The observed GC distribution showed some deviation from the theoretical
distribution. The overall GC content was approximately 51%, consistent
with the independently calculated GC content of 51.22%.

### Per-base N content — PASS

N bases represented only 0.17% of all bases. Several localized
positional peaks were observed, but the overall N content remained low.

### Sequence Length Distribution — WARN

Read lengths ranged from 35 to 99 bp. The majority of reads were
98–99 bp long, while a smaller fraction of reads had shorter lengths.

The shorter reads were retained because the available QC results did
not provide sufficient evidence that length-based filtering was required.

### Adapter Content — PASS

No significant adapter contamination was detected.

### Overrepresented Sequences — PASS

No overrepresented sequences were detected.

### Sequence Duplication Levels — PASS

77.56% of sequences would remain after deduplication. Most sequences
occurred only once or a small number of times, while extreme duplication
levels were rare. No major duplication problem was identified.

---

## R2

### Basic Statistics

- Number of reads: 1,457,207
- Total bases: 126.3 Mb
- Read length: 35–99 bp
- GC content: 51%

### Per-base sequence quality — PASS

Median Phred quality remained high across the read positions, generally
around Q31–32. Several positions showed wider quality distributions,
but there was no general decline toward low-quality scores at the end
of the reads.

### Per-tile sequence quality — FAIL

FastQC detected localized quality variation across sequencing tiles.
The deviations were more pronounced in R2 than in R1, but most tiles
remained close to the overall quality level.

### Per-base sequence content — FAIL

R2 showed a pronounced nucleotide composition bias during approximately
the first 20 bp of the reads. After this region, nucleotide frequencies
stabilized at approximately 25% for each base.

A similar positional bias was observed in R1, indicating that this
pattern is present in both paired-end reads.

### Per-sequence GC content — WARN

The observed GC distribution differed from the theoretical distribution,
with a pronounced peak around 52–54% GC. The overall GC content was
approximately 51%.

The R2 distribution showed a noticeable deviation from the theoretical
distribution, but no large population of reads with extreme GC content
was observed.

### Per-base N content — PASS

N content remained very low across the R2 reads. Small localized peaks
were observed at several positions, with the largest peak around 4%,
but the overall N content remained low.

The R2 profile was consistent with the R1 result, which also showed very
low overall N content.

### Sequence Length Distribution — WARN

R2 reads ranged from 35 to 99 bp. The vast majority of reads were
98–99 bp long, while a smaller fraction of reads had shorter lengths.

A similar length distribution was observed in R1. The presence of
shorter reads was documented but was not considered sufficient evidence
for length-based filtering at this stage.

### Sequence Duplication Levels — PASS

81.94% of R2 sequences would remain after deduplication, indicating a
lower duplication level than in R1 (77.56%).

Most sequences occurred only once or a small number of times, while
extreme duplication levels were rare. No major duplication problem was
identified by FastQC.

### Overrepresented Sequences — WARN

FastQC identified one overrepresented sequence consisting of N bases.

It occurred in 7,394 reads (0.507%). No known source was identified.

This result is consistent with the localized N-content peaks observed
in R2 and represents a small group of reads containing a large number
of undetermined bases rather than a known biological overrepresented
sequence.

### Adapter Content — PASS

No significant adapter contamination was detected in R2.

---

# R1 vs R2 Summary

| FastQC module | R1 | R2 | Interpretation |
|---|---|---|---|
| Per-base sequence quality | PASS | PASS | High base quality across both reads |
| Per-tile sequence quality | FAIL | FAIL | Localized tile-specific quality variation |
| Per-base sequence content | FAIL | FAIL | Strong bias during approximately the first 20 bp |
| Per-sequence GC content | WARN | WARN | Observed GC distribution differs from theoretical |
| Per-base N content | PASS | PASS | Overall N content is low |
| Sequence Length Distribution | WARN | WARN | Most reads are 98–99 bp, with a smaller fraction of shorter reads |
| Sequence Duplication Levels | PASS | PASS | No major or extreme duplication problem |
| Overrepresented sequences | PASS | WARN | R2 contains a small group of all-N reads |
| Adapter Content | PASS | PASS | No significant adapter contamination |

---

## Key Quantitative Results

| Metric | R1 | R2 |
|---|---:|---:|
| Reads | 1,457,207 | 1,457,207 |
| Total bases | 126.7 Mb | 126.3 Mb |
| Read length | 35–99 bp | 35–99 bp |
| GC content | 51% | 51% |
| N content | 0.17% overall | Very low |
| Remaining after deduplication | 77.56% | 81.94% |
| Overrepresented all-N reads | None detected | 7,394 (0.507%) |

## FastQC Reports

- [R1 FastQC report](../results/fastqc/SRR31439393_1_fastqc.html)
- [R2 FastQC report](../results/fastqc/SRR31439393_2_fastqc.html)