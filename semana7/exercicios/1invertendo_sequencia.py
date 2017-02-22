# Exercício 1: Invertendo sequência
#
# escreva um programa que recebe uma sequência de números inteiros terminados por 0
# imprima todos os valores em ordem inversa. Note que 0 (ZERO) não deve fazer parte da sequência.

lista = []
continuar = True
while continuar:
    valor = int(input("Digite um número != 0: "))
    if(valor == 0):
        break
    lista.append(valor)

x = len(lista)-1
while x >= 0:
    print(lista[x])
    x-=1
