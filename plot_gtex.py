import data_viz as dv
import argparse
import gzip
import sys

sys.path.insert(1,"hash-tables-ocmadin")
import hash_tables
import hash_functions

def linear_search(key, L):
    
    if key is None:
        raise TypeError('linear_search: must supply a key')
    if isinstance(key, list):
        raise TypeError('linear_search: key must be a single value')
    if L is None:
        raise TypeError('linear_search: must supply a list')
    if not isinstance(L,list):
        raise TypeError('linear_search: list must be of type "list"')
        
    for i in range(len(L)):
        val = L[i]
        if val == key:
            return i
    return -1
        




def binary_search(key, L):
    
    if key is None:
        raise TypeError('linear_search: must supply a key')
    if isinstance(key, list):
        raise TypeError('linear_search: key must be a single value')
    if L is None:
        raise TypeError('linear_search: must supply a list')
    if not isinstance(L,list):
        raise TypeError('linear_search: list must be of type "list"')
        
    for i in range(len(L)):
        lo = -1
        hi = len(L)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if ( key < L[mid][0] ):
            hi = mid
        else:
            lo = mid
    return -1

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'Inputs for plotting gene'
                                    ' expression for tissue types')
    parser.add_argument('--data_file', type = str, help = 'File gontaining gene read data', required = True)
    
    parser.add_argument('--sample_file', type = str, help = 'File gontaining sample attribute data', required = True)
    
    parser.add_argument('--gene', type = str, help = 'Name of gene to analyze', required = True)
    
    parser.add_argument('--sample_type', type = str, help = 'Group of samples to analyze gene expression for', required = True)
    
    parser.add_argument('--output_filename', type = str, help = 'Boxplot File Name', required = False)
    
    arguments = parser.parse_args()
    
    return arguments

def parse_sample_file(filename):
    
    samples = []
    sample_info_header = None
    for l in open(filename):
        if sample_info_header == None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))
    return sample_info_header,samples
    

def main():
    
    arguments = parse_arguments()
    
    data_file_name=arguments.data_file
    sample_info_file_name=arguments.sample_file
    group_col_name = arguments.sample_type
    sample_id_col_name = 'SAMPID'

    gene_name = arguments.gene
    
    sample_info_header,samples = parse_sample_file(sample_info_file_name)
    
    key = linear_search(group_col_name,sample_info_header)
    
    table = hash_tables.ChainedHash(50,hash_functions.h_rolling)
    keys = []
    for i in samples:
        result = table.search(i[key])
        if result is None:
            table.add(i[key],[i[0]])
            keys.append(i[key])
        else:
            loc = table.search_loc(i[key])
            table.T[loc][0][1].append(i[0])

        
        
        
    
    version = None
    dim = None
    data_header = None
    
    gene_name_col = 1
    
    table_2 = hash_tables.ChainedHash(10000,hash_functions.h_rolling)
    

    
    for l in gzip.open(data_file_name, 'rt'):
        if version == None:
            version = l
            continue
    
        if dim == None:
            dim = [int(x) for x in l.rstrip().split()]
            continue
    
        if data_header == None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])
    
            continue
    
        A = l.rstrip().split('\t')
    
        if A[gene_name_col] == 'BRCA2':
            for header, gene_data in zip(data_header[2:], A[2:]):
                table_2.add(header[0],gene_data)
    group_counts = [[] for _ in range(len(keys))]
    for i in range(len(keys)):
        for val in table.search(keys[i]):
            result = table_2.search(val)
            if result is not None:
                group_counts[i].append(int(result))
    
    dv.boxplot(group_counts,keys,ylabel = 'Gene Read Counts', xlabel = arguments.sample_type, title = arguments.gene, out_file_name = arguments.output_filename)

if __name__ == '__main__':
    main()
