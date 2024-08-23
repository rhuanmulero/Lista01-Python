#4.	Leia dois valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".

numero1 = float(input("Digite um Número Qualquer: "))
numero2 = float(input("Digite outro Número Qualquer: "))

verificar = numero1 % numero2

if verificar == 0:
    print("São Múltiplos")
else:
    print("Não São Múltiplos")