

# Intervalos de Confiança - Questão 1

import math

def normal_distribution_cdf(x, mu, std_dev):
    return(1 + math.erf(x-mu/std_dev * math.sqrt(2)))/2

def normal_distribution_cdf2(x):
    return (1 + math.erf(x/1 * math.sqrt(2)))/2
    
def normal_distribution_cdf3(x1, x2, mu, std_dev) {
    result_x1 = normal_distribution_cdf(x1, mu, std_dev)
    result_x2 = normal_distribution_cdf(x2, mu, std_dev)
    return abs(result_x2-result_x1)

def normal_distribution_cdf(x1, x2){
    result_x1 = normal_distribution_cdf2(x1)
    result_x2 = normal_distribution_cdf2(x2)
    return abs(result_x2-result_x1)

    


def main():
    numeros = [1,2,3,4,5,6,7,8,9,10,10]
    normal1 = normal_distribution_cdf(0,1,2)
    normal2 = normal_distribution_cdf2(1)

    print(normal1, normal2)

if __name__ == "__main__":
    main()