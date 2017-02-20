# desafio -  descobrir se é um numero primo

x = int(input("digite um numero primo: "))

def isprimo(valor):
    fator = 2
    while fator < valor:
        if valor % fator == 0:
            return False
        else:
            fator += 1
    return True

if(isprimo(x)):
    print(x,"é primo! xD")
else:
    print(x,"não é primo :/")
