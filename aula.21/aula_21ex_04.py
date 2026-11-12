def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else: 
            print("\033[1;31m ERRO!, DIGITE UM NUMERO VALIDO.\033[0;0m")
        if ok:
            break
    return valor

n = leiaint("digite um numero:")
print(f"voce acabou de digitar o numero {n}")
