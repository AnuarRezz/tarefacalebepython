# Um produto poderá ser vendido se houver estoque disponível e o item estiver ativo.
# Produtos reservados nã o podem ser vendidos. Gerentes podem autorizar a venda de itens
# inativos para descarte, desde que exista estoque. Para validar os dados de cada produto, ele
# deve estar cadastrado no sistema. O vendedor deve pesquisar o produto por nome e
# adicionar ao carrinho, se o produto nã o cumpre alguma das regras, o sistema deve
# apresentar uma mensagem informando qual regra nã o é satisfeita e voltar ao menu de
# seleçã o de produto. Caso o cliente desista da compra, o vendedor deve possuir permissã o
# para sair do menu. Se o produto está inativo, o vendedor pode solicitar a operaçã o para
# descarte (zerar estoque) no menu, assim o sistema irá pedir senha de administrador. O
# gerente poderá realizar a autorizaçã o com a senha de administrador, a venda poderá ser
# concluída.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("8. Controle de Estoque")

produto_cadastrado = True 
estoque = 10

while True:
    print("\n--- Menu de Vendas ---")
    acao = input("Deseja (1) Pesquisar/Vender Produto ou (2) Sair do menu? ")
    
    if acao == '2':
        permissao_sair = input("Vendedor possui permissão para sair/cancelar? (s/n): ") == 's'
        if permissao_sair:
            print("Saindo do sistema...")
            break
        else:
            print("Erro: Sem permissão para cancelar operação.")
            continue
            
    elif acao == '1':
        nome_produto = input("Digite o nome do produto: ")
        
        if not produto_cadastrado:
            print("Regra não satisfeita: Produto não cadastrado.")
            continue
        
        if estoque <= 0:
            print("Regra não satisfeita: Sem estoque disponível.")
            continue
            
        reservado = input("O produto está reservado? (s/n): ") == 's'
        if reservado:
            print("Regra não satisfeita: Produto reservado não pode ser vendido.")
            continue
            
        ativo = input("O produto está ativo? (s/n): ") == 's'
        if ativo:
            print("Produto adicionado ao carrinho e venda concluída com sucesso!")
            estoque -= 1
        else:
            print("O produto está inativo.")
            descarte = input("Deseja solicitar operação para descarte (zerar estoque)? (s/n): ") == 's'
            if descarte:
                senha_admin = input("Digite a senha de administrador (gerente): ")
                if senha_admin == "admin123": 
                    print("Autorização concedida! Venda para descarte concluída.")
                    estoque = 0
                else:
                    print("Regra não satisfeita: Senha incorreta. Autorização negada.")
            else:
                print("Operação cancelada. Voltando ao menu.")