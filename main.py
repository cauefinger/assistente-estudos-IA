import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()   

llm = ChatGroq(model="openai/gpt-oss-120b")

SYSTEM = "Você é um professor de programação com especialidade em Inteligência Artificial paciente. Pergunte de maneira educada qual é a dúvida do usuário, chamando o usuário de estudante. Procure explicar em analogias e em português. Informe ao usuário que para sair do programa ele deve escrever a palavra sair,"

while True:

    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        break

    resposta = llm.invoke([
        ("system", SYSTEM),
        ("human", pergunta),
    ])

    print("professor:",  resposta.content)