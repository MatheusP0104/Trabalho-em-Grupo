#Importando as bibliotecas
from tkinter import *
import posiciona

#Criação e Modificações da Janela
janela = Tk()
janela.geometry('1920x1080')
janela.title('Black MEGB')
janela.iconbitmap('Fotos/black megb.ico')

#Comando para copiar as coordenadas que sai no terminal
janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))
#Cores
dark_gray = '#242323'
blue = '#004AAD'
black = '#191919'
white = '#ffffff'
gray = '#323232'


#Frames
frame_entrada = Frame(janela)
frame_login = Frame(janela)
frame_cadastro = Frame(janela)
frame_principal = Frame(janela)
frame_mario = Frame(janela)
frame_sonic = Frame(janela)
frame_mk = Frame(janela)
frame_donkeykong = Frame(janela)
frame_bomberman = Frame(janela)

#Fotos
img_entrada = PhotoImage(file='Fotos/Tela_entrada.png')
img_login = PhotoImage(file='Fotos/tela_login.png')
img_cadastro = PhotoImage(file='Fotos/Tela_cadastro.png')
img_principal = PhotoImage(file='Fotos/Tela_principal.png')
img_mario = PhotoImage(file='Fotos/tela_mario.png')
img_sonic = PhotoImage(file='Fotos/tela sonic.png')
img_mk = PhotoImage(file='Fotos/tela_mk.png')
img_donkeykong = PhotoImage(file='Fotos/tela kong.png')
img_bomberman = PhotoImage(file='Fotos/bomberman.png')

#Frames principais
frame_entrada.pack()
frame_login.pack()

#Primeiro Frame (Logo)
lb_entrada = Label(frame_entrada, image=img_entrada, border=0)
lb_entrada.pack()

#Segundo Frame (Login)
lb_login = Label(frame_login, image=img_login,border=0)
lb_login.pack()
#entrys
en_email = Entry(frame_login, font='palatino 30 bold', bd=0, bg=dark_gray, fg=white)
en_senha = Entry(frame_login, font='palatino 30 bold', bd=0, bg=dark_gray, fg=white)

#Buttons
bt_entrar = Button(frame_login, text='Entrar', font='palatino 30 bold', bg=blue, bd=0, fg=white, activebackground=blue, activeforeground=white)
bt_cadas = Button(frame_login, text='Cadastrar', font='Cardo 20 underline', bg=dark_gray, fg=blue, activebackground=dark_gray, activeforeground=blue, bd=0,
                  command=lambda:[frame_cadastro.pack(),frame_login.forget()])

#places
en_email.place(width=801, height=52, x=559, y=387)
en_senha.place(width=805, height=48, x=560, y=619)
bt_entrar.place(width=812, height=101, x=553, y=844)
bt_cadas.place(width=139, height=43, x=840, y=718)
#Terceiro Frame (Cadastro)
lb_cadastro = Label(frame_cadastro, image=img_cadastro, border=0)
lb_cadastro.pack()
#entrys
en_nome = Entry(frame_cadastro, font='palatino 30 bold', bd=0, bg=gray, fg=white)
en_sobrenome = Entry(frame_cadastro, font='palatino 30 bold', bd=0, bg=gray, fg=white)
en_exebicao = Entry(frame_cadastro, font='palatino 30 bold', bd=0, bg=gray, fg=white)
en_email_cadas = Entry(frame_cadastro, font='palatino 30 bold', bd=0, bg=gray, fg=white)
en_senha_cadas = Entry(frame_cadastro, font='palatino 30 bold', bd=0, bg=gray, fg=white)
#Buttons
bt_cadastrar = Button(frame_cadastro, text='Cadastrar', font='Cardo 24 bold', bd=0, bg=black,fg=white,activebackground=black,activeforeground=white)
bt_conta = Button(frame_cadastro,text='Já tenho uma conta',font='cardo 20 underline',bg=dark_gray,fg=blue,bd=0,activebackground=dark_gray,activeforeground=blue,
                  command=lambda:[frame_login.pack(),frame_cadastro.forget()])
#places
en_nome.place(width=329, height=78, x=538, y=238)
en_sobrenome.place(width=331, height=80, x=901, y=239)
en_exebicao.place(width=693, height=88, x=537, y=401)
en_email_cadas.place(width=687, height=81, x=542, y=562)
en_senha_cadas.place(width=689, height=85, x=539, y=711)
bt_cadastrar.place(width=433, height=80, x=662, y=868)
bt_conta.place(width=440, height=30, x=660, y=960)
#Temporizador na tela (logo)
janela.after(1000,frame_entrada.forget)
#Execução da Janela
janela.mainloop()