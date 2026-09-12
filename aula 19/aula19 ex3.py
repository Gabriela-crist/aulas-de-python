from datetime import date
dict={}
dict2= {}
ano= date.today().year
dict["nome:"]= input("digite seu nome: ")
dict["ano de nascimento: "]=int(input("digite o ano que voce nasceu: "))
dict["num carteira: "]= input("carteira de trabalho (0 se nao tem):")
#aqui vou confirmar a data da carteira caso tenha uma
if dict["num carteira: "] != 0:
    dict["carteira: "]=int(input("digite o ano da de contrataçao : "))
#aqui deve calcular o ano de carteira 
    dict2["ctps: "]= ano - dict["carteira: "]
dict2["idade: "]= ano - dict["ano de nascimento: "]
#aqui calcula a aposentadoria
aposen= 35 - dict2["ctps: "]
if dict2["ctps: "] < 35:
     dict2["apos: "]= (f"faltam {aposen} anos para vc aposentar")
elif dict2["ctps: "] == 35:
    dict2["apos: "]= (f"voce tem {aposen} anos de carteira, ja pode aposentar")
elif dict2["ctps: "] > 35:
    dict2["apos: "]= (f"voce ja é ou deveria estar aposentado")
print(30*"_-_")
#printando e organizando o dicionario em linhas separadas
for i,v in dict2.items():
    print(f"{i}{v}")

