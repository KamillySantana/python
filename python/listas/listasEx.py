lista = []
listaPar = []
listaImpar = []
somaPar = 0
somaImpar = 0

while True:
    acrescentar = int(input("Informe um número para acrescentar a lista (0 para parar): "))

    lista.append(acrescentar)
    print(lista)

    if (acrescentar == 0):
        break

# percorrer a lista
for x in lista:
    if x % 2 == 0:
        listaPar.append(x)
        somaPar += x
    else:
        listaImpar.append(x)
        somaImpar += x

# imprimir os resultados
listaPar.sort() # coloca em crescente
listaImpar.sort()

print('-=' * 30)
print(f"Os numeros pares são: {listaPar} e sua somatória é {somaPar}")
print(f"Os numeros impares são: {listaImpar} e sua somatória é {somaImpar}")
print('-=' * 30)

