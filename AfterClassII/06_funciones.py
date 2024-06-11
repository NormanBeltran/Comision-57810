def multiplicar(*args):
    resultado = 1
    for p in args:
        resultado *= p
    return resultado


print(multiplicar(4,5,6,7,8,9))