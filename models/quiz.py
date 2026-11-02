from pydantic import BaseModel
from models.pergunta import Pergunta


class Quiz(BaseModel):

    perguntas: list[Pergunta]
