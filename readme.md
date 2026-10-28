# Organizador de Extrato Bancário com IA

O objetivo é extrair dados de extratos bancários utilizando Inteligência Artificial. Sem a necessidade de criar uma estrutura rígida de código para capturar os dados ou fazer tratamentos complexos para a extração. A IA lê o texto bruto e estrutura os dados, deixando apenas o tratamento básico de colunas e limpeza com o Pandas.

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) 
- [Google GenAI SDK](https://pypi.org/package/google-genai) 
- [pdfplumber](https://github.com/jsvine/pdfplumber) 
- [Pandas](https://pandas.pydata.org/)

---

## 🚀 Como Rodar 

1. Criar o ambiente virtual
```bash
python3 -m venv venv
```
2. Ativar o ambiente virtual
```bash


source venv/bin/activate
```
3. Instalar as dependências
```Bash

pip install streamlit pdfplumber google-genai pandas python-dotenv
```
4. Configurar .env
```
API_GEMINI=sua_chave_aqui
```
5. Executar a Aplicação
```Bash
streamlit run app.py
```
