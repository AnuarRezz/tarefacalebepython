# Um aluno poderá ser monitor se possuir mé dia maior ou igual a 8 e frequê ncia superior a
# 85%. Alunos com certificaçã o profissional poderã o participar com mé dia mínima de 7. Nã o
# podem participar alunos com advertê ncias ou reprovaçã o na disciplina.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("6. Seleção para Monitoria")

advertencias = input("O aluno possui advertências? (s/n): ") == 's'
reprovacao = input("O aluno possui reprovação na disciplina da monitoria? (s/n): ") == 's'

if advertencias or reprovacao:
    print("Resultado: Inscrição Negada. Possui advertências ou reprovação.")
else:
    frequencia = float(input("Qual a frequência do aluno? (%): "))
    if frequencia <= 85:
         print("Resultado: Inscrição Negada. Frequência insuficiente.")
    else:
        media = float(input("Qual a média do aluno?: "))
        certificacao = input("O aluno possui certificação profissional na área? (s/n): ") == 's'
        
        if media >= 8 or (certificacao and media >= 7):
            print("Resultado: Inscrição Aprovada para a monitoria!")
        else:
            print("Resultado: Inscrição Negada. Média insuficiente.")