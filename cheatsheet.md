### Building singularity images from docker hub
```bash
singularity build mriqc-0.16.simg docker:poldracklab/mriqc:0.16.1
export SINGULARITY_BINDPATH=/gs4,/gs5,/gs6,/gs7,/gs8,/gs9,/gs10,/gs11,/spin1,/scratch,/fdb,/data,/lscratch
```
