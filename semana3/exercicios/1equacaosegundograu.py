#input a, b, c
#Deverá resolver 3 situações, se o valor é maior de delta é negativo ou positivo ou igual a zero
#se delta > 0 dizer que tem duas raizes reais e printar elas
#se delta == 0 dizer que tem apenas uma raiz
#se delta < 0 dizer que não tem raizes reais

import math

a = int(input("Defina o valor para a: "))
b = int(input("Defina o valor para b: "))
c = int(input("Defina o valor para c: "))

delta = b**2 -4 * a * c

if (delta < 0):
    print("esta equação não possui raízes reais")

elif (delta == 0):
    raiz = (- b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é",raiz)

else:
    raiz1 = (- b + math.sqrt(delta)) / 2 * a
    raiz2 = (- b - math.sqrt(delta)) / 2 * a

    if (raiz1 < raiz2):
        print("as raízes da equação são",raiz1,"e",raiz2)
    else:
        print("as raízes da equação são",raiz2,"e",raiz1)
