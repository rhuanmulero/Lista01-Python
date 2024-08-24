# 11. Leia o preço de um produto e inflaciona esse preço em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100.

# Receber Dados
preco = float(input("Digite o Preço de um Produto: "))

# Cálculos
if preco < 100:
    novoPreco = preco * 1.1

else:
    novoPreco = preco * 1.2

# Enviar Dados
print("O Novo Preço é de: R$", novoPreco)
