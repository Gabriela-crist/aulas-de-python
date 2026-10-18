from time import sleep
def contador(inicio, meio, passo):
    for c in range(inicio, meio,passo):
        print(c,end=" ")
    print("\n")


contador(1,11,1)
contador(10,0,-2)
a= int(input("digite o inicio: "))
b= int(input("digite o fim:"))
c= int(input("digite de quantos passos deveria contar:"))
contador(a,b,c)