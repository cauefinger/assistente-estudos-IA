from dotenv import load_dotenv
from service.historico import carregar_historico, salvar_historico
from service.llm import llm
from service.quiz import iniciar_quiz
from service.historico_erros import carregar_erros

load_dotenv()   


SYSTEM = "Você é um professor de programação com especialidade em Inteligência Artificial paciente.  Procure explicar em português. Não diga olá nem cumprimente, faça isso apenas se o usuário cumprimentar. Você deve tirar as dúvidas"

def conversar():

    print("Iniciando a conversa com seu professor tech de inteligência artificial! Para sair do programa, basta digitar 'sair'. Para um quiz, digite '/quiz tema', e para verificar os erros e pontos para melhorar, digite um '/erros'!")

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

        if entrada.lower() == "/erros":

            erros = carregar_erros()
            resposta = llm.invoke(f"Você tem os seguintes erros registrados do usuário: {erros}. \n Preciso que você monte uma avaliação com base nesses erros e esclareça onde ele tem que melhorar.")
            print(f"Professor: ", resposta.content)
            continue

        if not erros:
            print("Você não tem erros registrados ainda. Faça um /quiz para testar seus conhecimentos na área!")
            continue
        
        historico.append(("human", entrada))

        resposta = llm.invoke(historico) # resposta com base no histórico

        historico.append(("ai", resposta.content))
        salvar_historico(historico)

        print("professor:",  resposta.content)

