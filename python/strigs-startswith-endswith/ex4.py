meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = input("Digite a data de nascimento (dd/mm/aaaa): ")
# Separar o dia, mês e ano
dia, mes, ano = data.split('/')

# Converter de string para inteiros
dia = int(dia)
mes = int(mes)
ano = int(ano)

# Verificar se o mês é válido
if mes < 1 or mes > 12:
    print("Mês inválido!")
else:
    # Obter o nome do mês por extenso
    nome_mes = meses[mes - 1]

    # Imprimir a data com o nome do mês por extenso
    print(f'Data de nascimento: {dia} de {nome_mes} de {ano}')

