
from confiance_interval2 import *

def t_distribution_confidence_interval(data, alpha):
    confidence_list = list()
    for (num in data):
        confidence_list.append(t_distribution_cdf(num, num-1));
    
    confidence_list.sort()
    idx = confidence_list.index(alpha)
       
    return data[idx], alpha
