filmes = {}

filmes['Wall-E'] = {"Vilão": "AUTO", "ano": 2008}
filmes['Meu Malvado Favorito 1'] = {"Vilão": "Vector", "ano": 2010}
filmes['Enrolados'] = {"Vilão": "Mãe Gothel", "ano": 2011}
filmes['Minions'] = {"Vilão": "Scarlet", "ano": 2015}
filmes['Zootopia'] = {"Vilão": "Bellwether", "ano": 2016}

print(filmes)
print("\n")

while True:
    filme_novo = input("Digite o nome do filme (0 para sair): ")
    if filme_novo == "0":
        break
    vilao_novo = input("Digite o nome do vilão: ")
    ano_novo = input("Digite o ano do filme: ")

    filmes[filmes] = {"vilão": vilao_novo, "ano": ano_novo}
print(filmes)

pesquisa = ("digite o filme procurado: ")
if pesquisa in filmes:
    print(filmes[pesquisa])
