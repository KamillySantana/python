# Não podemos acrescentar, apagar ou fazer atribuições aos seus itens
tupla_carros = "golf", "corolla", "civic", "opala", "tucson", "elantra"
*carros, tucson, elantra = tupla_carros
print(f"Carros: {carros}")
print(f"Tucson: {tucson}")
print(f"Elantra: {elantra}")

