from random import randint 
from operator import itemgetter
from time import sleep
dict1 = {'jogador 1 ': randint(0,6),
         'jogador 2 ': randint(0,6),
         'jogador 3 ': randint(0,6),
         'jogador 4 ': randint(0,6)}
dict2 = {}
for i, v in dict1.items():
        print(f"{i}tirou {v} no dado")
        sleep(1)
print("-"*30)
dict2 = sorted(dict1.items(), key=itemgetter(1), reverse=True) # VAI ORGANIZAR O DICIONARIO E POR DO MENOR PARA O MAIOR 
for i, v in enumerate(dict2):
        print(f"{i} lugar: {v[0]} com {v[1]}")
        sleep(2)
        