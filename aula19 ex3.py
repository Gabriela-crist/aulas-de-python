from datetime import date
dict={}
dict2= {}
dict["nome:"]= input("digite seu nome: ")
dict["ano de nascimento:"]=int(input("digite o ano que voce nasceu: "))
dict["carteira: "]=int(input("digite o ano da ctps: "))
ano= date.today().year
dict2["idade"]= ano - dict["ano de nascimento:"]
dict2["ctps"]= ano - dict["carteira: "]
if dict2["ctps"] < 35:
     aposen= 35 - dict2["ctps"]
     dict2["apos"]= (f"faltam {aposen}anos para vc aposentar")
elif dict2["ctps"] >= 35:
    dict2["apos"]= (f"voce tem {dict2["ctps"]} anos de carteira, ja pode aposentar")
print(dict2)
