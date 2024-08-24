# 6. Leia dois números inteiros e mostre o maior deles. Caso sejam iguais informe ao usuário.

# Receber Dados
numero1 = float(input("Digite Um Número Qualquer: "))
numero2 = float(input("Digite Outro Número Qualquer: "))

# Enviar Dados
if numero1 > numero2:
    print("O número", numero1, "é maior que o número", numero2)
elif numero1 < numero2:
    print("O número", numero2, "é maior que o número", numero1)
else:
    print("Os números são iguais")
