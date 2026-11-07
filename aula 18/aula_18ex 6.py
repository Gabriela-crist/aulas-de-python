list= []
listnt= []
while True:
    list.clear()
    nom = input("digite o nome do auluno: ").upper()
    nota1 = float(input("digite a nota do aluno: "))
    nota2 = float(input("digite a 2ª nota do mesmo aluno: "))
    media = (nota1 + nota2) / 2
    per = input("ainda tem aluno para cadastrar? S/N: ").upper().strip()
    list.append(nom)
    list.append(media)
    listnt.append(list.copy())
    while per != "S" and per != "N":
        print("resposta errada, tente novamente!")
        per = str(input("ainda tem aluno para cadastrar? S/N: ")).upper().strip()
    if per == "N" :
        break
print(f"{'*'*10}BOLETIM GERAL:{'*'*10}")
for aluno in listnt:
    print(aluno[0],f"{aluno[1]:.1f}")
aluno= input("DIGITE O NOME DO ALUNO QUE DESEJA CONSULTAR INDIVIDUALMENTE: ").upper()
for i in range(len(listnt)):
    if listnt[i][0] == aluno :
         print(f"O ALUNO: {listnt[i][0]} \nTEVE DE MEDIA: {listnt[i][1]}")



