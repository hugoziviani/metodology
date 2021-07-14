# Intervalos de Confiança - Questão 2

import math
from scipy import special

def t_distribution_pdf(x, v):
    return (math.gamma(v+1/2)/ math.sqrt(v * math.pi) * math.gamma(v/2)) * math.pow((1+math.pow(x,2)/v), -(v+1/2))


def t_distribution_cdf(x, v):
    return (1/2 + (x * (math.gamma((v + 1) / 2)) * (special.hyp2f1(1/2, (v+1)/2, 3/2, -(math.pow(x, 2)) /v))/(math.sqrt(v * math.pi) * math.gamma(v/2))))


def t_distribution_cdf2(x1, x2, v):
    result_x1 = t_distribution_pdf(x1, v)
    result_x2 = t_distribution_pdf(x2, v)
    
    return abs(result_x2-result_x1)


def main():
    r = t_distribution_cdf(0,1)
    n1 = t_distribution_cdf(0, 1)
    r1 = t_distribution_cdf2(0, 1, 1)

    print(r, n1, r1)


if __name__ == "__main__":
    main()