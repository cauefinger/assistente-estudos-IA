from pydantic import BaseModel
from service.llm import llm
from service.historico_erros import salvar_erro_historico

class Pergunta(BaseModel):

    enunciado: str
    gabarito: str
    topico: str

class Correcao(BaseModel):

    correta: bool
    explicacao: str

class Quiz(BaseModel):

    perguntas: list[Pergunta]

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

    perguntas = gerar_perguntas(tema)

    for questao in perguntas:

        resposta_aluno = input(f"{questao.enunciado}\n> ")
        correcao = corrigir_quiz(questao.enunciado, questao.gabarito, resposta_aluno)

        if not correcao.correta:
            salvar_erro_historico(questao, resposta_aluno)

        print(correcao.explicacao)
