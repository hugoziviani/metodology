import math


def mean(vect_numbers):
    return sum(vect_numbers)/len(vect_numbers)

def interval(vet_numbers):
    return min(vet_numbers), max(vet_numbers)

def variance(vet_numbers):
    var = 0
    med = mean(vet_numbers)
    for num in vet_numbers:
        var = var + pow((num - med), 2)
    return var/len(vet_numbers)

def standard_deviation(vet_numbers):
    return math.sqrt(variance(vet_numbers))

def main():
    #fonte:  https://mundoeducacao.uol.com.br/matematica/variancia-desvio-padrao.htm

    numeros = [10, 9, 11, 12, 8]
    print("Minimo: ", str(interval(numeros)[0]))
    print("Maximo: ", str(interval(numeros)[1]))
    print("Variancia: ", variance(numeros))
    print("Desvio Padrao: ", standard_deviation(numeros))
        
if __name__ == "__main__":
    main()