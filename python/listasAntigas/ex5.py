numero = int(input("Informe um número de 3 digitos: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 10) 

print(numero, "\nunidade", unidade, "\ndezena", dezena, "\ncentena", centena)
