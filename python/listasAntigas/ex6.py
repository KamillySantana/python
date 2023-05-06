salario = int(input("Defina um valor para o salário mínimo: "))
watts = int(input("quantidade de quilowatts: "))

result = (salario / 7) #valor de 100 watts
result2 = (result / watts) #valor de 1 watts
result3 = (result2 * watts)
desconto = (0.1 * result3)
desconto2 = (result3 - desconto)

print("O valor do quilowatts:", result2)
print("O valor a ser pago:", result3)
print("O valor a ser pago com desconto de 10% é:", desconto2)