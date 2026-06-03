# Um aluno poderá se candidatar aos projetos de IC se possuir mé dia maior ou igual a 8 e
# frequê ncia superior a 80%. Os dados serã o validados no sistema acadê mico. Cada aluno
# deve ter um cadastro pré vio para validaçã o, o docente faz uma pesquisa informando a turma
# e o nome do aluno. Caso o discente pesquisado cumpra todas as regras dos projetos de IC, o
# sistema deve imprimir: apto.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("7. Seleção para IC")

cadastro_previo = input("O aluno possui cadastro prévio no sistema acadêmico? (s/n): ") == 's'

if not cadastro_previo:
    print("Aluno não encontrado no sistema acadêmico.")
else:
    turma = input("Docente, informe a turma para pesquisa: ")
    nome_aluno = input("Docente, informe o nome do aluno: ")
    
    print(f"Validando dados de {nome_aluno} da turma {turma}...")
    
    media = float(input(f"Qual a média registrada para {nome_aluno}?: "))
    frequencia = float(input(f"Qual a frequência registrada para {nome_aluno}?: "))
    
    if media >= 8 and frequencia > 80:
        print("apto")
    else:
        print("inapto")