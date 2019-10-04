import data_viz
import argparse

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
        




def binary_serach(key, L):
    pass

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'Inputs for plotting gene'
                                    ' expression for tissue types')
    parser.add_argument('--data_file', type = str, help = 'File gontaining gene read data', required = True)
    
    parser.add_argument('--sample_file', type = str, help = 'File gontaining sample attribute data', required = True)
    
    parser.add_argument('--gene', type = str, help = 'Name of gene to analyze', required = True)
    
    parser.add_argument('--sample_type', type = str, help = 'Group of samples to analyze gene expression for', required = True)
    
    arguments = parser.parse_args()
    
    return arguments
    

def main():
    arguments = parse_arguments()
    
    data_file_name=arguments.data_file
    sample_info_file_name=arguments.sample_file
    group_col_name = arguments.sample_type
    sample_id_col_name = 'SAMPID'

    gene_name = arguments.gene

if __name__ == '__main__':
    main()
