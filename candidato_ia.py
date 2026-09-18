from token_tracker import calcular_tokens

def analisar_candidato_com_ia(texto_curriculo, dados_vaga):
    """
    Simula o envio do currículo e dos dados da vaga para um modelo generativo,
    gerando um parecer qualitativo e um resumo executivo fictícios (didáticos)
    e calculando rigorosamente os tokens de entrada e saída.
    Parâmetros:
        texto_curriculo (str): O texto completo extraído do currículo do candidato.
        dados_vaga (str): As informações da vaga (título, empresa, stack desejada).
    Retorna:
        tuple: (str com o parecer + resumo gerados pela IA simulada, dict com o relatório detalhado de tokens)
    """
    # Define o nome do modelo simulado para fins de relatório
    modelo_utilizado = "gpt-4o-mini-simulado"

    # Configura o System Prompt (Instrução de papel que define o contexto do modelo)
    prompt_sistema = (
        "Você é um Recrutador Técnico Sênior especializado em tecnologia, "
        "responsável por avaliar a senioridade, as soft skills implícitas e a "
        "aderência de candidatos às vagas de uma agência de empregos."
    )

    # Configura o User Prompt (A janela de contexto que injeta os dados dinâmicos da execução)
    prompt_usuario = f"""
    Com base no currículo do candidato descrito abaixo e nos dados da vaga,
    gere um parecer qualitativo sobre a senioridade/soft skills e um resumo
    executivo para o recrutador da empresa contratante.

    --- DADOS DA VAGA ---
    {dados_vaga}

    --- CURRÍCULO DO CANDIDATO ---
    {texto_curriculo}
    """

    # --- CONCEITO DE CONTEXTO E TOKENS DE ENTRADA ---
    # Tudo o que é enviado para o modelo (System + User) forma a "Janela de Contexto".
    # Calculamos exatamente quantos tokens essa entrada consome.
    texto_total_entrada = prompt_sistema + prompt_usuario
    tokens_entrada = calcular_tokens(texto_total_entrada, modelo_utilizado)

    # --- SIMULAÇÃO DA RESPOSTA DO MODELO GENERATIVO ---
    # Em vez de chamar uma API na nuvem, geramos uma resposta estruturada baseada no contexto.
    # (heurística simples apenas para tornar a simulação didaticamente coerente)
    texto_lower = texto_curriculo.lower()
    if "sênior" in texto_lower or "senior" in texto_lower:
        senioridade_estimada = "Sênior"
    elif "pleno" in texto_lower:
        senioridade_estimada = "Pleno"
    else:
        senioridade_estimada = "Júnior"

    texto_resposta = (
        "--- PARECER E RESUMO EXECUTIVO GERADOS PELA IA (SIMULAÇÃO DIDÁTICA) ---\n\n"
        f"**Parecer Qualitativo:** O candidato aparenta possuir perfil de nível "
        f"{senioridade_estimada}, com boa organização na descrição das experiências, "
        "o que sugere comunicação estruturada. Recomenda-se validar em entrevista "
        "competências de liderança e trabalho em equipe, que não ficam explícitas "
        "apenas na leitura do currículo.\n\n"
        "**Resumo Executivo para o Recrutador:** Perfil tecnicamente compatível com "
        "os requisitos da vaga informada, com experiência e stack alinhadas ao "
        "briefing repassado pela empresa contratante. Recomendado para prosseguir "
        "no processo seletivo."
    )

    # --- CONCEITO DE TOKENS DE SAÍDA ---
    # Medimos quantos tokens a resposta gerada pelo modelo consumiu
    tokens_saida = calcular_tokens(texto_resposta, modelo_utilizado)

    # --- RELATÓRIO COMPUTACIONAL DE TOKENS ---
    # Consolida as métricas para demonstrar o custo computacional da operação
    relatorio_tokens = {
        "modelo": modelo_utilizado,
        "tokens_entrada": tokens_entrada,
        "tokens_saida": tokens_saida,
        "tokens_totais": tokens_entrada + tokens_saida
    }

    # Retorna o parecer/resumo simulado e o dicionário completo de tokens
    return texto_resposta, relatorio_tokens
