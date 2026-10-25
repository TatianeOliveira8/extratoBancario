import streamlit as st
import pdfplumber
from google import genai
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

st.title(" Organizador de Extrato Bancário")
st.write("Faça o upload do seu extrato bancário em PDF para começar")

api_key = os.getenv("API_GEMINI")

arquivo_pdf = st.file_uploader('Escolha um arquivo PDF', type='pdf')

if arquivo_pdf is not None:
    st.success("Arquivo enviado!")

    
    with pdfplumber.open(arquivo_pdf) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"

    if st.button("Processar com IA"):
        if not api_key:
            st.error("chave api invalida")
        else:
            with st.spinner("Processando com IA..."):

                client = genai.Client(api_key=api_key)
                prompt = f"""
                Analise o texto do extrato bancário abaixo. 
                Extraia todas as transações de saída de dinheiro (compras, pagamentos de fatura, débitos).
                Para cada transação, traga estritamente no seguinte formato separado por pipe (|):
                Data | Estabelecimento Limpo | Valor (ex: 45.90) | Categoria (Alimentação, Transporte, Lazer, Contas, Compras, Fatura, Outros)

                Regra importante para a Categoria:
                - Se for pagamento de fatura do cartão (ex: "Pagamento de fatura"), categorize obrigatoriamente como "Fatura".

                Não adicione texto explicativo antes ou depois, apenas as linhas no formato pedido.

                Texto do extrato:
                {texto}
                """

                response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=prompt,
                )

                st.subheader("Transações extraídas:")
                st.text(response.text)

                try:
                    linhas = response.text.strip().split("\n")
                    dados_tratados = []

                    for linha in linhas:
                        partes = linha.split('|')
                        if len(partes) == 4:
                            dados_tratados.append(partes)

                    df = pd.DataFrame(dados_tratados, columns=['Data', 'Estabelecimento', 'Valor', 'Categoria'])

                    df["Valor"] = df["Valor"].str.replace("R$", "", regex=True).str.strip()
                    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")

                    st.subheader("Tabela Organizada (Pandas):")
                    st.dataframe(df, use_container_width=True)

                    st.subheader("Total Gasto por Categoria:")
                    resumo = df.groupby("Categoria")["Valor"].sum().reset_index()
                    total_gasto = resumo["Valor"].sum()
                    linha_total = pd.DataFrame({"Categoria": ["TOTAL GERAL"], "Valor": [total_gasto]})
                    resumo = pd.concat([resumo, linha_total], ignore_index=True)

                    st.dataframe(resumo, use_container_width=True)

                except Exception as e:
                    st.error(f"Erro ao processar a tabela com o Pandas: {e}")

    st.write("Texto extraído do PDF:")
    st.text_area("Texto do PDF", texto, height=300)
