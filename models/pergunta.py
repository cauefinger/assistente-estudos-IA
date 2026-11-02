from pydantic import BaseModel


class Pergunta(BaseModel):

    enunciado: str
    gabarito: str
    topico: str
