# Função lambda para converter Celsius para Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

# Função lambda para converter Fahrenheit para Celsius
fahrenheit_to_celsius = lambda f: (f - 32) * 5/9

# Função lambda para converter Celsius para Kelvin
celsius_to_kelvin = lambda c: c + 273.15

# Função lambda para converter Kelvin para Celsius
kelvin_to_celsius = lambda k: k - 273.15

# Função lambda para converter Fahrenheit para Kelvin
fahrenheit_to_kelvin = lambda f: (f + 459.67) * 5/9

# Função lambda para converter Kelvin para Fahrenheit
kelvin_to_fahrenheit = lambda k: (k * 9/5) - 459.67

# Função para solicitar a temperatura e a unidade de medida ao usuário
def converter_temperatura():
    temperatura = float(input("Digite a temperatura: "))
    unidade = input("Digite a unidade de medida (Celsius = C, Fahrenheit = F, Kelvin = K): ")
    
    if unidade.lower() == 'c':
        celsius = temperatura
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit e {kelvin} Kelvin.")

    elif unidade.lower() == 'f':
        fahrenheit = temperatura
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius} graus Celsius e {kelvin} Kelvin.")

    elif unidade.lower() == 'k':
        kelvin = temperatura
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin equivalem a {celsius} graus Celsius e {fahrenheit} graus Fahrenheit.")

    else:
        print("Unidade de medida inválida.")

# Chamada da função para converter a temperatura
converter_temperatura()