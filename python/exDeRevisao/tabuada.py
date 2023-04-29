while True:
    numero = int(input("Informe um numero para treinar a tabuada: "))
    acertos = 0
    erros = 0

    for x in range (1,11):
        resultado = numero * x
        resposta = int(input(f"{numero} x {x} = "))

        if (resposta == resultado):
            print("parabéns está correto, vai abraça sua mãe")
            acertos += 1
        else:
            print(f"Que pena, você é burro, o valor correto é {resultado}")
            erros += 1

    print("-=" * 20)
    print(f"Total de acertos: {acertos}")
    print(f"Total de erros: {erros}")
    print("-=" * 20)
    
    opcao = input("Deseja começar de novo? (s/n): ")
    if opcao == 'n':
        break
