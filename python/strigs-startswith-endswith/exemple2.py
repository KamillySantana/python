texto = 'Olá Mundo!'
texto_centro = texto.center(20)
texto_centro_2 = texto.center(20,'=')
texto_esquerda = texto.ljust(12)
texto_direita = texto.rjust(12)
print(f'**{texto_esquerda}*{texto_direita}**')

nomes2 = "João Paulo\nMaria Paula\nAna Beatriz\nJosé Pedro"
print(nomes2.splitlines())