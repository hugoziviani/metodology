import math

def normal_distribuition(x, mu, std_dev):
    if(std_dev == 0):
        return 0
    result = math.exp((-1)*math.pow(x-mu, 2)/2 * math.pow(std_dev, 2)) / math.sqrt(2 * math.pi * math.pow(std_dev, 2))

    return result

def normal_distribuition2(x):
    
    result = (math.exp((-1)*math.pow(x, 2)/2)) / (math.sqrt(2 * math.pi))

    return result



def main():
    nd = normal_distribuition(3, 4, 0)
    nd2 = normal_distribuition2(1)
    print(f"Distribuicao Normal: {nd}")
    print(f"Distribuicao Normal2: {nd2}")

if __name__ == "__main__":
    main()