# 13. Receba dois números, o primeiro deve ser maior que 10 e menor que 25, o segundo deve ser maior ou igual a zero, o terceiro deve ser a soma dos dois primeiros e o quarto é o produto dos três números anteriores. Calcule e exiba a soma dos quadrados de cada um dos quatro números. Caso o resultado seja menor que 50000, solicite novos dados. 

def programa():

    while True:
        # Receber Dados
        numero1 = int(input("Digite um Número Maior que 10 e Menor que 25: "))

        while numero1 < 10 and numero1 > 25: # Validação das Condições do Número 1
            numero1 = int(input("Digite um Número Maior que 10 e Menor que 25: "))

        numero2 = int(input("Digite um Número Maior ou Igual a Zero (0): "))

        while numero2 < 0 and numero2 != 0: # Validação das Condições do Número 2
            numero2 = int(input("Digite um Número Maior ou Igual a Zero (0): "))

        # Cálculos
        numero3 = numero1 + numero2
        numero4 = numero1 * numero2 * numero3
        somaDosQuadrados = pow(numero1, 2) + pow(numero2, 2) + pow(numero3, 2) + pow(numero4, 2)

        # Enviar Dados
        if somaDosQuadrados >= 50000:
            print("A Soma dos Quadrados deu: ", somaDosQuadrados)
            break
        else:
            print("A Soma dos Quadrados deu: ", somaDosQuadrados, "O Resultado deveria ser: 50.000")
            print("O Resultado é menor que 50000..., por favor, reenvie os dados!")
  
programa()
