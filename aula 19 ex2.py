import random
dict = {}
for i in range(1,5):
    sort = random.randint(0,10)
    dict['jogador']= (f"o jogador {i}: sorteou o numero: {sort}")
    for i, v in dict.items():
        print(f"{v}")
