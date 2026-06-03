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