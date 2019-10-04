import math

def list_mean(L):
    """
    Function to compute the mean of a list
    
    Arguments
    ---------
    L : list of floats/ints
        List to compute the mean of
    
    Returns
    -------
    mean : float
        The mean of the list
    """
    if L is None:
        raise TypeError("list_mean: No input passed to function")
        
    if not isinstance(L,list):
        raise TypeError("list_mean: Wrong input type")

    if len(L) == 0:
        raise IndexError("list_mean: List is empty")
        
    valid_types = [isinstance(value,(int,float,complex)) for value in L]
    
    if not any(valid_types):
        raise TypeError("list_mean: Invalid types in list")
    
    mean=sum(L)/len(L)
    
    return mean

def list_stdev(L):
    """
    Function to compute the standard deviation of a list
    
    Arguments
    ---------
    L : list of floats/ints
        List to compute the mean of
    
    Returns
    -------
    stdev : float
        The standard deviation of the list
    """
    if L is None:
        raise TypeError("list_stdev: No input passed to function")
        
    if not isinstance(L,list):
        raise TypeError("list_stdev: Wrong input type")
        
    if len(L) == 0:
        raise IndexError("list_stdev: List is empty")

    valid_types = [isinstance(value,(int,float,complex)) for value in L]
    
    if not any(valid_types):
        raise TypeError("list_stdev: Invalid types in list")
    
    mean = list_mean(L)

    stdev = math.sqrt(sum([(mean-x)**2 for x in L]) / len(L))
        
    return stdev
