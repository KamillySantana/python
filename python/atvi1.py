produtos = ["tomate", "batata", "limão"]
estoque = [100, 200, 50]
min_estoque = [10, 20, 5]

for num in range(3):
    print(f'O produto {produtos[num]}, tem estoque de {estoque[num]} e no minimo de {min_estoque[num]}')

while True:
    informe = input("Digite o nome do produto: ")
    qnt = int(input("digite a quantidade do produto: "))
    min = int(input("digite o minimo de estoque para este produto: "))
    adicionar = input("deseja adicionar mais algun produto? (s/n): ")

    produtos.append(informe)
    estoque.append(qnt)
    min_estoque.append(min)

    for num in range(len(produtos)):
        if estoque[num] <= min_estoque[num]:
            print(f'O Produto {produtos[num]} com quantidade minina')

    lista = []
    for num in range(len(produtos)):
        lista.append([produtos[num], estoque[num], min_estoque[num]])
    print(lista)

    if adicionar == "n":
        break

while True:
    remover = input("Digite o nome do produto para ser apagado: ")
    if remover in produtos:
        break
    else:
        print("Produto não encontrado")
ind = produtos.index(remover)
produtos.remove(remover)
estoque.remove(estoque[ind])
min_estoque.remove(min_estoque[ind])
print(produtos, estoque, min_estoque)

pedidos = []
while True: 
    ped_prod = input("Digite o produto que deseja comprar: ")
    ped_qnt = int(input("Digite a quantidadede produtos: "))
    pedidos.append([ped_prod, ped_qnt])
    repete = input("deseja continuar (S/N): ")
    if repete.upper() == "N":
        break
print(pedidos)

for itens in pedidos:
    if itens[0] not in produtos:
        print(f'produto {itens[0]} não tem')
    elif itens[1] < estoque[produtos.index(itens[0])]:
        print(f'saldo insuficiente de {itens[0]}!')
