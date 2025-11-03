def media(*args):
    total=len(args)
    suma=sum(args)
    return print(suma / total)

def mediana(*args):
    args= sorted(args)
    n = len(args)
    mitad = n//2

    if n % 2 == 0:
        return print((args[mitad - 1] + args[mitad]) / 2)
    else:
        return print(args[mitad])