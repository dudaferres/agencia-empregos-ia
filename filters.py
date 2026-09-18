import re

def aplicar_filtros_deterministicos(texto_curriculo, anos_experiencia_minima, salario_min, salario_max):
    """
    Aplica filtros determinísticos estritos no currículo do candidato, ANTES de
    acionar qualquer modelo de IA, para otimizar custo e tempo de processamento.
    Parâmetros:
        texto_curriculo (str): O texto extraído do PDF do currículo.
        anos_experiencia_minima (float): Tempo mínimo de experiência exigido pela vaga.
        salario_min (float): Piso do orçamento salarial da vaga.
        salario_max (float): Teto do orçamento salarial da vaga.
    Retorna:
        tuple: (bool indicando aprovação, lista de motivos de reprovação se houver)
    """
    # Converte todo o texto para letras minúsculas para padronizar as buscas
    texto_lower = texto_curriculo.lower()

    # Variável de controle assumindo que o candidato passou inicialmente
    aprovado = True

    # Lista para armazenar os motivos de eventuais desclassificações
    motivos_reprovacao = []

    # --- REGRA 1: Validação do tempo mínimo de experiência em anos ---
    # Expressão regular para capturar padrões como "5 anos de experiência"
    padrao_experiencia = r'(\d+(?:[.,]\d+)?)\s*(?:\+)?\s*anos?\s+de\s+experi[êe]ncia'
    match_experiencia = re.search(padrao_experiencia, texto_lower)

    if not match_experiencia:
        aprovado = False
        motivos_reprovacao.append("Não foi possível identificar os anos de experiência no currículo.")
    else:
        anos_encontrados = float(match_experiencia.group(1).replace(',', '.'))
        if anos_encontrados < anos_experiencia_minima:
            aprovado = False
            motivos_reprovacao.append(
                f"Experiência insuficiente: possui {anos_encontrados} ano(s), "
                f"mínimo exigido é {anos_experiencia_minima} ano(s)."
            )

    # --- REGRA 2: Compatibilidade de faixa salarial com o orçamento da vaga ---
    # Expressão regular para buscar a pretensão salarial informada no currículo
    padrao_salario = r'pretens[ãa]o\s+salarial[:\s]*r?\$?\s*([\d.]+(?:,\d{2})?)'
    match_salario = re.search(padrao_salario, texto_lower)

    if not match_salario:
        aprovado = False
        motivos_reprovacao.append("Não foi possível identificar a pretensão salarial no currículo.")
    else:
        valor_str = match_salario.group(1).replace('.', '').replace(',', '.')
        pretensao_salarial = float(valor_str)
        if not (salario_min <= pretensao_salarial <= salario_max):
            aprovado = False
            motivos_reprovacao.append(
                f"Pretensão salarial (R$ {pretensao_salarial:,.2f}) fora do orçamento da vaga "
                f"(R$ {salario_min:,.2f} - R$ {salario_max:,.2f})."
            )

    # Retorna o status final da triagem e os motivos de corte
    return aprovado, motivos_reprovacao
