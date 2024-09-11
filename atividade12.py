# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.


def verificar_aprovacao(nota):
    media_aprovacao = 7
    if nota >= media_aprovacao:
        return "Aprovado"
    else:
        return "Reprovado"

# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Verifica a aprovação e exibe o resultado
resultado = verificar_aprovacao(nota)
print(f"O aluno foi {resultado}.")
