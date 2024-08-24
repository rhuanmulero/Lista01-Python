# 8. Informar um preço de um produto. Calcule e exiba o preço com desconto de 9% e o preço com reajuste de 10%.

# Receber Dados
precoProduto = float(input("Digite o Preço de um Produto: "))

# Fórmulas
desconto = precoProduto * 0.91
novoPreco = precoProduto * 1.1
novoPrecoComDesconto = novoPreco * 0.9

# Enviar Dados
print("O Preço Antigo com Desconto de 9% é: ", desconto)
print("O Preço com Reajuste de 10% foi para: ", novoPreco)
print("O Novo Preço com Desconto de 9% é de: ", novoPrecoComDesconto)
