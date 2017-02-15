# Exercício 3 - Primos
# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
# Note que
# maior_primo(100) deve retornar 97
# maior_primo(7) deve retornar 7

def maior_primo(primo):
    aux = i = 2
    while i <= primo:
        j = 2
        isprimo = True
        while j <= i:
            if i % j == 0 and i != j :
                isprimo = False
                break
            j += 1
        if(isprimo == True):
            aux = i
        i += 1
    return aux
