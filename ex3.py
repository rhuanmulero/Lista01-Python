# 3. Calcule a média aritmética das quatro notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 6, ou a mensagem "reprovado", caso contrário.

nota1 = float(input("Digite a Nota do Primeiro Bimestre: "))
nota2 = float(input("Digite a Nota do Segundo Bimestre: "))
nota3 = float(input("Digite a Nota do Terceiro Bimestre: "))
nota4 = float(input("Digite a Nota do Quarto Bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("A Nota Final foi: ", media)

if media >= 6:
    print("APROVADO :)")
else:
    print("Reprovado :(")