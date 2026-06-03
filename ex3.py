# Um cliente terá cré dito aprovado se possuir renda superior a R$ 3.000 e nã o possuir
# restriçõ es financeiras. Clientes que possuem relacionamento com o banco há mais de 5 anos
# podem ser aprovados mesmo com renda menor. O cré dito deve ser negado caso existam
# parcelas em atraso. Todo cliente deve ter um cadastro pré vio e ao realizar aná lise de cré dito,
# o sistema deve validar as regras.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("3. Aprovação de Crédito")

cadastro_previo = input("O cliente possui cadastro prévio? (s/n): ") == 's'

if not cadastro_previo:
    print("Resultado: Análise não pode ser feita. Necessário realizar o cadastro do cliente primeiro.")
else:
    parcelas_atraso = input("O cliente possui parcelas em atraso? (s/n): ") == 's'
    restricoes = input("O cliente possui restrições financeiras? (s/n): ") == 's'
    
    if parcelas_atraso or restricoes:
        print("Resultado: Crédito Negado. Cliente possui parcelas em atraso ou restrições financeiras.")
    else:
        renda = float(input("Qual a renda do cliente? R$ "))
        tempo_banco = int(input("Qual o tempo de relacionamento com o banco (em anos)?: "))
        
        if renda > 3000 or tempo_banco > 5:
            print("Resultado: Crédito Aprovado!")
        else:
            print("Resultado: Crédito Negado. Renda insuficiente e tempo de relacionamento menor que 5 anos.")