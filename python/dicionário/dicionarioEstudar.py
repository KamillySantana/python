# Um dicionário consiste em um conjunto de chaves e valores, parece uma lista.
# para criar dicionario ultiliza-se {}

# chave = curso, aula, professor
# valor = Python, Dicionario, Fernando
dic = {"curso": "Python", "aula": "Dicionario", "professor": "Fernando", "Aleatorio": "teste"}

# Acessamos um elemento utilizando a chave
# chamou a chave professor e curso
print(f'Professor {dic["professor"]} que da aula do curso de {dic["curso"]}')

print("\n") # pula linha

# para adicionar elementos ao dicionario usamos a chave pra fazer a alteração
dic["aula"] = "Dicionario - Aula08"
print(dic)

print("\n")

# Para apagar dicionário dic.clear()
