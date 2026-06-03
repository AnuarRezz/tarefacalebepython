# Um aluno poderá representar a instituiçã o em uma competiçã o se estiver matriculado,
# possuir frequê ncia mínima de 85% e mé dia maior ou igual a 8. Caso participe de projeto de
# pesquisa, a mé dia mínima poderá ser 7. Além disso, deve possuir recomendaçã o de um
# professor ou certificado té cnico. O aluno nã o poderá possuir advertê ncias disciplinares nem
# faltas injustificadas.
# Tarefa: Identifique as regras do problema, solicite os dados necessá rios ao usuá rio e
# desenvolva um algoritmo em Python para determinar o resultado.
print("9. Competição de Tecnologia")

matriculado = input("O aluno está matriculado? (s/n): ") == 's'
advertencias = input("Possui advertências disciplinares? (s/n): ") == 's'
faltas_injustificadas = input("Possui faltas injustificadas? (s/n): ") == 's'

if not matriculado or advertencias or faltas_injustificadas:
    print("Resultado: Participação Negada. Problemas com matrícula, advertências ou faltas.")
else:
    frequencia = float(input("Qual a frequência do aluno? (%): "))
    if frequencia < 85:
        print("Resultado: Participação Negada. Frequência menor que 85%.")
    else:
        recomendacao = input("Possui recomendação de um professor? (s/n): ") == 's'
        certificado = input("Possui certificado técnico? (s/n): ") == 's'
        
        if not recomendacao and not certificado:
            print("Resultado: Participação Negada. Requer recomendação ou certificado.")
        else:
            media = float(input("Qual a média do aluno?: "))
            projeto_pesquisa = input("Participa de projeto de pesquisa? (s/n): ") == 's'
            
            if media >= 8 or (projeto_pesquisa and media >= 7):
                print("Resultado: Participação Aprovada na competição de tecnologia!")
            else:
                print("Resultado: Participação Negada. Média insuficiente.")