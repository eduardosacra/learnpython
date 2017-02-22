# Exercício 2 - Soma dos elementos de uma lista
#
# faça um programa que receba a leitura de valores inteiros diferentes de 0
# depois disso realize a soma de todos os elementos na lista

import sys

def soma_elementos(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

valor = list(input("entre com o valor: "))

for i in range(0,len(valor)):
    valor[i] = int(valor[i])

print(soma_elementos(valor))
