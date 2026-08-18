while True:
    nom = input("digite o nome do auluno: ")
    nota = float(input("digite a nota do aluno"))
    per = input("ainda tem aluno para cadastrar? S/N: ").upper().strip()
    while per != "S" and per != "N":
        print("resposta errada, tente novamente!")
        per = str(input("ainda tem aluno para cadastrar? S/N: ")).upper().strip()
    if per == "N" :
        break
    