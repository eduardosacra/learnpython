# Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores primos
# indicando também a mutiplicidade de cada fatores
# 8 = 2 * 2 * 2
# 20 = 2 * 2 * 5
# 1000 = 2^3 * 5^3 ...


n = int(input("Digite um número inteiro > 1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if(multiplicidade > 0):
        print("Fator",fator,"multiplicidade =",multiplicidade)
        multiplicidade = 0
    fator += 1
