num  = [[], []]
pegue = 0
for c in range(0,7):
    pegue = int(input(f"o digite um numero: "))
    if pegue %2 == 0:
        num[0].append(pegue)
        num[0].sort()
    else:
        if pegue %2 == 1:
            num[1].append(pegue)
            num[1].sort()
    pegue+=1
print(f"os numeros pares sao : {num[0]} \nos numeros impares sao : {num[1]}")