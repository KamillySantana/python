cidade = 'São Carlos'
endereco = 'Rua Cândido Padim, 25 - Vila Prado'
completo = cidade + endereco
print(cidade.startswith('São'))
print(cidade.endswith('los'))
print('Rua' in completo)
print('Avenida' not in completo)

texto = 'Python é uma linguagem de programação. Python é simples. Python é organizado. Python é uma excelente linguagem.'
print(texto.count('é')) #conta as letras de acordo com o que voce especificar.
print(texto.find('Python',25,50)) #find para obter a posição da primeira ocorrência de uma String.
print(texto.rfind('lingua')) #rfind para realizar a pesquisa da direita para a esquerda.
print(texto.index('é')) #Para localizar o índice de ocorrência de uma string, podemos usar
print(texto.rindex('é')) #também o index e rindex.

