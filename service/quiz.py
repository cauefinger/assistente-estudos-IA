from pydantic import BaseModel

class Pergunta(BaseModel):

    pergunta: str
    gabarito: str
    topico: str

