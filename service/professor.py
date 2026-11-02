import os 
from dotenv import load_dotenv
from service.historico import carregar_historico, salvar_historico
from service.llm import llm
from service.quiz import iniciar_quiz


load_dotenv()   


SYSTEM = "Você é um professor de programação com especialidade em Inteligência Artificial paciente.  Procure explicar em português. Não diga olá nem cumprimente, faça isso apenas se o usuário cumprimentar. Você deve tirar as dúvidas"

def conversar():

    print("Iniciando a conversa com seu professor tech de inteligência artificial! Para sair do programa, basta digitar 'sair'. Para um quiz, digite '/quiz tema'.")

    historico = carregar_historico(SYSTEM)

    while True:

        entrada = input("Você: ")

        if entrada.lower() == "sair":
            break

        if entrada.lower().startswith("/quiz"):
            tema = entrada[5:].strip()
            if not tema:
                print("Informe o tema, por exemplo: /quiz redes neurais")
            else:
                iniciar_quiz(tema)
            continue

        historico.append(("human", entrada))

        resposta = llm.invoke(historico) # resposta com base no histórico

        historico.append(("ai", resposta.content))
        salvar_historico(historico)

        print("professor:",  resposta.content)