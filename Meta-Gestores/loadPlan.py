from openpyxl import load_workbook
from tkinter import messagebox
from datetime import date
from geraPDF import gerarPDF, filePDF

def loadWB():
    try:

        criaPasta = filePDF()
        
        gestor = []

        mes = [
            'JANEIRO','FEVEREIRO','MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
            'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'
        ]
        atual = f'REFERÊNCIA: {mes[date.today().month-1]} {date.today().year}'

        #Carrega planilha
        wb = load_workbook('file/baseDeDados.xlsx')
        ws = wb['DADOS']
        
        #sequencia gestor
        for row in ws.values:
            if str(row[2]) == '2':
                if str(row[9]).strip() not in gestor:
                    gestor.append(str(row[9]).strip())

        #carrega dados
        for element in gestor:
            
             #numerador de páginas
            cont = 1

            #cabeçalho tabela
            dados = [
                (f'GESTOR: {element}',"","","","","",""),
                (atual,"","","","","",""),
                ('#', 'CLIENTE', 'CPF', 'TELEFONE', 'STATUS', 'VENDEDOR', 'VENCIMENTO')]

            #cria a lista de dados
            for row in ws.values:
                if str(row[2]) == '2' and  str(row[9]).strip() == element and  str(row[10]).strip()!='PAGO' and str(row[10]).strip()!='CANCELADO':
                    dados.append((cont, row[5], row[3], row[6], row[10], row[8], "{:%d/%m/%Y}".format(row[12])))
                    cont+=1
            gerarPDF(element.replace('/','-'),dados,criaPasta)
                
    #tratamento de erros
    except FileNotFoundError:
        erro = 'Coloque o arquivo "baseDeDados" dentro da pasta "file"!'
        messagebox.showerror('ERRO!', erro)
    except KeyError:
        erro = 'Não existe a planilha "DADOS" dentro do arquivo "baseDeDados"'
        messagebox.showerror('ERRO!', erro)
    except ValueError:
        erro = 'Verifique se as datas da coluna "M" da planilha "DADOS" estão em formto de data'
        messagebox.showerror('ERRO!', erro)

if __name__ == '__main__':
    loadWB()