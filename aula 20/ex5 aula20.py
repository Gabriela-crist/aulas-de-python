from random import randint
numeros= []
def sorteia (*num):
    for c in range(5):
        numeros.append(randint(0,60))
    print(numeros)


def soma(*num):
    pares= 0
    for i, v in enumerate(num):
        for v in num:
            if v % 2 == 0:
                pares+=v
    print(pares)


soma(numeros)
sorteia(numeros)
