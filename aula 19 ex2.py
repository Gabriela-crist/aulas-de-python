import random
dict = {}
for i in range(0,5):
    sort = random.randint(0,10)
    dict['jogador']= (f"o jogador{i} sorteou o numero{sort}")

print(dict.items())