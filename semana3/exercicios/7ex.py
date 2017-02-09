x1 = int (input ("entre com o x1: "))
y1 = int (input ("entre com o y1: "))

x2 = int (input ("entre com o x2: "))
y2 = int (input ("entre com o y2: "))

if abs(x1 - x2) < 10 and  abs(y1-y2) < 10:
    print("perto")
else:
    print("longe")
