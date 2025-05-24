"""
Calculadora da Média 
alunos 
"""


N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a primeira nota: "))
N3 = float(input("Digite a primeira nota: "))
N4 = float(input("Digite a primeira nota: "))

media = (N1 * 2 + N2 * 3 + N3* 4* 1) / 10

print(f"Média: {media:.1f}")

if media >= 7 :
    print ("Aluno aprovado")
elif media < 5 :
    print ("Aluno reprovado")
else:
    print ("Aluno em exame.")
    exame = float(input("Digite a nota do exame:"))
    print (f"Nota do exame: {exame:.1f}")

    media_final = (media + exame) / 2

    if media_final >= 5:
        print("Aluno aprovado")
    else:
        print ("Aluno reprovado")
    print (f"Média final: {media_final:.1f}")