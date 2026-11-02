from pydantic import BaseModel

class Pergunta(BaseModel):

    pergunta: str
    gabarito: str
    topico: str

class Quiz(BaseModel):

    perguntas: list[Pergunta]

