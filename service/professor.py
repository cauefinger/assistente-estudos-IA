import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()   

llm = ChatGroq(model="openai/gpt-oss-120b")

SYSTEM = "Você é um professor de programação com especialidade em Inteligência Artificial paciente.  Procure explicar em português. Não diga olá nem cumprimente, faça isso apenas se o usuário cumprimentar. Você deve tirar as dúvidas"

def conversar():

    print("Iniciando a conversa com seu professor tech de inteligência artificial! Para sair do programa, basta digitar 'sair'.")
    
    while True:

        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            break

        # "invocar" LLM e adicionar as tuplas.

        resposta = llm.invoke([
            ("system", SYSTEM),
            ("human", pergunta),
    ])

        print("professor:",  resposta.content)