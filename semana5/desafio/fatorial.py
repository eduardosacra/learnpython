def fatorial(val):
    if(val == 1):
        return val
    else:
        return val * fatorial(val -1)

valor = 1

while valor != 0:
    valor = int(input("Digite um valor para calcular o fatorial, para sair digite 0: "))
    if(valor == 0):
        print("até a próxima")
        break
    print( fatorial(valor))
