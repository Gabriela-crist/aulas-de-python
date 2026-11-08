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
#aqui faço a lista de mulheres 
    if dados["genero"] == "fem":
        nomes.append(dados["nome"])
#pessoas maiores que a media de idade 
    if dados["idade"] > media:
        dif.append(dados["nome"])
    lista.append(dados.copy())
#quantidade de pessoas cadastrada
    media= id // len(lista) # media de idade
#confimaçao de cadastro
    while quest != "N" and quest != "S":
        print("resposta errada, tente novamente ")
        quest = input("vai adicionar outro cadastro ?(s/n) ").upper().strip()
    if quest == "N":
        break  
print(f"foram cadastradas {len(lista)} pessoas")
print(f"a media de idade dos cadastrados é {media} anos")
print(f"as mulhesres da lista sao {nomes}")
print(f"as pessoas com a idade a cima da media sao {dif}")
