from google import genai

def extrair_transacoes(texto: str, api_key: str) -> str:

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
        config={"temperature": 0,
        }
    )

    return response.text