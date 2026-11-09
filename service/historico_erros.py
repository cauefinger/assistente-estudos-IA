from datetime import datetime
from pathlib import Path
import json


PASTA_DADOS = Path(__file__).resolve().parent.parent / "data"
PASTA_DADOS.mkdir(exist_ok=True)
ARQUIVO = PASTA_DADOS / "erros.json"


def carregar_erros():
    if not ARQUIVO.exists():
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Aviso: erros.json está corrompido. Começando uma lista vazia.")
        return []


def salvar_erro_historico(questao, resposta_aluno):
    erros = carregar_erros()
    erros.append({
        "topico": questao.topico,
        "enunciado": questao.enunciado,
        "sua_resposta": resposta_aluno,
        "gabarito": questao.gabarito,
        "data": datetime.now().isoformat(timespec="seconds"),
    })
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(erros, f, ensure_ascii=False, indent=2)


