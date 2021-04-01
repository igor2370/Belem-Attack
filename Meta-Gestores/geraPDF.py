from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from datetime import datetime
from os import mkdir, path

def filePDF():
    #cria diretório
    data = datetime.now().strftime("%d%m%Y-%H%M%S")
    arquivo ='Gestores'+data
    mkdir('file/'+arquivo)
    return str('file/Gestores'+data+'/')



def gerarPDF(nome, dados, fileName):

    #Config pdf
    pdf = SimpleDocTemplate(fileName + nome+'.pdf', pagesize=A4)

    #cria tabela
    table = Table(dados)
    

    #Config Tabela
    #========================================================
    #Fonte e cores
    style = TableStyle([
        ('SPAN', (0,0), (2,0)),
        ('SPAN', (0,1), (2,1)),
        ('BACKGROUND', (0,2), (-1,2), colors.cadetblue),
        ('TEXTCOLOR', (0,2), (-1,2), colors.white),
        ('ALIGN', (0,0), (-1,1), 'LEFT'),
        ('ALIGN', (0,2), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,-1), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,2), 10),
        ('FONTSIZE', (0,3), (-1,-1), 8),
        ('BACKGROUND', (0,3), (-1,-1), colors.beige),

    ])

    table.setStyle(style)

    rowNumb = len(dados)

    #Cores das linhas alternadas
    for i in range(3, rowNumb):
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
    #========================================================
    
    #Grava pdf
    pdf.build([table])

  
 #Teste do módulo 
if __name__=='__main__':
    nomeArquivo = filePDF()
    gerarPDF('teste', [("Gestor","","","","","",""), ("data","","","","","",""), (1,1,1,1,1,1,1), (2,2,2,2,2,2,2), (2,2,2,2,2,2,2), (2,2,2,2,2,2,2)],nomeArquivo)

'''

'''