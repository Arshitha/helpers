## MRIQC on biowulf

### Building singularity images from docker hub
```bash
singularity build mriqc-0.16.simg docker:poldracklab/mriqc:0.16.1

```

### Setting the `SINGULARITY_BINDPATH` env variable 
```bash
export SINGULARITY_BINDPATH=/gs4,/gs6,/gs7,/gs8,/gs9,/gs10,/gs11,/spin1,/fdb,/data,/lscratch
```

### Running mriqc 
```bash
singularity run --cleanenv \
-B /data/NIMH_scratch/afni-frontiers-proj/ds-frontiers-qc:/in \
-B /data/NIMH_scratch/afni-frontiers-proj/ds-frontiers-qc/derivatives:/out \
/data/MLDSST/containers/mriqc-0.16.simg \
/in /out participant --participant_label 101
```
