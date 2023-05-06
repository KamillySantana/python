# string(letras) usa aspas, número n
lista = ["A", "B", "C"]
print(lista[1])
# se eu coloco -1 ele vai printar na tela o ultimo valor da lista no caso o 7, se fosse -2 seria o C

# ele acrescenta algo na lista, sem mexer la em cima
lista.append("D")
print(lista)

lista = lista + ["E", "F"]
print(lista)

# insert vai acrescentando a lista, na posição que eu colocar, ex na posição 3 vai colocar cahorro
lista.insert(3, "cachorro")
print(lista)

# remove da lista
lista.remove("cachorro")
print(lista)

# enverte a ordem
lista.sort(reverse=True)
print(lista)

# conta os valores da lista, ex só tem 1 A na lista, ai ele vai conta
print(lista.count("A"))

# vai tira o ultimo valor da lista e colocar em baixo
var = lista.pop()
print(lista)
print(var)

# apaga da lista até onde eu quero, ex do 0 a 2
del lista[0:2]
print(lista)


