x =  int(input("entre com um numero "))

test = False

div = 0
i = 1
while i <= x:
    if x % i == 0:
        div += 1
    i+=1

if( div == 2):
    print("primo")
else:
    print("não primo")
