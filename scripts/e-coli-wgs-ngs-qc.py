#!/usr/bin/env python
# coding: utf-8

# # FASTQ Exploration and Nucleotide Composition
# 
# Analysis of paired-end Illumina WGS data from *Escherichia coli*.
# 
# **SRA accession:** SRR31439393  
# **File analyzed:** SRR31439393_1.fastq  
# **Tools:** Python, Biopython

# ## 1. Inspecting a FASTQ Record
# 
# First, we inspect a single FASTQ record to examine how Biopython
# represents sequence identifiers, descriptions, nucleotide sequences,
# and per-base Phred quality scores.

# In[5]:


from Bio import SeqIO

recs = SeqIO.parse("/home/elena/SRR31439393/SRR31439393_1.fastq", "fastq")

rec = next(recs)

print(rec.id)
print(rec.description)
print(rec.seq)
print(rec.letter_annotations)


# ## 2. Nucleotide Composition
# 
# The nucleotide composition of the R1 FASTQ file was calculated by
# iterating through all reads and counting each nucleotide.
# 
# The FASTQ file was processed sequentially using `SeqIO.parse()`,
# without loading the complete dataset into memory.

# In[6]:


from collections import defaultdict
recs = SeqIO.parse("/home/elena/SRR31439393/SRR31439393_1.fastq", "fastq")
cnt = defaultdict(int)
for rec in recs:
    for letter in rec.seq:
        cnt[letter] += 1
tot = sum(cnt.values())

for letter, count in cnt.items():
    print(f"{letter}: {100 * count / tot:.2f}% ({count})")


# ## 3. Distribution of N Calls by Read Position
# 
# The overall nucleotide composition showed that 0.17% of the
# observed bases were reported as `N`. To investigate whether
# ambiguous bases were concentrated at particular positions within
# the reads, the number of `N` calls was calculated for each read
# position.
# 
# The analysis was performed on the R1 FASTQ file using Biopython
# `SeqIO.parse()`. Each read was examined base by base, and `N` calls
# were counted according to their position within the read.

# In[7]:


from collections import defaultdict
from Bio import SeqIO
import matplotlib.pyplot as plt

recs = SeqIO.parse(
    "/home/elena/SRR31439393/SRR31439393_1.fastq",
    "fastq"
)

n_cnt = defaultdict(int)

for rec in recs:
    for i, letter in enumerate(rec.seq):
        pos = i + 1
        if letter == "N":
            n_cnt[pos] += 1

seq_len = max(n_cnt.keys())
positions = range(1, seq_len + 1)

plt.figure(figsize=(12, 6))
plt.plot(positions, [n_cnt[x] for x in positions])

plt.title("Number of N Calls by Read Position")
plt.xlabel("Read position")
plt.ylabel("Number of N calls")

plt.show()


# In[5]:


for position, count in sorted(n_cnt.items()):
    print(position, count)


# In[8]:


sum(n_cnt.values())


# ### Results
# 
# A total of 210,491 `N` calls were detected, corresponding to
# 0.17% of all analyzed bases.
# 
# The `N` calls were not uniformly distributed across read positions.
# Several pronounced peaks were observed, particularly at positions
# 2, 12, and 28–36, with an additional peak at position 68.
# 
# The highest number of `N` calls was observed at position 35,
# with 35,867 calls.
# 

# ## 4. Read Length Distribution
# 
# The length of each read in the R1 FASTQ file was calculated using
# Biopython. The distribution of read lengths was examined to
# characterize the sequencing dataset and assess read-length
# consistency.

# In[7]:


from Bio import SeqIO

recs = SeqIO.parse(
    "/home/elena/SRR31439393/SRR31439393_1.fastq",
    "fastq"
)

read_lengths = []

for rec in recs:
    read_lengths.append(len(rec.seq))


# In[8]:


print("Number of reads:", len(read_lengths))
print("Minimum read length:", min(read_lengths))
print("Maximum read length:", max(read_lengths))
print("Mean read length:", sum(read_lengths) / len(read_lengths))


# In[ ]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(read_lengths, bins=range(35, 101), edgecolor="black")

plt.title("Read Length Distribution")
plt.xlabel("Read length (bp)")
plt.ylabel("Number of reads")

plt.show()


# ### Results
# 
# The R1 FASTQ file contains 1,457,207 reads with lengths ranging
# from 35 to 99 bp. The mean read length is 87.01 bp.
# 
# The read length distribution is strongly concentrated at 99 bp,
# with a smaller peak at 98 bp and additional groups of shorter reads.
# A small but distinct group of reads has a length of 35 bp.
# 
# The predominance of 99 bp reads indicates that the dataset is
# largely composed of near-full-length reads, while the presence of
# shorter reads indicates heterogeneity in read length.
# 
# The shorter reads were retained because the available QC results did
# not provide sufficient evidence that length-based filtering was required.

# ## 5. Phred Quality Score Distribution
# 
# The distribution of Phred quality scores was analyzed for all bases
# in the R1 FASTQ file.
# 
# For each read, the per-base Phred quality scores were extracted from
# the `SeqRecord` object using Biopython. The frequency of each quality
# score was then calculated across the dataset.
# 
# This analysis provides an overview of the sequencing quality before
# examining how quality changes across individual read positions.

# In[10]:


from collections import defaultdict
from Bio import SeqIO

recs = SeqIO.parse(
    "/home/elena/SRR31439393/SRR31439393_1.fastq",
    "fastq"
)

cnt_qual = defaultdict(int)

for rec in recs:
    for qual in rec.letter_annotations["phred_quality"]:
        cnt_qual[qual] += 1

tot = sum(cnt_qual.values())

for qual, count in sorted(cnt_qual.items()):
    print(f"{qual}: {100 * count / tot:.2f}% ({count})")


# ### Results
# 
# The R1 FASTQ file contained four distinct Phred quality scores:
# Q2, Q12, Q26, and Q34.
# 
# The majority of bases (88.85%) had a Phred score of 34, indicating
# high base-call quality for most of the dataset. Q26 accounted for
# 5.96% of bases, while Q12 accounted for 5.03%.
# 
# A total of 210,491 bases had a Phred score of 2. This number exactly
# matches the total number of `N` bases identified in the nucleotide
# composition analysis, indicating that all `N` calls in this dataset
# were assigned a Phred score of 2.
# 
# The quality-score distribution therefore shows that most bases were
# called with high confidence, while a smaller fraction had lower
# quality scores or were reported as ambiguous `N` bases.

# ## 6. Per-base Phred Quality
# 
# To investigate how sequencing quality varies across read positions,
# the distribution of Phred quality scores was calculated separately
# for each position in the R1 reads.
# 
# Unlike the previous analysis, which examined the overall frequency
# of Phred scores, this analysis preserves the positional information
# and allows changes in quality across the read to be visualized.
# 
# 

# In[13]:


from collections import defaultdict
from Bio import SeqIO

recs = SeqIO.parse(
    "/home/elena/SRR31439393/SRR31439393_1.fastq",
    "fastq"
)

qual_pos = defaultdict(list)

for rec in recs:
    for i, qual in enumerate(rec.letter_annotations["phred_quality"]):
        pos = i + 1
        qual_pos[pos].append(qual)


# In[18]:


from collections import Counter

for pos, n_count in top_n_positions:
    quality_counts = Counter(qual_pos[pos])

    print(f"\nPosition {pos}: N calls = {n_count}")

    for qual in sorted(quality_counts):
        count = quality_counts[qual]
        percentage = 100 * count / len(qual_pos[pos])

        print(f"  Q{qual}: {count} ({percentage:.2f}%)")



# ### Results
# 
# The analysis of Phred quality scores at positions with the highest
# number of `N` calls showed that all `N` bases were assigned a Phred
# score of 2 (Q2), the lowest quality score observed in the dataset.
# 
# However, `N` calls represented only a small fraction of all bases
# at the affected positions. For example, at position 35, which had
# the highest number of `N` calls, 2.46% of bases had Q2, while 87.74%
# had Q34.
# 
# These results indicate that the positional peaks of `N` calls are
# associated with very low-quality base calls, but the affected
# positions are not globally low-quality because the majority of bases
# at these positions have high Phred scores.

# ## 7. GC Content

# In[21]:


gc_content = 100 * (cnt["G"] + cnt["C"]) / (
    cnt["A"] + cnt["C"] + cnt["G"] + cnt["T"]
)

print(f"GC content: {gc_content:.2f}%")


# ### Results
# 
# The GC content calculated from the R1 FASTQ data was 51.22%,
# excluding ambiguous `N` bases.
# 
# This value is close to the GC content reported in the SRA metadata
# (50.9%), with a difference of only 0.32 percentage points. The
# agreement between the two values supports the consistency of the
# nucleotide composition analysis.

# ## Paired-end Read Validation
# 
# The R1 and R2 FASTQ files were processed simultaneously using Python's
# `zip()` function.
# 
# A total of 1,457,207 read pairs were checked. The read identifiers were
# identical between R1 and R2 for all checked pairs, with zero mismatches.
# 
# This confirms that the R1 and R2 FASTQ files are correctly paired and
# maintain consistent read order.

# In[14]:


from Bio import SeqIO

f1 = open('/home/elena/SRR31439393/SRR31439393_1.fastq', 'r')
f2 = open('/home/elena/SRR31439393/SRR31439393_2.fastq', 'r')

rec1 = next(SeqIO.parse(f1, 'fastq'))
rec2 = next(SeqIO.parse(f2, 'fastq'))

print("R1 ID:", rec1.id)
print("R2 ID:", rec2.id)

f1.close()
f2.close()


# In[15]:


from Bio import SeqIO

f1 = open('/home/elena/SRR31439393/SRR31439393_1.fastq', 'r')
f2 = open('/home/elena/SRR31439393/SRR31439393_2.fastq', 'r')

recs1 = SeqIO.parse(f1, 'fastq')
recs2 = SeqIO.parse(f2, 'fastq')

pairs_checked = 0
mismatches = 0

for rec1, rec2 in zip(recs1, recs2):
    pairs_checked += 1

    if rec1.id != rec2.id:
        mismatches += 1
        print("Mismatch:", rec1.id, rec2.id)
        break

print("Pairs checked:", pairs_checked)
print("Mismatches:", mismatches)

f1.close()
f2.close()


# In[ ]:




