from random import randint
numeros= list()
def sorteia (lista):
    for c in range(0,5):
        lista.append(randint(1, 10))
    print(f"os valores sao: {lista}")


def soma(lista):
    soma=0
    for valor in lista:
        if valor %2 ==0 :
            soma+=valor
    print(f"somando os valores pares temos: {soma}")


sorteia(numeros)
soma(numeros)