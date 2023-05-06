print("Informe um número para saber se é maior ou menor que 0")

while True:
    def verificar(numero):
        if numero > 0:
            return 'P'
        else:
            return 'N'

    valor = float(input("Número: "))
    resultado = verificar(valor)
    print("O Resultado é:", resultado)