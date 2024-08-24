#5.	Receba dois valores a e b e os escreve com a mensagem: "São pares " ou "São ímpares".

numero1 = float(input("Digite um Número Qualquer: "))
numero2 = float(input("Digite outro Número Qualquer: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos os Números são Pares")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print("Apenas o Número", numero1, "é par\nO Número", numero2, "é Ímpar")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print("Apenas o Número", numero2, "é par\nO Número", numero1, "é Ímpar")
else:
    print("Ambos os Números são Ímpares")
