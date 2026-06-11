dados = list()
pessoas = list()
while True:
    dados.append(str(input("digite seu nome:")))
    dados.append(int(input("digite seu peso:")))
    pessoas.append(dados[:])
    dados.clear()
    pq = str(input("quer continuar cadastrando[S/N]?:")).upper().strip()
    if pq == "N":
        break
print(pessoas)
