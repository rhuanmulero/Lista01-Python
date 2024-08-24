# 12. Elabore um programa que receba o salário de um funcionário e calcule o reajuste desse salário. Considere que o funcionário deve receber um reajuste de 15% caso seu salário seja menor que 800 reais. Se o salário for maior ou igual a 800 e menor ou igual a 1000, seu reajuste será de 10 %; caso seja maior que 1000, o reajuste deve ser de 5%. Ao final do programa deve apresentar o valor antigo e o novo salário.

# Receber Dados
salario = float(input("Digite o Valor do seu Salário: "))

# Cálculos
if salario < 800:
    salario = salario * 1.15

elif salario >= 800 and salario <= 1000:
    salario = salario * 1.1

else:
    salario = salario * 1.05

# Enviar Dados
print("Seu novo Salário é de: R$", salario)
