def somaImposto(taxaImposto, custo):
    imposto = custo * taxaImposto / 100
    custo_total = custo + imposto
    return custo_total

taxa = float(input("Digite a taxa de imposto: "))
valor_custo = float(input("Digite o custo do item: "))

valor_total = somaImposto(taxa, valor_custo)
print("Valor total com imposto:", valor_total)