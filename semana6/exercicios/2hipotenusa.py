# Exercício 2 - Soma das hipotenusas
#
# Escreva uma função 'soma_hipotenusas' que receba como parâmetro
#um número inteiro positivo n e devolva a soma de todos os
#inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.
# Atenção: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez.
#
#Uma boa solução para este exercício é fazer um laço de 1 até n testando
#se o número é hipotenusa de algum triângulo. Uma solução que dificilmente
# vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

def ishipotenusa(n,valor):
    a = b = 1

    while a <= valor:
        b=1
        while b <= valor:
            if(int(math.sqrt(a**2+b**2)) == n):
                return n
            b += 1
        a += 1
    return 0

def soma_hipotenusas(valor_digitado):
    test = False
    cont =0
    soma=0
    hipotenusa =1
    while hipotenusa <= valor_digitado:
        a=1
        test = False
        while a <= valor_digitado and test == False:
            b=1
            while  b**2 + a**2 <= valor_digitado**2 :
                if(a**2 + b**2 == hipotenusa**2):
                    cont += 1
                    test = True
                    soma+=hipotenusa
                b += 1
            a += 1
        hipotenusa += 1
    return soma


limite = int(input("Entre com um valor inteiro positivo:"))
print(soma_hipotenusas(limite))
