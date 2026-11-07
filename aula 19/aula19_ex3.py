from datetime import date
dict={}
ano= date.today().year
dict["nome:"]= input("digite seu nome: ").upper()
nasc= int(input("digite o ano que voce nasceu: "))
dict["idade: "]= date.today().year - nasc
dict["ctps: "]= input("carteira de trabalho (0 se nao tem):")
#aqui vou confirmar a data da carteira caso tenha uma e calcular a aposentadoria
if dict["ctps: "] != "0"  :
    dict["carteira: "]=int(input("digite o ano da de contrataçao : ")) 
    dict["slario: "]=  float(input("salario: R$"))
    dict["aposentadoria: "]= dict["idade: "] + ((dict["carteira: "]+ 35)- date.today().year)
print(30*"_-_")
#printando e organizando o dicionario em linhas separadas
for i,v in dict.items():
    print(f"  -{i} tem o valor {v}")

