import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()   

llm = ChatGroq(model="openai/gpt-oss-120b")

SYSTEM = "Você é um professor de programação com especialidade em Inteligência Artificial paciente. Pergunte de maneira educada qual é a dúvida do usuário, chamando o usuário de estudante. Procure explicar em analogias e em português"

while True:
    response = llm.invoke("Olá! Qual dúvida você quer que eu exclareça hoje?")
    print(response.content)

    if response.lower() == "sair":
        break