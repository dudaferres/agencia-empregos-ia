from reader import extrair_texto_pdf
from filters import aplicar_filtros_deterministicos
from candidato_ia import analisar_candidato_com_ia

def executar_pipeline_agencia_empregos():
    print("=== SISTEMA INTELIGENTE DE TRIAGEM DE CURRÍCULOS (AGÊNCIA DE EMPREGOS) ===")

    # ---------------------------------------------------------
    # CONFIGURAÇÕES DA VAGA
    # ---------------------------------------------------------
    anos_experiencia_minima = 3
    salario_min = 6000
    salario_max = 10000
    dados_vaga = (
        "Vaga: Desenvolvedor(a) Python Pleno | Empresa: TechNova Solutions | "
        "Stack desejada: Python, Django, SQL, AWS | "
        f"Experiência mínima: {anos_experiencia_minima} anos | "
        f"Orçamento: R$ {salario_min} a R$ {salario_max}."
    )

    # Caminho do arquivo PDF do currículo do candidato
    caminho_pdf = "curriculo.pdf"

    # ---------------------------------------------------------
    # PASSO 1: LEITURA E EXTRAÇÃO DO PDF
    # ---------------------------------------------------------
    print(f"\n[Passo 1] Lendo o currículo do candidato a partir do arquivo: {caminho_pdf}...")

    # Tenta extrair o texto de um arquivo PDF real na pasta
    texto_curriculo = extrair_texto_pdf(caminho_pdf)

    # Se o PDF não existir na pasta ou estiver vazio, usa o texto simulado para a aula não parar
    if not texto_curriculo.strip():
        print("-> Aviso: Arquivo PDF não encontrado na pasta. Usando dados simulados para a demonstração.")
        texto_curriculo = (
            "Candidato: Ana Silva. "
            "Cargo pretendido: Desenvolvedora Python Pleno/Senior. "
            "Possui 5 anos de experiencia em desenvolvimento backend. "
            "Pretensao salarial: R$ 8500,00. "
            "Habilidades tecnicas: Python, Django, FastAPI, SQL, AWS."
        )
    else:
        print("-> Texto extraído com sucesso do arquivo PDF real!")

    # ---------------------------------------------------------
    # PASSO 2: APLICAÇÃO DOS FILTROS DETERMINÍSTICOS
    # ---------------------------------------------------------
    print("\n[Passo 2] Aplicando filtros determinísticos (Experiência Mínima / Faixa Salarial)...")
    aprovado_regras, motivos_reprovacao = aplicar_filtros_deterministicos(
        texto_curriculo,
        anos_experiencia_minima,
        salario_min,
        salario_max
    )

    # Valida se o candidato passou na triagem rígida
    if not aprovado_regras:
        print("-> Status: REPROVADO na triagem determinística.")
        print("-> Motivos da desclassificação:")
        for motivo in motivos_reprovacao:
            print(f"   - {motivo}")
        print("-> Processo encerrado. Nenhum recurso de IA foi consumido.")
        return

    print("-> Status: APROVADO na triagem determinística! Prosseguindo para a IA gerar o parecer...")

    # ---------------------------------------------------------
    # PASSO 3 & 4: CAMADA GENERATIVA E CONTROLE DE TOKENS
    # ---------------------------------------------------------
    print("\n[Passo 3 & 4] Acionando Camada Generativa (IA) e monitorando tokens...")

    try:
        parecer_e_resumo, relatorio_tokens = analisar_candidato_com_ia(
            texto_curriculo,
            dados_vaga
        )

        # Exibe os resultados da análise generativa
        print("\n==================================================")
        print("     PARECER E RESUMO EXECUTIVO GERADOS PELA IA    ")
        print("==================================================")
        print(parecer_e_resumo)

        # Exibe o relatório de consumo computacional
        print("\n==================================================")
        print("         RELATÓRIO DE CONSUMO E TOKENS            ")
        print("==================================================")
        print(f"• Modelo Utilizado          : {relatorio_tokens['modelo']}")
        print(f"• Tokens de Entrada (Prompt): {relatorio_tokens['tokens_entrada']}")
        print(f"• Tokens de Saída (Output)  : {relatorio_tokens['tokens_saida']}")
        print(f"• Total de Tokens Consumidos: {relatorio_tokens['tokens_totais']}")
        print("==================================================")

    except Exception as e:
        print(f"[Erro Crítico] Falha ao executar a camada generativa: {e}")

if __name__ == "__main__":
    executar_pipeline_agencia_empregos()
