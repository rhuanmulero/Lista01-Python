# 14. Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente. O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o preço total, usando a tabela abaixo:

# Código do Produto | Preço Unitário
# 1001                          5.32
# 1324                          6.45
# 6548                          2.37
# 0987                          5.32
# 7623                          6.45

# Receber Informações
codigo = input("Digite o Código do Produto: ")

while codigo not in [1001, 1324, 6548, "0987", 7623]:
    codigo = input("Digite um Código Válido: ")

unidade = int(input("Digite a Quantidade de Unidades Compradas: "))

while unidade < 0:
    codigo = int(input("Digite um Código Válido: "))

# Enviar Dados

if codigo == 1001:
    valor = 5.32 * unidade
    print("Compra Total: R$", valor)

if codigo == 1324:
    valor = 6.45 * unidade
    print("Compra Total: R$", valor)

if codigo == 6548:
    valor = 2.37 * unidade
    print("Compra Total: R$", valor)

if codigo == "0987":
    valor = 5.32 * unidade
    print("Compra Total: R$", valor)

if codigo == 7623:
    valor = 6.45 * unidade
    print("Compra Total: R$", valor)