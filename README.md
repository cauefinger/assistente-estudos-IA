# inteligencia-artificial-inicio
Repositório destinado aos estudos iniciais de Inteligência Artificial, com foco nos conceitos fundamentais, ferramentas e bibliotecas do ecossistema Python.

Versão do LLM utilizada no projeto: Groq 1.7.0
Framework utilizado no projeto: LangChain 1.4.7
Integração entre Groq e LangChain: LangChain-Groq 1.1.3

## 📚 Projeto 1: Assistente de Estudos com IA

Meu primeiro projeto prático de IA: um assistente de estudos que roda no terminal, conversa em linguagem natural e me ajuda a aprender melhor o meu próprio material.

A ideia é simples: em vez de só *usar* uma IA, quero **entender como uma aplicação de IA funciona por dentro**, construindo cada peça passo a passo.

### O que ele vai fazer
- 💬 Conversar como um professor paciente, explicando com analogias
- 🧠 Lembrar do que foi dito durante a conversa
- 📈 Registrar meus erros e mostrar no que preciso melhorar

### Conceitos que estou aprendendo
| Etapa | Conceito |
|---|---|
| Professor paciente | Chamada de LLM, prompts de sistema e personas |
| Memória | Como manter o contexto de uma conversa |
| Registro de erros | Persistência simples em arquivo JSON |

### Próximos passos
Ideias para evoluir depois que a base estiver pronta:
- 📄 Ler e resumir arquivos de estudo
- ❓ Gerar quizzes com saída estruturada
- 🛠️ Tool calling, para o assistente decidir sozinho quando usar cada ferramenta

### Visão de futuro 🔭
Por enquanto o projeto fica no terminal, com JSON. Se tudo correr bem, ele pode crescer em camadas:
1. **FastAPI**: transformar o assistente em rotas (`POST /chat`, `GET /erros`), testando no Insomnia
2. **PostgreSQL no Docker**: trocar o JSON por um banco de verdade

Nada disso é para agora. Primeiro, a base de IA.

### Tecnologias
- **Python**
- **Groq**: LLM
- **LangChain**: framework para orquestrar prompts e memória

### Status
🚧 Em construção. O projeto está sendo desenvolvido etapa por etapa, e o histórico de commits mostra a evolução.
