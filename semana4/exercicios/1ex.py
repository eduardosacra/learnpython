x =  int(input("entre com um numero "))
total = x

while x > 1:
    x -= 1
    total *=  x

if x == 0:
    print(1)
else:
    print(total)
