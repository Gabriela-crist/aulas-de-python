from random import randint
numeros= list()
def sorteia (lista):
    for c in range(0,5):
        lista.append(randint(1, 10))


"""def soma(*num):
    pares= 0
    for i, v in enumerate(num):
        for v in num:
            if v % 2 == 0:
                pares+=v
    print(pares)"""


"""soma(numeros)"""
sorteia(numeros)
print(numeros)
