x =  int(input("entre com um numero "))

total = 0
while x > 0:
    total += x % 10
    x  = x // 10
print(total)
