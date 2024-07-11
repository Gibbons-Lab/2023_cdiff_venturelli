# 2023 C. difficile strains

This repository contains data and scripts for the construction of strain-specific Genome-scale Metabolic Models and some comparisons.

## Assembly

Isolate sequencing data as processed using our [isolate nextflow pipeline](https://github.com/Gibbons-Lab/pipelines/blob/master/isolates/main.nf) which consistes of the following steps:

1. QC and trimming with FASTP
2. Assembly with MEGAHIT
3. Classification with GTDB-TK
4. Quality control with CHECKM2
5. Phylogenetic tree building with FastTree based on the GTDB alignment

## Model reconstruction

### Medium

The DM38 medium was manually converted from the media recipe by dividing compounds into their respective ions and annotation using the ModelSEED database. The media in MICOM and CARVEME formats are available [in this repo here](https://github.com/Gibbons-Lab/2023_cdiff_venturelli/tree/main/models/data).

### Reconstruction

Models were built with out [model builder nextflow pipeline](https://github.com/Gibbons-Lab/pipelines/tree/master/model_builder) using CARVEME and gapfilling on the DM38 medium. A joined mode containing all starins is also provided in the
`models/data` folder.

### Functional overlap

The analysis included in the paper can be found in [the notebook](functional_overlap.ipynb).
