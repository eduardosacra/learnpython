# desafio - tabuada
#
# desenhe a tabuada de 1 até 10

x = 1

while x <= 10:
    y=1
    while y <= 10:
        print(x,"x",y,"=",x*y)
        y += 1
        print()
    x += 1
    print("********")
