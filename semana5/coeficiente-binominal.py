

def coeficientebinominal(n,k):
    return fatorial(n)/(fatorial(k)*(fatorial(n-k)))

def fatorial(x):
    if x == 0:
        return 1
    if x > 1:
        return x * fatorial(x-1)
    else:
        return x

x = int(input("Entre com um valor inteiro para n: "))
y = int(input("Entre com um valor inteiro para k: "))
print(coeficientebinominal(x,y))
