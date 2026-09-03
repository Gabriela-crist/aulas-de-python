from datetime import date
dict={}
dict2= {}
ano= date.today().year
dict["nome:"]= input("digite seu nome: ")
dict["ano de nascimento:"]=int(input("digite o ano que voce nasceu: "))
dict["num carteira"]= input("carteira de trabalho (0 se nao tem):")
if dict["num carteira"] != 0:
    dict["carteira: "]=int(input("digite o ano da de contrataçao : "))
    dict2["ctps"]= ano - dict["carteira: "]
dict2["idade"]= ano - dict["ano de nascimento:"]
if dict2["ctps"] < 35:
     aposen= 35 - dict2["ctps"]
     dict2["apos"]= (f"faltam {aposen}anos para vc aposentar")
elif dict2["ctps"] >= 35:
    dict2["apos"]= (f"voce tem {dict2["ctps"]} anos de carteira, ja pode aposentar")
print(dict2)
