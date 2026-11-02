from pathlib import Path     
import json


PASTA_DADOS = Path(__file__).resolve().parent.parent / "data"
PASTA_DADOS.mkdir(exist_ok=True)
ARQUIVO = PASTA_DADOS / "historico.json"


def carregar_erros(system):
    if ARQUIVO.exists():
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
        return [tuple(msg) for msg in dados]
    return [("system", system)]


def salvar_erro_historico(historico):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)
