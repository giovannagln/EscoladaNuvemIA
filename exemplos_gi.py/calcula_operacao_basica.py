"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição,
subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com
diversos tipos de erros de entrada e operação. Siga as especificações abaixo:
A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja
concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números Divisão por zero, operação inválida,Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""

def calculadora():
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: Entrada inválida. Digite um número válido.")

    while True:
        try:
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: Entrada inválida. Digite um número válido.")

    while True:
        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            try:
                resultado = num1 / num2
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
                continue
        else:
            print("Erro: Operação inválida. Tente novamente.")
            continue

        # Arredonda o resultado para 2 casas decimais
        resultado = round(resultado, 2)
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break

# Executa a calculadora
calculadora()
