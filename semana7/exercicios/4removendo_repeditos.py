# Exercício 4 - Removendo elementos repetidos
#
# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
#
# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

def remove_repetidos(lista):
    clone = lista[:]
    remover = []
    print(clone)
    for item in lista:
        cont = 0
        repet = clone.count(item)
        while repet >= 2:
            clone.remove(item)
            repet -= 1
    clone.sort()
    return clone

def high_and_low(numbers):
    return list(map(int,numbers.split(',')))

print(remove_repetidos(high_and_low(input("entre com o valor: "))))
