from openpyxl import load_workbook
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

#Carrega planilha
wb = load_workbook('baseDeDados.xlsx')
ws = wb['DADOS']

gestor = []
dados = [('MARCELA ARAUJO',"","","","",""),('#', 'CLIENTE', 'CPF', 'TELEFONE', 'STATUS', 'VENCIMENTO')]
cont = 1

#sequencia gestor
for row in ws.values:
    if row[2] == 2:
        if str(row[9]).strip() not in gestor:
            gestor.append(str(row[9]).strip())

fileName = 'MARCELO MORAES BLM.pdf'

for row in ws.values:
    if row[2] == 2 and str(row[10]).strip() != 'PAGO' and str(row[10]).strip() != 'A VENCER':
        if str(row[9]).strip() == 'MARCELO MORAES BLM':
            dados.append((cont, row[5], row[3], row[6], row[10], "{:%d/%m/%Y}".format(row[12])))
            cont+=1

pdf = SimpleDocTemplate(fileName, pagesize=A4)
table = Table(dados)

#Fonte e cores
style = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.cadetblue),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,0), 'LEFT'),
    ('SPAN', (0,0), (2,0)),
    ('ALIGN', (0,1), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,-1), 'Courier-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 10),
    ('FONTSIZE', (0,1), (-1,-1), 8),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),

])
table.setStyle(style)

rowNumb = len(dados)

#Cores das linhas alternadas
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.bisque
    else:
        bc = colors.beige
    ts = TableStyle([('BACKGROUND', (0,i), (-1,i), bc)])
    table.setStyle(ts)

#Linhas
ts = TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.gray),
    ('LINEABOVE', (0,0), (-1,-1), 1, colors.gray)
])
table.setStyle(ts)


elems = []
elems.append(table)

pdf.build(elems)