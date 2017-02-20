# Exercício 4 - Retângulos 2
#
# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
#de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
aux = altura
while aux > 0:
    x = largura
    linha = ""
    while x > 0:
        if((aux == 1 or aux == altura) and x > 0 or (x == 1 or x == largura)):
            linha += "#"
        else:
            linha += " "
        x -= 1
    print (linha)
    aux -= 1
