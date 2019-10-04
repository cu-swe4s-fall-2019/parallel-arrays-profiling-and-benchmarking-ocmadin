# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

Usage: 

`python plot_gtex.py --data_file 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz' --sample_file 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt' --gene BRCA2 --sample_type 'SMTS' --output_filename='BRCA2_output.png'
`
