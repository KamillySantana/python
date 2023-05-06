p1 = [7, 8, 5, 9, 10, 6]
p2 = [8, 7, 9, 9, 9, 8]

# sum = soma, len = quantidade
media_p1 = sum(p1) / len(p1)
media_p2 = sum(p2) / len(p2)

print("Média na prova 1: ", media_p1)
print("Média na prova 2: ", media_p2)

if media_p1 > media_p2:
    print("A turma teve melhor média na prova 1")
elif media_p2 > media_p1:
    print("A turma teve melhor média na prova 2")
else:
    print("A turma teve a mesma média nas duas provas")