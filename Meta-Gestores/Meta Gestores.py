from tkinter import *
from loadPlan import loadWB

janela = Tk()
janela.title('Meta Gestores')

janela.geometry('480x200+300+100')
janela.resizable(False, False)
janela['bg'] = 'linen'

lb1 = Label(janela, text='Meta dos Gestores', font=('Arial 30 bold'), bg='linen', pady=1, fg='VioletRed1')
lb2 = Label(janela, text='Kamyla Albuquerque', font=('Arial 14 italic'), bg='linen', pady=20, fg='VioletRed1')

lb1.pack()
lb2.pack()

btn = Button(janela, text = 'Gerar PDF', command=lambda: loadWB(), bg='maroon4', fg='white', font=('Arial 14'), width=20)
btn.pack()


janela.mainloop()