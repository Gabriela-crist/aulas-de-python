def ficha(jog=0, gols=0):
    print(f'O jogador {jog} fez {gols} gols no campeonato ')


n = str(input("Nome do jogador: "))
g= str(input("numero de gols:"))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    n= "<desconhecido>"
    ficha(n,gols=g)
else:
    ficha(n,g)
