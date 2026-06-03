# Um aluno poderá retirar livros se possuir cadastro ativo, nã o possuir multas pendentes e
# tiver menos de cinco livros emprestados. Alunos bolsistas podem retirar livros mesmo com
# cinco empré stimos ativos. Nenhum empré stimo poderá ocorrer se o cadastro estiver
# bloqueado. Cada aluno deve ter um cadastro com suas informaçõ es. Ao solicitar
# empré stimo, seus dados devem ser validados seguindo as regras de empré stimo. Se
# satisfazer as regras, o empré stimo deve ser criado e as informaçõ es salvas para consulta
# futura.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("5. Controle de Biblioteca")

cadastro_status = input("Qual o status do cadastro do aluno? (ativo/bloqueado/inativo): ")

if cadastro_status == 'bloqueado':
    print("Resultado: Empréstimo Negado. Cadastro bloqueado.")
elif cadastro_status != 'ativo':
    print("Resultado: Empréstimo Negado. Cadastro não está ativo.")
else:
    multas = input("O aluno possui multas pendentes? (s/n): ") == 's'
    if multas:
        print("Resultado: Empréstimo Negado. O aluno possui multas pendentes.")
    else:
        livros_emprestados = int(input("Quantos livros o aluno já possui emprestados?: "))
        bolsista = input("O aluno é bolsista? (s/n): ") == 's'
        
        if livros_emprestados < 5 or bolsista:
            nome_livro = input("Qual o nome do livro que deseja retirar?: ")
            print(f"Resultado: Empréstimo do livro '{nome_livro}' aprovado e registrado com sucesso!")
        else:
            print("Resultado: Empréstimo Negado. Limite de 5 livros atingido (regra exclusiva para não bolsistas).")