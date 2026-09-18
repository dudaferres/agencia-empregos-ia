import tiktoken

def calcular_tokens(texto, modelo="gpt-4o-mini"):
    """
    Calcula o número exato de tokens consumidos por um texto para o modelo de IA.
    Parâmetros:
        texto (str): O texto a ser medido.
        modelo (str): Nome do modelo de linguagem.
    Retorna:
        int: Quantidade total de tokens.
    """
    try:
        # Obtém o codificador oficial correspondente ao modelo
        codificador = tiktoken.encoding_for_model(modelo)

        # Converte o texto em uma lista de IDs de tokens
        tokens_lista = codificador.encode(texto)

        # Conta a quantidade de elementos na lista gerada
        return len(tokens_lista)

    except Exception as e:
        # Fallback seguro caso ocorra algum problema com a biblioteca
        print(f"Aviso: Erro ao calcular tokens ({e}). Usando aproximação.")
        return len(texto) // 4
