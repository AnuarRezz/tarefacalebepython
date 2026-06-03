# Uma reserva poderá ser realizada se o auditó rio estiver disponível e a solicitaçã o for feita
# por um professor ou coordenador. Para realizar reserva, o usuá rio deve efetuar o login, com
# e-mail e senha. Caso o evento seja institucional emergencial, a reserva poderá ocorrer
# mesmo sem disponibilidade pré via, desde que autorizada pela direçã o. As informaçõ es
# sobre o evento, devem ser informadas por cada usuá rio solicitante.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("4. Reserva de Auditório")

email = input("E-mail para login: ")
senha = input("Senha: ")
print(f"Login efetuado com sucesso para {email}.")

cargo = input("Qual o cargo do solicitante? (professor/coordenador/outro): ")
if cargo not in ['professor', 'coordenador']:
    print("Resultado: Reserva Negada. Apenas professores e coordenadores podem solicitar.")
else:
    evento = input("Informe os detalhes/nome do evento: ")
    auditorio_disponivel = input("O auditório está disponível na data desejada? (s/n): ") == 's'
    
    if auditorio_disponivel:
        print(f"Resultado: Reserva confirmada para o evento '{evento}'.")
    else:
        emergencial = input("O evento é institucional emergencial? (s/n): ") == 's'
        if emergencial:
            autorizacao_direcao = input("Possui autorização da direção? (s/n): ") == 's'
            if autorizacao_direcao:
                print(f"Resultado: Reserva emergencial confirmada para o evento '{evento}'.")
            else:
                print("Resultado: Reserva Negada. Falta autorização da direção para evento emergencial.")
        else:
            print("Resultado: Reserva Negada. Auditório indisponível e não é um evento emergencial autorizado.")