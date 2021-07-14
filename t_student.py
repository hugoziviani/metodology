# Teste T de Student

import statistics
import math

def statistic(data_1, data_2) {
    s = len(data_1)+len(data_2)
    st1 = statistics.stdev(data_1)
    st2 = statistics.stdev(data_1)
    return abs((statistics.mean(numbers1) - statistics.mean(numbers2))/math.sqrt(pow(s1,2) + math.pow(s2,2))/s)
