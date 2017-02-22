# Exercício 3 - Maior elemento de uma lista
#
# Escreva a função maior_elemento que recebe como parâmetro uma lista
# com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(lista):

    maior = lista[0]
    for item in lista:
        if(item >= maior):
            maior = item
    return maior

lista = list(input("entre com o valor: "))

for i in range(0,len(lista)):
    lista[i] = int(lista[i])

print(maior_elemento(lista))
