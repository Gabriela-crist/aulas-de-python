from time import sleep
def contador(inicio, meio, passo): 
    print("="* 30)
    print(f"contagem de {inicio} ate {meio} de {passo} em {passo}")
    for c in range(inicio, meio,passo):
        print(c,end=" ", flush= True)
        sleep(0.5)       
    print("\n")


contador(0,11,1)
contador(10,0,-2)
a= int(input("digite o inicio: "))
b= int(input("digite o fim:"))
c= int(input("digite de quantos passos deveria contar:"))
contador(a,b,c)
