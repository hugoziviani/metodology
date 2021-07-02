from collections import Counter
import math


def mean(vect_numbers):
    return sum(vect_numbers)/len(vect_numbers)

def mode(vect_numbers):
    #retorno o mais comum e suas ocorrencias
    data = Counter(vect_numbers)
    return data.most_common(1)[0]

def percentile(vect_numbers, percentile):
    result = sorted(vect_numbers)[int(math.ceil((len(vect_numbers) * percentile)/100))-1]
    return result

def median(vect_numbers):
    return math.sqrt(percentile(vect_numbers, 50))

def main():
    numeros = [1,2,3,4,5,6,7,8,9,10,10]
    print(numeros)
    # numeros.sort()
    print("Media:", mean(numeros))
    print("Moda:", mode(numeros))
    print("Percentil:", percentile(numeros, 50))
    print("Mediana:", median(numeros))

if __name__ == "__main__":
    main()