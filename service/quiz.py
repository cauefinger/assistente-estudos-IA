from pydantic import BaseModel
from service.llm import llm

class Pergunta(BaseModel):

    pergunta: str
    gabarito: str
    topico: str

class Quiz(BaseModel):

    perguntas: list[Pergunta]

def gerar_perguntas(tema, quantidade=5):

    # TODO: cirar um arquivo LLM e importar ele pra cá e pro professor

    gerador = llm.with_structured_output(Quiz)
    quiz = gerador.invoke(f"Crie {quantidade} perguntas curtas sobre {tema} para um estudante de programação. "
        "Para cada uma, dê o gabarito e o tópico específico.")

    return quiz.perguntas