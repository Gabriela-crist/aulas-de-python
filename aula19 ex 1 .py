dict = {}
dict["Nome do Aluno: "]= input("nome do aluno:")
dict["Media do Aluno: "]= float(input("qual a media desse aluno:"))
if dict["Media do Aluno: "] >= 6:
    dict["Situaçao do Aluno: "]= ("Aprovado")
else:
    dict["Situaçao do Aluno:"]= ("Reprovado")
print("*"*20)
for i,v in dict.items():
    print(f"{i}{v}")

