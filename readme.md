# 📊 Organizador de Extrato Bancário com IA

O objetivo é extrair dados de extratos bancários utilizando Inteligência Artificial. Sem a necessidade de criar uma estrutura rígida de código para capturar os dados ou fazer tratamentos complexos de extração: a IA lê o texto bruto e estrutura os dados, deixando apenas o tratamento básico de colunas e limpeza a cargo do Pandas.

---

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) (Interface gráfica)
* [Google GenAI SDK](https://pypi.org/package/google-genai) (Modelo Gemini Flash Lite)
* [pdfplumber](https://github.com/jsvine/pdfplumber) (Extração de texto de PDFs)
* [Pandas](https://pandas.pydata.org/) (Manipulação e estruturação de dados)

---

## 📋 User Stories

| Prioridade | User Story |
| --- | --- |
| **Alta** | Como desenvolvedor, quero extrair as informações do extrato utilizando IA, para que eu não precise criar regras complexas ou tratamentos pesados de extração na arquitetura do software. |
| **Alta** | Como usuário, quero ver todas as minhas transações detalhadas (separadas por data, estabelecimento, valor e categoria), para que eu possa acompanhar meus gastos de forma clara. |
| **Média** | Como usuário, quero visualizar uma tabela com o total de gastos por categoria junto com o total geral, para que eu possa identificar facilmente onde estou gastando mais. |