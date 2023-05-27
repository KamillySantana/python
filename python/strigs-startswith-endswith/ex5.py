frase = input("Digite uma frase: ")

# Contar os espaços em branco
espacos = frase.count(' ')

# Contar as vogais
vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')

print("Quantidade de espaços em branco:", espacos)
print("Quantidade de vogais (a, e, i, o, u):", vogais)
