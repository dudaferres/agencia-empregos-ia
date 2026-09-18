# Agência de Empregos Tech — Triagem Automatizada de Currículos

Checkpoint 1 — IA&ML — Engenharia de Software — FIAP

## 📋 Descrição

Sistema em Python para uma agência de empregos focada no ecossistema de
tecnologia. O sistema automatiza a triagem de currículos em PDF combinando:

1. **Camada Determinística (`filters.py`)** — filtros rígidos de regras de
   negócio (experiência mínima e faixa salarial), aplicados **antes** de
   qualquer chamada de IA, para reduzir custo e tempo de processamento.
2. **Camada Generativa (`candidato_ia.py`)** — para os candidatos aprovados,
   uma IA (simulada, seguindo o mesmo modelo didático usado em sala) gera um
   parecer qualitativo sobre senioridade/soft skills e um resumo executivo
   customizado para o recrutador.
3. **Monitoramento de Tokens (`token_tracker.py`)** — contagem exata de
   tokens de entrada e saída com `tiktoken`, exibida em um relatório de
   consumo ao final de cada execução.

> A camada de IA **não faz chamadas a nenhuma API paga**: ela monta os
> prompts (system + user) normalmente, calcula os tokens reais desses
> prompts com `tiktoken`, e gera uma resposta simulada, exatamente como
> demonstrado em sala de aula. Isso permite validar todo o fluxo de
> engenharia (extração → filtros → IA → tokens) sem custo e sem depender de
> chave de API.

## 🗂️ Estrutura de pastas

```
agencia-empregos-ia/
├── reader.py           # Leitura e extração de texto do PDF do currículo
├── filters.py          # Camada determinística (filtros rígidos)
├── candidato_ia.py      # Camada generativa (IA simulada) + prompts
├── token_tracker.py     # Cálculo de tokens (tiktoken) e fallback seguro
├── gerar_pdf.py         # Gera um currículo de exemplo em PDF (reportlab)
├── main.py              # Orquestrador do pipeline (ponto de entrada)
├── curriculo.pdf        # Currículo de exemplo gerado por gerar_pdf.py
├── integrantes.md
├── requirements.txt
└── README.md
```

## ⚙️ Configuração do ambiente

1. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Como executar

1. **Gere o currículo de exemplo em PDF:**

   ```bash
   python gerar_pdf.py
   ```

   Isso cria o arquivo `curriculo.pdf` na pasta do projeto, com os dados de
   uma candidata fictícia (Ana Silva, 5 anos de experiência, pretensão
   salarial de R$ 8.500). Você pode editar os dados diretamente em
   `gerar_pdf.py` para testar outros perfis (por exemplo, um candidato com
   pouca experiência ou pretensão salarial fora do orçamento, para ver o
   sistema reprovando na triagem determinística).

2. **Execute a triagem:**

   ```bash
   python main.py
   ```

   O sistema vai:
   - Ler o `curriculo.pdf` (ou usar dados simulados, se o arquivo não existir);
   - Aplicar os filtros determinísticos (experiência mínima e faixa salarial
     da vaga, configurados no início de `main.py`);
   - Se aprovado, acionar a camada de IA (simulada) para gerar o parecer
     qualitativo e o resumo executivo;
   - Exibir o relatório de tokens (entrada, saída e total) e o modelo usado.

   Se o candidato for **reprovado** nos filtros determinísticos, o sistema
   encerra o processo e **nenhum token é consumido** — essa é justamente a
   otimização de custo pedida no enunciado.

## 🧩 Como funciona cada camada

### 1. Extração de PDF (`reader.py`)
Usa `pypdf` para abrir o currículo e concatenar o texto de todas as páginas.

### 2. Filtros determinísticos (`filters.py`)
Usa expressões regulares para extrair do texto do currículo:
- Os **anos de experiência** citados (ex: "5 anos de experiência");
- A **pretensão salarial** informada (ex: "Pretensão salarial: R$ 8500,00").

E valida se ambos atendem aos requisitos da vaga (experiência mínima e faixa
salarial), retornando aprovação/reprovação e os motivos, se houver.

### 3. Camada generativa (`candidato_ia.py`)
Monta um **system prompt** (papel do recrutador) e um **user prompt** (dados
da vaga + currículo), calcula os tokens dessa entrada, gera uma resposta
simulada (parecer + resumo executivo) e calcula os tokens dessa saída.

### 4. Monitoramento de tokens (`token_tracker.py`)
Usa `tiktoken.encoding_for_model()` para contar tokens de forma exata, com
fallback (aproximação de 1 token a cada 4 caracteres) caso a biblioteca
encontre algum problema (por exemplo, falta de conexão com a internet na
primeira execução, quando os arquivos de encoding ainda não estão em cache).
