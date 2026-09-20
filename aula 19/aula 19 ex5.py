dados = {}
lista= []
while True:
    dados["nome"]= input("NOME: ")
    dados["genero"]= input("GENERO: ")
    dados["idade"]= input("IDADE: ")
    quest = input("vai adicionar outro cadastro ?(s/n) ").upper().strip()
    lista.append(dados.copy())
    while quest != "N" and quest != "S":
        print("resposta errada, tente novamente ")
        quest = input("vai adicionar outro cadastro ?(s/n) ").upper().strip()
    if quest == "N":
        break
for i in range(len(lista)):
    
print(lista)
