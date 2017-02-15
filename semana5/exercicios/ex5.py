# Exercício 5 - Vogais
# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
# Note que
# vogal("a") deve retornar True
# vogal("b") deve retornar False
# vogal("E") deve retornar True
# Os valores True e False devolvidos devem ser do tipo bool (booleanos)

import re
def vogal(char):
    verifica = re.compile('[aAeEiIoOuU]')
    if verifica.match(char) != None:
        return True
    else:
        return False

print(vogal(input("entre com uma vogal valida: ")))
