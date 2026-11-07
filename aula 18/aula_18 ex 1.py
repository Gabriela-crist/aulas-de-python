dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input("digite seu nome:")))
    dados.append(int(input("digite seu peso:")))
    if len(pessoas)== 0 :
        maior = menor= dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    pq = str(input("quer continuar cadastrando[S/N]?:")).upper().strip()
    if pq == "N":
        break
print(f"foram cadastradas {len(pessoas)} pessoas")
print(f"o maior peso é {maior} que é de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}", end="")
print(f"o menor peso é {menor} que é de ", end="")
for p in pessoas:
    if p[1]== menor:
        print(f"{p[0]}",end="")
