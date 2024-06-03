from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import datetime

nome = "Willian Yoshio Murayama"
minicurso = "Introdução à linguagem Python"
dia = "20/12/2023"

# Para cada fonte que deseja utilizar, eh necessario registrar por essa funcao
registerFont(TTFont("Pacifico", "Pacifico-Regular.ttf"))
registerFont(TTFont("Inter Regular", "Inter-Regular.ttf"))
registerFont(TTFont("Inter Light", "Inter-Light.ttf"))

# Define o tamanho do documento, por padrao eh o tamanho da folha A4 em paisagem
pdf = canvas.Canvas(
    "nome.pdf",
    pagesize=(A4[1], A4[0]),
)
# pdf.setFontSize(56)

# Definimos a fonte que sera escrito no comeco
pdf.setFont("Pacifico", 50)

# Funcao que escreve string, tem como parametro a posicao no documento e a string
pdf.drawCentredString(
    A4[1] / 2,
    A4[0] - 50,
    "Certificado",
)

# Quando desejar alterar a fonte, eh necessario utilizar o set e o tamanho da fonte
pdf.setFont("Inter Light", 12)
# pdf.drawString(10,10,"Centro Acadêmico de Ciência da Computação - CACiC")

# Ha diversas funcoes que escrevem string em diferentes posicoes
pdf.drawRightString(A4[1] - 10, 10, f"Hacktoberfest 2023")
pdf.setFont("Inter Regular", 12)

estilo = ParagraphStyle(name="Estilo", fontName="Inter Regular", fontSize=14)

# Podemos tambem escrever um paragrafo inteiro aplicando um determinado estilo
texto = Paragraph(
    f"""Certificamos que {nome} realizou o curso de {
        minicurso} que foi realizado no dia {dia}.""",
    estilo,
)
# texto.drawOn(pdf,100,A4[1]-70)
# Chamamos o metodo wrapon para definir o tamanho do paragraph
texto.wrapOn(pdf, A4[1] - 100, A4[0] - 100)
# Chamamos o metodo drawon para escrever onde queremos
texto.drawOn(pdf, 50, A4[0] - 110)
estilo_autoria = ParagraphStyle(
    "Estilo autoria", fontName="Inter Regular", alignment=1)

# Podemos utilizar tambem tags html dentro da funcao paragraph
autoria = Paragraph(
    "Willian Yoshio Murayama<br/>Presidente do Centro Acadêmico<br/>de Ciência da Computação<br/>CACiC",
    estilo_autoria,
)

# Chamamos o metodo wrapon para definir o tamanho do paragraph
autoria.wrapOn(pdf, 300, 300)
# Chamamos o metodo drawon para escrever onde queremos
autoria.drawOn(pdf, (A4[1] - 300) / 2, 150)

estilo_rodape = ParagraphStyle(
    name="Estilo rodape",
    fontName="Inter Light",
)

rodape = Paragraph(
    f"Centro Acadêmico de Ciência da Computação - CACiC<br/>Certificado gerado em {
        datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}"
)

rodape.wrapOn(pdf, A4[1], A4[0])
rodape.drawOn(pdf, 10, 10)
# pdf.drawCentredString("Willian Yoshio Murayama")
pdf.setAuthor("Willian Murayama")
pdf.save()
