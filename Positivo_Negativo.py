#2.	Receba via teclado um número inteiro qualquer e exiba se ele é positivo ou negativo ou zero.

numero = int(input("Digite Um Número Inteiro Qualquer: "))

if numero > 0:
    print("Esse número é positivo")
elif numero < 0:
    print("Esse número é negativo")
else:
    print("Esse número é o 0")
