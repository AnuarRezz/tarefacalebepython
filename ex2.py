# Um estudante poderá participar do intercâ mbio se possuir mé dia maior ou igual a 8,
# frequê ncia mínima de 80% e passaporte vá lido. Alunos que participam de projetos de
# pesquisa podem participar mesmo com mé dia mínima de 7. Caso possuam advertê ncia
# disciplinar, a inscriçã o deverá ser negada.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("2. Programa de Intercâmbio")

advertencia = input("Possui advertência disciplinar? (s/n): ") == 's'

if advertencia:
    print("Resultado: Inscrição Negada. Aluno possui advertência disciplinar.")
else:
    passaporte_valido = input("Possui passaporte válido? (s/n): ") == 's'
    frequencia = float(input("Qual a porcentagem de frequência do aluno? (Ex: 85): "))
    media = float(input("Qual a média do aluno?: "))
    projeto_pesquisa = input("Participa de projeto de pesquisa? (s/n): ") == 's'
    
    if not passaporte_valido or frequencia < 80:
        print("Resultado: Inscrição Negada. Requisitos de passaporte ou frequência não atendidos.")
    elif media >= 8 or (projeto_pesquisa and media >= 7):
        print("Resultado: Inscrição Aprovada para o intercâmbio!")
    else:
        print("Resultado: Inscrição Negada. Média insuficiente.")