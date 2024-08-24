# 7. Tendo como dados de entrada a altura e o sexo de uma pessoa (1 masculino e 2 feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. para homens: (72.7*h)-58
# b. para mulheres: (62.1*h)-44.7

# Receber Dados
altura = float(input("Digite sua Altura (Exemplo: 1.62): "))
sexo = int(input("Escolha seu Sexo (1 para Masculino e 2 para Feminino): "))

# Fórmulas
pesoIdealHomem = (72.7 * altura) - 58
pesoIdealMulher = (62.1 * altura) - 44.7

# Enviar Dados
if sexo == 1:
    print("Seu Peso Ideal é: ", pesoIdealHomem)
elif sexo == 2:
    print("Seu Peso Ideal é: ", pesoIdealMulher)
else:
    print("Opção não válida")
