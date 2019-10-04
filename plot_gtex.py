import data_viz as dv
import argparse
import gzip

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
    
    group_col_idx = linear_search(group_col_name, sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)
    
    groups = []
    members = []
    
    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]
    
        curr_group_idx = linear_search(curr_group, groups)
    
        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])
    
        members[curr_group_idx].append(sample_name)
        
        
    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]

        curr_group_idx = linear_search(curr_group, groups)
    
        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)
    
    version = None
    dim = None
    data_header = None
    
    gene_name_col = 1
    
    group_counts = [ [] for i in range(len(groups)) ]
    

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
    
        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = binary_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break 
    
    dv.boxplot(group_counts,groups,ylabel = 'Gene Read Counts', xlabel = arguments.sample_type, title = arguments.gene, out_file_name = arguments.output_filename)

if __name__ == '__main__':
    main()
