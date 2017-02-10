def fatorial(x):
    if x == 0:
        return 1
    if x > 1:
        return x * fatorial(x-1)
    else:
        return x
