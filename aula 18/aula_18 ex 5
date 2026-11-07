import  random 
list= []
listfim= []
num = int(input("Quantos palpites do jogo voce precisa: "))
#no primeiro for ja deixei feito para que ele limpe a lista para que os palpites estejam separados
for i in range(num):
    list.clear()
#nesse segundo for ele vai sortear o numero a partir da biblioteca random ridint
    for i in range(0,6):
        list.append(random.randint(1, 60))
#por sugestao do gpt o copy foi a melhor opçao para conseguir imprimir um em baixo do outro depois 
    listfim.append(list.copy())
print("Os palpites sao :".upper())
#o * faz com que o python leia a lista por partes e nao ela inteira, oq facilita usar o sep= \n para pular linha 
print(*listfim, sep="\n")

