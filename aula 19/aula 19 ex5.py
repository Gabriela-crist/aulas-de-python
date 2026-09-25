dados = {}
lista= []
nomes= []
dif= []
cont= id= media= 0
while True:
    dados["nome"]= input("NOME: ")
    dados["genero"]= input("GENERO: ")
    idade = int(input("IDADE: "))
    id +=idade
    dados["idade"]= idade
    quest = input("vai adicionar outro cadastro ?(s/n) ").upper().strip()
    if dados["genero"] == "fem":
        nomes.append(dados["nome"])
    lista.append(dados.copy())
    while quest != "N" and quest != "S":
        print("resposta errada, tente novamente ")
        quest = input("vai adicionar outro cadastro ?(s/n) ").upper().strip()
    if quest == "N":
        break
    for i in range(len(lista)):
            cont+=1
    media= id // cont
    if dados["idade"] > media:
            dif.append(dados["nome"])
print(dif)
print(f"as mulhesres da lista sao {nomes}")
print(f"a media de idade dos cadastrados é {media} anos") 
print(f"foram cadastradas {cont} pessoas")

