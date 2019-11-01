# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Uses a hash table to collect and store header values and sample IDs, then uses a second hash table with sample IDs as keys to get the values of the counts, then plots the result.

Note: After cloning, run `git submodule update --init` to download the `hash-tables-ocmadin` submodule.

Then run:
```
- curl https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt > GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
- wget "https://github.com/swe4s/lectures/raw/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
```
To get the data.


Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

Usage: 

`python plot_gtex.py --data_file 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz' --sample_file 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt' --gene BRCA2 --sample_type 'SMTS' --output_filename='BRCA2_output.png'
`
