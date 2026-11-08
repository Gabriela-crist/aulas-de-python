jogador = dict()
part = []
jogador["nome"]= input("nome do jogador: ")
tot= int(input(f"quantas partidas o {jogador["nome"]} jogou?: "))
for c in range(0, tot):
    part.append(int(input(f"quantos gols {jogador["nome"]} fez na partida {c}?: ")))
jogador["gols:"]= part[:]
jogador["totalgols:"]= sum(part)
print(30*'_-')
print(f"O jogador {jogador["nome"]} jogou {len(jogador["gols:"])} partidas.")
for i, v  in enumerate(jogador["gols:"]):
    print(f"  => na partida {i}, fez {v} gols")
print(f"foi um total de {jogador["totalgols:"]} gols")



