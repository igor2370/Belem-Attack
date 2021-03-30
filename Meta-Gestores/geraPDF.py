from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from datetime import datetime
from os import mkdir


def gerarPDF(nome, dados):
    arquivo =  mkdir('file/gestores '+str(datetime.now()))
    fileName = str(arquivo)+'/'+str(nome)+'.pdf'

    pdf = SimpleDocTemplate(fileName, pagesize=A4)

    table = Table(dados)

    '''
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
'''
if __name__=='__main__':
    gerarPDF('teste', [(0,0,0,0,0,0,0), (0,0,0,0,0,0,0), (1,1,1,1,1,1,1), (2,2,2,2,2,2,2), (2,2,2,2,2,2,2), (2,2,2,2,2,2,2)])