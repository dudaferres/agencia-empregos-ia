from pypdf import PdfReader

def extrair_texto_pdf(caminho_arquivo):
    """
    Abre o PDF do currículo do candidato e extrai todo o texto contido nele.
    Parâmetros:
        caminho_arquivo (str): O caminho para o arquivo PDF do currículo.
    Retorna:
        str: O texto bruto extraído de todas as páginas.
    """
    try:
        # Inicializa o objeto leitor de PDF com o arquivo fornecido
        leitor = PdfReader(caminho_arquivo)

        # Cria uma string vazia para acumular o texto de todas as páginas
        texto_acumulado = ""

        # Itera por cada página contida no documento PDF
        for pagina in leitor.pages:
            # Extrai o texto da página atual
            texto_pagina = pagina.extract_text()

            # Verifica se a página realmente contém texto (evita falhas em páginas vazias)
            if texto_pagina:
                # Concatena o texto da página ao acumulador geral com quebra de linha
                texto_acumulado += texto_pagina + "\n"

        # Retorna o texto completo extraído do currículo
        return texto_acumulado

    except Exception as e:
        # Trata eventuais erros de leitura ou arquivos corrompidos
        print(f"Erro ao ler o arquivo PDF {caminho_arquivo}: {e}")
        return ""
