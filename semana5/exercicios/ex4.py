# Exercício 4 - Máximo com 3 parâmetros
# Reescreva a função 'maximo' do exercício 2, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
# Note que
# maximo(30,14,10) deve retornar 30
# maximo(0,-1, 1) deve retornar 1

def maximo(x,y,z):
    if(x > y and x > z):
        return x
    elif y > x and y > z:
        return y
    else:
        return z

x = int(input("Entre com um valor para x: "))
y = int(input("Entre com um valor para y: "))
z = int(input("Entre com um valor para z: "))

print(maximo(x,y,z))
