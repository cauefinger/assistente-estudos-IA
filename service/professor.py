import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()   

llm = ChatGroq(model="openai/gpt-oss-120b")

SYSTEM = "Você é um professor de programação com especialidade em Inteligência Artificial paciente.  Procure explicar em português. Não diga olá nem cumprimente, faça isso apenas se o usuário cumprimentar. Você deve tirar as dúvidas"

def conversar():

    print("Iniciando a conversa com seu professor tech de inteligência artificial! Para sair do programa, basta digitar 'sair'.")

    historico = [("system", SYSTEM)]    

    while True:

        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            break

        historico.append(("human", pergunta))

        resposta = llm.invoke(historico)

        historico.append(("ai",resposta.content))

    

        print("professor:",  resposta.content)