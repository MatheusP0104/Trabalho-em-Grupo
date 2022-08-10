from tkinter import *
from Classe_DB import *
from tkinter import Button, Label, messagebox, ttk
from urllib.request import urlretrieve
import time


class Back:
    def __init__(self):
        self.db = BlackDB()

    def cadas_user(self, nome, sobrenome, nome_exibicao, email, senha, frame1, frame2):
        if messagebox.askyesno('confirmar', 'salvar dados?'):
            self.db.cadas_user(nome=nome.get(), sobrenome=sobrenome.get(), nome_exibicao=nome_exibicao.get(),
                               email=email.get(), senha=senha.get())
            frame1.forget()
            frame2.pack()
            nome.delete(0, 'end')
            sobrenome.delete(0, 'end')
            nome_exibicao.delete(0, 'end')
            email.delete(0, 'end')
            senha.delete(0, 'end')
        else:
            pass

    def logar(self, entry_email, entry_senha, frame1, frame2):
        if self.db.check_user(entry_email.get(), entry_senha.get()):
            frame1.pack()
            frame2.forget()
        else:
            messagebox.showerror('Acesso Negado', 'conta desconhecida, tente novamente')

    def Deletar(self, entry_email,entry_senha, frame1, frame2):
        self.db.delete_accont(email=entry_email.get())
        frame1.pack()
        frame2.forget()
        entry_email.delete(0, 'end')
        entry_senha.delete(0, 'end')

    def mudar(self, vari, bt, x, y):
        if vari.get():
            bt.place(width=206, height=15, x=x, y=y)
        else:
            bt.place_forget()

    def Lista(self, entry_email, lb_exi, lb_nome, lb_email):
        lista = self.db.info_user(entry_email.get())
        lb_exi['text'] = f'{lista[0]}'
        lb_nome['text'] = f'{lista[1]} {lista[2]}'
        lb_email['text'] = f'{lista[3]}'

    def add_biblioteca(self, bt, jogo, x, y):
        if bt['fg'] == '#191919':
            jogo.place(width=195, height=21, x=x, y=y)
            bt['text'] = 'Remover da Biblioteca'
            bt['fg'] = '#F01F15'
        elif bt['fg'] == '#F01F15':
            jogo.place_forget()
            bt['fg'] = '#191919'
            bt['text'] = 'Adicionar a Biblioteca'

    def download(self):
        janela2 = Toplevel()
        janela2.geometry('350x200')
        janela2.resizable(False,False)
        janela2.iconbitmap('Fotos/black megb.ico')
        janela2.title('Download')

        def instalar():
            urlretrieve("https://docs.google.com/uc?export=download&id=1EjKmIidcQNEgpX4lVJniWJYhtdyAYHSC",
                        "JogoMario.rar")
            for i in range(5):
                if progress1['value'] < 100:
                    janela2.update_idletasks()
                    progress1['value'] += 20
                    value_label['text'] = progress1['value'], '%'
                    time.sleep(0.1)
                else:
                    messagebox.showinfo(message='Algo deu errado!, Tente novamente')

            messagebox.showinfo(message='Download terminado com sucesso!')

        def parar():
            progress1.stop()
            value_label['text'] = progress1['value'], '%'

        progress1 = ttk.Progressbar(janela2, orient='horizontal', mode='determinate', length=200)
        progress1.pack(pady=20)

        value_label = Label(janela2, text='0%')
        value_label.pack(pady=20)

        bt_instalar = Button(janela2, text='Instalar', command=instalar)
        bt_instalar.pack(pady=20)

        bt_parar = Button(janela2, text='Cancelar', command=parar)
        bt_parar.pack(pady=20)