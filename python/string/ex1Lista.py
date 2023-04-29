lista = []
soma = sum(lista)
multiplicacao = 1
maior = max(lista)
menor = min(lista)

while True:
    acrescentar = int(input("Informe um número para acrescentar a lista (0 para parar): "))

    lista.append(acrescentar)
    print(lista)

    if (acrescentar == 0):
        break

for x in lista:
    multiplicacao *= acrescentar