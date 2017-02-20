# Exercício 3 - Primos
#
# Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 como parâmetro
#e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

def isprimo(valor):
    fator = 2
    while fator < valor:
        if valor % fator == 0:
            return False
        else:
            fator += 1
    return True


def n_primos(x):
    aux = 2
    cont = 0
    while aux <= x:
        if(isprimo(aux)):
            cont +=1
        aux += 1
    return cont

x = int(input("digite um numero primo ou não > 2: "))
print(n_primos(x))
