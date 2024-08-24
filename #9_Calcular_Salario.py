# 9. Cálculo de um salário líquido de um professor. Serão fornecidos via teclado o valor da hora aula, número de aulas dadas e o % de desconto do INSS.

# Receber Dados
valor = float(input("Digite o Valor da Hora-Aula: "))
aulas = int(input("Digite a Quantidade de Aulas Dadas: "))
desconto = int(input("Digite o Valor da % que é descontado para o INSS: "))

# Cálculo do Salário
salario = (valor * aulas) * (1 - (desconto/100))

# Enviar Dados
print("O Salário Líquido é de: R$", salario)

