from service.llm import llm
from service.historico_erros import salvar_erro_historico
from models.quiz import Quiz
from models.correcao import Correcao

def gerar_perguntas(tema, quantidade=5):

    gerador = llm.with_structured_output(Quiz)
    quiz = gerador.invoke(f"Crie {quantidade} perguntas curtas sobre {tema} para um estudante de programação. "
        "Para cada uma, dê o gabarito e o tópico específico.")

    return quiz.perguntas

def corrigir_quiz(enunciado, gabarito, resposta_aluno):
    
    juiz = llm.with_structured_output(Correcao)
    return juiz.invoke(f"Pergunta: {enunciado}\nGabarito: {gabarito}\nResposta do aluno: {resposta_aluno}\n"
        "Avalie se a resposta do aluno está correta."
    )


def iniciar_quiz(tema): 

    numero_acertos = 0
    numero_erros = 0 

    perguntas = gerar_perguntas(tema)

    for questao in perguntas:

        resposta_aluno = input(f"{questao.enunciado}\n> ") # print "o que é overtting, por exemplo"
        correcao = corrigir_quiz(questao.enunciado, questao.gabarito, resposta_aluno)

        if correcao.correta:
            numero_acertos += 1

        if not correcao.correta:
            salvar_erro_historico(questao, resposta_aluno)
            numero_erros += 1

        print(correcao.explicacao)

    print(f"Quiz encerrado! Você obteve {numero_acertos} questões corretas e {numero_erros} questões erradas.")


