# 15. Leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:
# MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME)/7
# A atribuição de conceitos obedece a tabela abaixo:

# Média de Aproveitamento | Conceito
# 9,0	                  | A
# 7,5 e < 9,0	          | B
# 6,0 e < 7,5	          | C
# 4,0 e < 6,0	          | D
# < 4,0	                  | E

# O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A, B ou C e REPROVADO se o conceito for D ou E.

# Receber Dados
id = int(input("Digite o Número de Identificação do Aluno: "))
nota1 = float(input("Digite a Primeira Nota do Aluno: "))
nota2 = float(input("Digite a Segunda Nota do Aluno: "))
nota3 = float(input("Digite a Terceira Nota do Aluno: "))
mediaExercicio = float(input("Digite a Nota da Média dos Exercícios do Aluno: "))

# Calcular a Média de Aproveitamento
mediaAproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + mediaExercicio)/7

# Conceito de Notas
if mediaAproveitamento >= 9:
    conceitoAproveitamento = "A"
    situacao = "APROVADO :)"
elif 7.5 <= mediaAproveitamento < 9:
    conceitoAproveitamento = "B"
    situacao = "APROVADO :)"
elif 6 <= mediaAproveitamento < 7.5:
    conceitoAproveitamento = "C"
    situacao = "APROVADO :)"
elif 4 <= mediaAproveitamento < 6:
    conceitoAproveitamento = "D"
    situacao = "REPROVADO :("
else:
    conceitoAproveitamento = "E"
    situacao = "REPROVADO :("

# Enviar Dados
print("\nO Nº de Identifição do Aluno: ", id)
print("\n\nNOTAS DO ALUNO\nPrimeira Nota: ", nota1, "\nSegunda Nota: ", nota2, "\nTerceira Nota: ", nota3, "\nMédia dos Exercícios: ", mediaExercicio)
print(f"Média de Aproveitamento: {mediaAproveitamento:.2f}", "\nConceito: ", conceitoAproveitamento, "\nSituação: ", situacao)
