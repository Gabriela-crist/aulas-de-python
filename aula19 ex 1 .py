dict = {}
dados= []
while True:
    dict["nome"]= input("nome do aluno:")
    dict["media"]= input("qual a media desse aluno:")
    dados.append(copy(dict))
    per= input
    print(dados)