import random

jogador = input("Informe o nome do jogador: ")

lista = ("pedra", "papel", "tesoura")
computador = random.choice(lista)

escolha = -1
while escolha < 0 or escolha > 2:
    escolha = int(input(jogador + ''', escolha entre:

        [0] pedra 
        [1] papel 
        [2] tesoura
        
Qual é a sua jogada: '''))
    
    if (escolha < 0 or escolha > 2):
        print("\nPresta atenção, burro \n")

print('-=' * 20)
print("jo")
print("ken")
print("POO")
print('-=' * 20)

print("computador jogou: " + computador)
print (jogador + " jogou: " + lista[escolha])
print('-=' * 20)


if (computador == "pedra" and escolha == 0):
    print("Empate")
elif (computador == "pedra" and escolha == 1):
    print(jogador + " Venceu")
elif (computador == "pedra" and escolha == 2):
    print(jogador + " perdeu :(")

elif (computador == "papel" and escolha == 0):
    print(jogador + " perdeu :(")
elif (computador == "papel" and escolha == 1):
    print("Empate")
elif (computador == "papel" and escolha == 2):
    print(jogador + " Venceu")

elif (computador == "tesoura" and escolha == 0):
    print(jogador + " Venceu")
elif (computador == "tesoura" and escolha == 1):
    print(jogador + " perdeu :(")
elif (computador == "tesoura" and escolha == 2):
    print("Empate")
