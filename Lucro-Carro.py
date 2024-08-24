# 10. O custo ao consumidor de um carro novo é a soma do preço da fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos. Calcule e mostre:
# a. O valor correspondente ao lucro do distribuidor
# b. O valor correspondente aos impostos
# c. O preço final do veículo

# Receber Dados
precoDeFabrica = float(input("Digite o Preço de Fábrica do Carro: "))
percentualDeLucro = int (input("Digite o Percentual (%) de Lucro do Distuibidor: "))
percentualDeImpostos = int (input("Digite o Percentual (%) de Impostos Pagos: "))

# Fórmulas
lucroDoDistribuidor = (precoDeFabrica * (1 + (percentualDeLucro/100))) - precoDeFabrica
valorLiquido = (precoDeFabrica * (1 + (percentualDeLucro/100)))
valorDeImpostos = (valorLiquido * (1 + (percentualDeImpostos/100))) - valorLiquido
valorFinal = precoDeFabrica + lucroDoDistribuidor - valorDeImpostos

# Enviar Dados

print("O Distruibidor Lucrará: R$", lucroDoDistribuidor)
print("O Imposto pago será de: R$", valorDeImpostos)


print("O Preço Final do Veículo será de: ", valorFinal)
