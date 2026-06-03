# Uma empresa possui um Data Center com acesso restrito. Um colaborador poderá entrar se
# possuir crachá ativo e autorizaçã o do gestor. O sistema deve permitir cadastro de um crachá
# que possui os seguintes atributos: status, autorização, treinamento e cargo. Funcioná rios da
# equipe de infraestrutura podem entrar sem autorizaçã o do gestor. Entretanto, ninguém
# poderá entrar se estiver com treinamento de segurança vencido.
# Tarefa: Identifique as regras do problema, solicite os dados necessários ao usuário e
# desenvolva um algoritmo em Python para determinar o resultado.
print("1. Controle de Acesso ao Data Center")

treinamento_vencido = input("O treinamento de segurança está vencido? (s/n): ") == 's'

if treinamento_vencido:
    print("Resultado: Acesso Negado. Treinamento de segurança vencido.")
else:
    cracha_ativo = input("O crachá está ativo? (s/n): ") == 's'
    
    if not cracha_ativo:
        print("Resultado: Acesso Negado. Crachá inativo.")
    else:
        cargo_infra = input("O funcionário é da equipe de infraestrutura? (s/n): ") == 's'
        
        if cargo_infra:
            print("Resultado: Acesso Permitido. (Equipe de Infraestrutura)")
        else:
            autorizacao_gestor = input("Possui autorização do gestor? (s/n): ") == 's'
            if autorizacao_gestor:
                print("Resultado: Acesso Permitido. (Autorização do Gestor)")
            else:
                print("Resultado: Acesso Negado. Necessária autorização do gestor para este cargo.")