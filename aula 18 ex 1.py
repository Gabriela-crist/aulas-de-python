dados = list()
pessoas = list()
cont = 0
maior = menor = 0
while True:
    nome = dados.append(str(input("digite seu nome:")))
    peso = dados.append(int(input("digite seu peso:")))
    pessoas.append(dados[:])
    cont+=1
    dados.clear()
    pq = str(input("quer continuar cadastrando[S/N]?:")).upper().strip()
    if pq == "N":
        break
print(pessoas)
print(f"foram cadastradas {cont} pessoas")
print(f"o maior peso é {maior} e o menor peso é {menor}")