from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def criar_pdf():
    nome_arquivo = "curriculo.pdf"

    # Cria o documento PDF na pasta atual
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    largura, altura = letter

    # Escreve as informações que o leitor de PDF vai capturar
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, altura - 50, "AGENCIA DE EMPREGOS TECH - CURRICULO DO CANDIDATO")

    c.setFont("Helvetica", 11)
    c.drawString(50, altura - 90, "------------------------------------------------------------------------------------------------")
    c.drawString(50, altura - 120, "Nome do Candidato: Ana Silva")
    c.drawString(50, altura - 150, "Cargo Pretendido: Desenvolvedora Python Pleno/Senior")
    c.drawString(50, altura - 180, "Experiencia: Possui 5 anos de experiencia em desenvolvimento backend.")
    c.drawString(50, altura - 210, "Pretensao Salarial: R$ 8500,00")
    c.drawString(50, altura - 240, "Habilidades Tecnicas: Python, Django, FastAPI, SQL, AWS.")
    c.drawString(50, altura - 270, "------------------------------------------------------------------------------------------------")

    # Salva o arquivo no disco
    c.save()
    print(f"Sucesso! O arquivo '{nome_arquivo}' foi gerado na pasta.")

if __name__ == "__main__":
    criar_pdf()
