import matplotlib.pyplot as plt
import math_lib as ml

def boxplot(L,labels, xlabel=' ', ylabel=' ', title=' ', out_file_name='boxplot.png'):
    if L is None:
        raise TypeError('boxplot: No input to L')
    if not isinstance(L,list):
        raise TypeError('boxplot: must pass a list to L')
        
    valid_types = [isinstance(value,(int,float,complex,list)) for value in L]
    
    if not any(valid_types):
        raise TypeError("boxplot: Invalid types in list")
        
    if not isinstance(out_file_name,str):
        raise TypeError("boxplot: File name must be str")
        
    if not isinstance(xlabel, str):
        raise TypeError('boxplot: X label must be str')

    if not isinstance(ylabel, str):
        raise TypeError('boxplot: X label must be str')
        
    if not isinstance(title, str):
        raise TypeError('boxplot: X label must be str')
        
    fig = plt.figure(figsize=(10,5),dpi=300)
    ax = fig.add_subplot(1, 1 ,1)
    ax.title.set_text(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    ax.boxplot(L,labels=labels)
    ax.xaxis.set_tick_params(rotation=90)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError


def histogram(L, out_file_name='histogram.png'):
    if L is None:
        raise TypeError('histogram: No input to L')
    if not isinstance(L,list):
        raise TypeError('histogram: must pass a list to L')
        
    valid_types = [isinstance(value,(int,float,complex)) for value in L]
    
    if not any(valid_types):
        raise TypeError("histogram: Invalid types in list")
        
    if not isinstance(out_file_name,str):
        raise TypeError("histogram: File name must be str")
    fig = plt.figure(figsize=(3,3))
    ax = fig.add_subplot(1, 1 ,1)
    title = 'Mean: '+str(ml.list_mean(L))+ ', Stdev: ' + str(ml.list_stdev(L))
    ax.title.set_text(title)
    ax.set_ylabel('Values')
    ax.set_xlabel('')

    ax.hist(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError

    pass

def combo(L, out_file_name='combo.png'):
    if L is None:
        raise TypeError('combo: No input to L')
    if not isinstance(L,list):
        raise TypeError('combo: must pass a list to L')
        
    valid_types = [isinstance(value,(int,float,complex)) for value in L]
    
    if not any(valid_types):
        raise TypeError("combo: Invalid types in list")
        
    if not isinstance(out_file_name,str):
        raise TypeError("combo: File name must be str")
    
    fig,ax = plt.subplots(1,2,figsize=(10,5))
    title = 'Mean: '+str(ml.list_mean(L))+ ', Stdev: ' + str(ml.list_stdev(L))
    fig.suptitle(title)
    #ax[0,1].set_ylabel('Values')

    ax[1].hist(L)
    ax[1].set_ylabel('Frequency')
    ax[0].boxplot(L)
    ax[0].set_ylabel('Values')
    
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except ValueError:
        raise ValueError

    
    pass
