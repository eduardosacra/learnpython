x =  int(input("entre com um numero "))

aux = 0
test = False
while x > 0:
    aux = x % 10
    x = x // 10
    if(aux == x % 10):
        test = True
if test:
    print("sim")
else:
    print("não")
