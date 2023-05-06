while True:
    sim = input("você gosta de python ? (sim/não): ")
    # upper converte todos os caracteres minusculos em uma string para maiusculos
    sim = sim.upper()

    if sim == "SIM":
        print("Resposta correta!")
        break
    else:
        print("Esta resposta não é correta, tente novamente")


