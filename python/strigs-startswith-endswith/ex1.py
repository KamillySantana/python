primeira = input("Digite o primeiro texto: ")
segunda = input("Digite o segundo texto: ")

#Informações sobre o comprimento
tamanho_primeira = len(primeira)
tamanho_segunda = len(segunda)

#Comparação do comprimento e conteúdo
if tamanho_primeira == tamanho_segunda:
    print("Os texto têm o mesmo comprimento.")
    if primeira == segunda:
        print("Os texto têm o mesmo conteúdo.")
    else:
        print("Os texto têm conteúdo diferente.")
else:
    print("Os texto têm comprimentos diferentes.")