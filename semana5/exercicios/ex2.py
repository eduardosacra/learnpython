# Exercício 2 - Máximo
# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.
# Note que
# maximo(3,4) deve retornar 4
# maximo(0,-1) deve retornar 0

def maximo(x,y):
    if(x > y):
        return x
    else:
        return y

x = int(input("Entre com um valor para x: "))
y = int(input("Entre com um valor para y: "))

print(maximo(x,y))
