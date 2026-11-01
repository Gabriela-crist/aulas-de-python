from time import sleep
def maior(*num):
    cont= maior = 0
    print('analisando valores...')
    for valor in num:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f"foram cadastrados {cont} valores")
    print(f"o maior valor foi {maior}")
maior(0,3,4,5,6,7)
maior(3,4,52,3,9)
maior(3,6,4,9,2)
