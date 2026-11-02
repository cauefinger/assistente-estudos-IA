from pydantic import BaseModel


class Correcao(BaseModel):

    correta: bool
    explicacao: str
