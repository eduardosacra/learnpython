# Exercício 4 - Retângulos 2
#
# Escreva um programa que recebe como entradas (utilize a função input)
#dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente.
#O programa deve imprimir uma cadeia de caracteres que represente o retângulo
# informado com caracteres '#' na saída.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura > 0:
    x = largura
    linha = ""
    while x > 0:
        linha += "#"
        x -= 1
    print (linha)
    altura -= 1
