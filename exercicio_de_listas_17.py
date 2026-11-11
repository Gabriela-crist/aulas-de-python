print( "verificador de parenteses")

num = input("DIGITE SUA OPERAÇAO ALGEBRICA: ")
pilha =[]
for i in num:
    if i == "(":
        pilha.append("(")
    elif i == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("sua conta esta correta")
else:
    print("sua conta esta errada verifique os parenteses")
    