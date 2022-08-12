# Importando as bibliotecas
# import posiciona
from Classe_BC import *
from Classe_DB import *

# =======================================================================================================================
# objetos
back = Back()
data = BlackDB()
# =======================================================================================================================
# Criação e Modificações da Janela
janela = Tk()
janela.geometry('960x540')
janela.title('Black MEGB')
janela.iconbitmap('Fotos/black megb.ico')
# janela.resizable(False, False)
# =======================================================================================================================
# Comando para copiar as coordenadas que sai no terminal
'''
janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))'''
# =======================================================================================================================
# Cores
dark_gray = '#242323'
blue = '#004AAD'
black = '#191919'
white = '#ffffff'
gray = '#323232'
red = '#F01F15'
ligth_red = '#ED3F3F'
ligth_gray = '#A6A6A6'
# =======================================================================================================================
# Frames
frame_entrada = Frame(janela)
frame_login = Frame(janela)
frame_cadastro = Frame(janela)
frame_principal = Frame(janela)
frame_mario = Frame(janela)
frame_sonic = Frame(janela)
frame_mk = Frame(janela)
frame_donkeykong = Frame(janela)
frame_bomberman = Frame(janela)
frame_biblioteca = Frame(janela)
frame_perfil = Frame(janela)
# =======================================================================================================================
# Fotos
img_entrada = PhotoImage(file='Fotos/Tela_entrada.png')
img_login = PhotoImage(file='Fotos/tela_login.png')
img_cadastro = PhotoImage(file='Fotos/Tela_cadastro.png')
img_principal = PhotoImage(file='Fotos/Tela_principal.png')
img_jogar = PhotoImage(file='Fotos/tela_jogar.png')
img_mario = PhotoImage(file='Fotos/tela_mario.png')
img_sonic = PhotoImage(file='Fotos/tela sonic.png')
img_mk = PhotoImage(file='Fotos/tela_mk.png')
img_donkeykong = PhotoImage(file='Fotos/tela kong.png')
img_bomberman = PhotoImage(file='Fotos/bomberman.png')
img_bt_mario = PhotoImage(file='Fotos/ver mario.png')
img_bt_jogo = PhotoImage(file='Fotos/ver jogo.png')
img_menu_bt = PhotoImage(file='Fotos/menu_bt.png')
img_bt_biblioteca = PhotoImage(file='Fotos/bt_biblioteca.png')
img_biblioteca = PhotoImage(file='Fotos/Tela_biblioteca.png')
img_perfil = PhotoImage(file='Fotos/tela_perfil.png')
img_bt_perfil = PhotoImage(file='Fotos/perfil.png')
img_supermario = PhotoImage(file='Fotos/super-mario.png')
img_sonic_ico = PhotoImage(file='Fotos/sonic_icone.png')
img_donkey_ico = PhotoImage(file='Fotos/donkey.png')
img_mk3 = PhotoImage(file='Fotos/mk3.png')
img_sbomber = PhotoImage(file='Fotos/sbomberman.png')
img_bt_jogar = PhotoImage(file='Fotos/bt_jogar.PNG')
img_bt_remover = PhotoImage(file='Fotos/bt_desistalar.PNG')
img_fav_on = PhotoImage(file='Fotos/estrela_comcor.png')
img_fav_off = PhotoImage(file='Fotos/estrela_semcor.png')
# =======================================================================================================================
# Frames principais
frame_entrada.pack()
frame_login.pack()
# =======================================================================================================================
# Primeiro Frame (Logo)
lb_entrada = Label(frame_entrada, image=img_entrada, border=0)
lb_entrada.pack()
# =======================================================================================================================
# Segundo Frame (Login)
lb_login = Label(frame_login, image=img_login, border=0)
lb_login.pack()
# entrys
en_email = Entry(frame_login, font='palatino 15 bold', bd=0, bg=dark_gray, fg=white)
en_senha = Entry(frame_login, font='palatino 15 bold', bd=0, bg=dark_gray, fg=white)
# Buttons
bt_entrar = Button(frame_login, text='Entrar', font='palatino 20 bold', bg=blue, bd=0, fg=white, activebackground=blue,
                   activeforeground=white, command=lambda: [back.logar(en_email, La_N_exibicao, La_Nome, La_email,
                                                                       en_senha, frame_principal, frame_login)])

bt_cadas = Button(frame_login, text='Cadastrar', font='Cardo 12 underline', bg=dark_gray, fg=blue,
                  activebackground=dark_gray, activeforeground=blue, bd=0,
                  command=lambda: [frame_cadastro.pack(), frame_login.forget()])
# places
en_email.place(width=396, height=28, x=281, y=194)
en_senha.place(width=401, height=34, x=279, y=304)
bt_entrar.place(width=404, height=50, x=279, y=427)
bt_cadas.place(width=71, height=20, x=424, y=365)
# =======================================================================================================================
# Terceiro Frame (Cadastro)
lb_cadastro = Label(frame_cadastro, image=img_cadastro, border=0)
lb_cadastro.pack()
# entrys
en_nome = Entry(frame_cadastro, font='palatino 15 bold', bd=0, bg=gray, fg=white)
en_sobrenome = Entry(frame_cadastro, font='palatino 15 bold', bd=0, bg=gray, fg=white)
en_exebicao = Entry(frame_cadastro, font='palatino 15 bold', bd=0, bg=gray, fg=white)
en_email_cadas = Entry(frame_cadastro, font='palatino 15 bold', bd=0, bg=gray, fg=white)
en_senha_cadas = Entry(frame_cadastro, font='palatino 15 bold', bd=0, bg=gray, fg=white)
# Buttons
bt_cadastrar = Button(frame_cadastro, text='Cadastrar', font='Cardo 13 bold', bd=0, bg=black, fg=white,
                      activebackground=black, activeforeground=white,
                      command=lambda: [back.cadas_user(en_nome, en_sobrenome, en_exebicao, en_email_cadas,
                                                       en_senha_cadas, frame_cadastro, frame_login)])
bt_conta = Button(frame_cadastro, text='Já tenho uma conta', font='cardo 10 underline', bg=dark_gray, fg=blue, bd=0,
                  activebackground=dark_gray, activeforeground=blue,
                  command=lambda: [frame_login.pack(), frame_cadastro.forget(), en_nome.delete(0, 'end'),
                                   en_sobrenome.delete(0, 'end'), en_exebicao.delete(0, 'end'),
                                   en_email_cadas.delete(0, 'end'), en_senha_cadas.delete(0, 'end')])
# places
en_nome.place(width=165, height=41, x=269, y=123)
en_sobrenome.place(width=163, height=39, x=451, y=124)
en_exebicao.place(width=344, height=42, x=270, y=207)
en_email_cadas.place(width=344, height=42, x=270, y=283)
en_senha_cadas.place(width=346, height=45, x=269, y=359)
bt_cadastrar.place(width=216, height=42, x=331, y=437)
bt_conta.place(width=218, height=19, x=330, y=483)
# =======================================================================================================================
# Quarto Frame (Principal)
lb_principal = Label(frame_principal, image=img_principal, bd=0)
lb_principal.pack()
# Buttons
bt_mario = Button(frame_principal, image=img_bt_mario, bd=0, bg=red, activebackground=red,
                  command=lambda: [frame_principal.forget(), frame_mario.pack()])
bt_mario.place(x=275, y=296)
bt_sonic = Button(frame_principal, image=img_bt_jogo, bd=0, bg=dark_gray, activebackground=dark_gray,
                  command=lambda: [frame_principal.forget(), frame_sonic.pack()])
bt_sonic.place(x=241, y=504)
bt_donk = Button(frame_principal, image=img_bt_jogo, bd=0, bg=dark_gray, activebackground=dark_gray,
                 command=lambda: [frame_principal.forget(), frame_donkeykong.pack()])
bt_donk.place(x=409, y=504)
bt_mk = Button(frame_principal, image=img_bt_jogo, bd=0, bg=dark_gray, activebackground=dark_gray,
               command=lambda: [frame_principal.forget(), frame_mk.pack()])
bt_mk.place(x=564, y=504)
bt_bm = Button(frame_principal, image=img_bt_jogo, bd=0, bg=dark_gray, activebackground=dark_gray,
               command=lambda: [frame_principal.forget(), frame_bomberman.pack()])
bt_bm.place(x=736, y=504)
bt_biblioteca = Button(frame_principal, image=img_bt_biblioteca, bd=0, bg=dark_gray, activebackground=dark_gray,
                       command=lambda: [frame_biblioteca.pack(), frame_principal.forget()])
bt_biblioteca.place(x=4, y=117)
bt_perfil = Button(frame_principal, image=img_bt_perfil, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_perfil.pack(), frame_principal.forget()])
bt_perfil.place(x=5, y=472)
# =======================================================================================================================
# Temporizador na tela (logo)
janela.after(1000, frame_entrada.forget)
# =======================================================================================================================
# FRAME MARIO LOJA
lb_mario = Label(frame_mario, image=img_mario)
lb_mario.pack()

chvalue = BooleanVar()
check_fav_mario = Checkbutton(frame_mario, image=img_fav_off, selectimage=img_fav_on, activebackground=dark_gray,
                              selectcolor=dark_gray, indicatoron=False, bd=0, onvalue=True, offvalue=False,
                              bg=dark_gray, variable=chvalue, command=lambda: back.mudar(chvalue, fav_mario,
                                                                                         x=1, y=311))
check_fav_mario.place(x=735, y=474)

menu_mario = Button(frame_mario, image=img_menu_bt, bd=0, bg=dark_gray, activebackground=dark_gray,
                    command=lambda: [frame_mario.forget(), frame_principal.pack()])
menu_mario.place(x=12, y=76)
bt_biblioteca = Button(frame_mario, image=img_bt_biblioteca, bd=0, bg=dark_gray, activebackground=dark_gray,
                       command=lambda: [frame_biblioteca.pack(), frame_mario.forget()])
bt_biblioteca.place(x=4, y=117)
bt_perfil = Button(frame_mario, image=img_bt_perfil, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_perfil.pack(), frame_mario.forget()])
bt_perfil.place(x=5, y=472)
bt_add_bibli_mario = Button(frame_mario, text='Adicionar a Biblioteca', font='palatino 15 bold', bd=0, bg='#737373',
                            fg=black, activebackground='#737373', activeforeground=black,
                            command=lambda: back.add_biblioteca(bt_add_bibli_mario, bt_mario_bibli, x=5, y=164))
bt_add_bibli_mario.place(width=200, height=39, x=240, y=477)
# =======================================================================================================================
# FRAME SONIC LOJA
lb_sonic = Label(frame_sonic, image=img_sonic)
lb_sonic.pack()
menu_sonic = Button(frame_sonic, image=img_menu_bt, bd=0, bg=dark_gray, activebackground=dark_gray,
                    command=lambda: [frame_sonic.forget(), frame_principal.pack()])
menu_sonic.place(x=12, y=76)

ch_sonic_value = BooleanVar()

check_fav_soni = Checkbutton(frame_sonic, image=img_fav_off, selectimage=img_fav_on, activebackground=dark_gray,
                             selectcolor=dark_gray, indicatoron=False, bd=0, onvalue=True, offvalue=False,
                             bg=dark_gray, variable=ch_sonic_value, command=lambda: back.mudar(ch_sonic_value,
                                                                                               fav_sonic, x=1, y=336))
check_fav_soni.place(x=735, y=474)

bt_biblioteca = Button(frame_sonic, image=img_bt_biblioteca, bd=0, bg=dark_gray, activebackground=dark_gray,
                       command=lambda: [frame_biblioteca.pack(), frame_sonic.forget()])
bt_biblioteca.place(x=4, y=117)
bt_perfil = Button(frame_sonic, image=img_bt_perfil, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_perfil.pack(), frame_sonic.forget()])
bt_perfil.place(x=5, y=472)
bt_add_bibli_sonic = Button(frame_sonic, text='Adicionar a Biblioteca', font='palatino 15 bold', bd=0, bg='#737373',
                            fg=black, activebackground='#737373', activeforeground=black,
                            command=lambda: back.add_biblioteca(bt_add_bibli_sonic, bt_sonic_bibli, x=5, y=192))
bt_add_bibli_sonic.place(width=200, height=39, x=240, y=477)
# =======================================================================================================================
# FRAME DONK
lb_kong = Label(frame_donkeykong, image=img_donkeykong)
lb_kong.pack()
menu_kong = Button(frame_donkeykong, image=img_menu_bt, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_donkeykong.forget(), frame_principal.pack()])
menu_kong.place(x=12, y=76)
bt_biblioteca = Button(frame_donkeykong, image=img_bt_biblioteca, bd=0, bg=dark_gray, activebackground=dark_gray,
                       command=lambda: [frame_biblioteca.pack(), frame_donkeykong.forget()])
bt_biblioteca.place(x=4, y=117)

ch_donkey = BooleanVar()

check_fav_donkey = Checkbutton(frame_donkeykong, image=img_fav_off, selectimage=img_fav_on, activebackground=dark_gray,
                               selectcolor=dark_gray, indicatoron=False, bd=0, onvalue=True, offvalue=False,
                               bg=dark_gray, variable=ch_donkey, command=lambda: back.mudar(ch_donkey, fav_donkey, x=1,
                                                                                            y=362))
check_fav_donkey.place(x=735, y=474)

bt_perfil = Button(frame_donkeykong, image=img_bt_perfil, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_perfil.pack(), frame_donkeykong.forget()])
bt_perfil.place(x=5, y=472)
bt_add_bibli_dk = Button(frame_donkeykong, text='Adicionar a Biblioteca', font='palatino 15 bold', bd=0, bg='#737373',
                         fg=black, activebackground='#737373', activeforeground=black,
                         command=lambda: back.add_biblioteca(bt_add_bibli_dk, bt_donkey_bibli, x=10, y=219))
bt_add_bibli_dk.place(width=200, height=39, x=240, y=477)
# =======================================================================================================================
# frame mk
lb_mk = Label(frame_mk, image=img_mk)
lb_mk.pack()
menu_mk = Button(frame_mk, image=img_menu_bt, bd=0, bg=dark_gray, activebackground=dark_gray,
                 command=lambda: [frame_mk.forget(), frame_principal.pack()])
menu_mk.place(x=12, y=76)
bt_biblioteca = Button(frame_mk, image=img_bt_biblioteca, bd=0, bg=dark_gray, activebackground=dark_gray,
                       command=lambda: [frame_biblioteca.pack(), frame_mk.forget()])
bt_biblioteca.place(x=4, y=117)

ch_mk = BooleanVar()


check_fav_mk = Checkbutton(frame_mk, image=img_fav_off, selectimage=img_fav_on, activebackground=dark_gray,
                           selectcolor=dark_gray, indicatoron=False, bd=0, onvalue=True, offvalue=False,
                           bg=dark_gray, variable=ch_mk, command=lambda: back.mudar(ch_mk, fav_mk, x=1, y=385))
check_fav_mk.place(x=735, y=474)

bt_perfil = Button(frame_mk, image=img_bt_perfil, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_perfil.pack(), frame_mk.forget()])
bt_perfil.place(x=5, y=472)
bt_add_bibli_mk = Button(frame_mk, text='Adicionar a Biblioteca', font='palatino 15 bold', bd=0, bg='#737373', fg=black,
                         activebackground='#737373', activeforeground=black,
                         command=lambda: back.add_biblioteca(bt_add_bibli_mk, bt_mk3_bibli, x=0, y=244))
bt_add_bibli_mk.place(width=200, height=39, x=240, y=477)
# =======================================================================================================================
# frame bomber
lb_bomber = Label(frame_bomberman, image=img_bomberman)
lb_bomber.pack()
menu_bomberman = Button(frame_bomberman, image=img_menu_bt, bd=0, bg=dark_gray, activebackground=dark_gray,
                        command=lambda: [frame_bomberman.forget(), frame_principal.pack()])
menu_bomberman.place(x=12, y=76)
bt_biblioteca = Button(frame_bomberman, image=img_bt_biblioteca, bd=0, bg=dark_gray, activebackground=dark_gray,
                       command=lambda: [frame_biblioteca.pack(), frame_bomberman.forget()])
bt_biblioteca.place(x=4, y=117)

ch_bomber = BooleanVar()

check_fav_bomber = Checkbutton(frame_bomberman, image=img_fav_off, selectimage=img_fav_on, activebackground=dark_gray,
                               selectcolor=dark_gray, indicatoron=False, bd=0, bg=dark_gray, variable=ch_bomber,
                               onvalue=True, offvalue=False, command=lambda: back.mudar(ch_bomber, fav_bomber, x=1,
                                                                                        y=407))
check_fav_bomber.place(x=735, y=474)

bt_perfil = Button(frame_bomberman, image=img_bt_perfil, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_perfil.pack(), frame_bomberman.forget()])
bt_perfil.place(x=5, y=472)
bt_add_bibli_bomber = Button(frame_bomberman, text='Adicionar a Biblioteca', font='palatino 15 bold', bd=0,
                             bg='#737373', fg=black, activebackground='#737373', activeforeground=black,
                             command=lambda: back.add_biblioteca(bt_add_bibli_bomber, bt_bomber, x=0, y=269))
bt_add_bibli_bomber.place(width=200, height=39, x=240, y=477)
# =======================================================================================================================
# Frame Biblioteca
lb_biblioteca = Label(frame_biblioteca, image=img_biblioteca, bd=0)
lb_biblioteca.pack()
lb_jogar = Label(frame_biblioteca, image=img_jogar, bd=0)
# Buttons
bt_jogar = Button(frame_biblioteca, image=img_bt_jogar, bd=0, bg=dark_gray, activebackground=dark_gray,
                  command=lambda: back.download())
bt_remover = Button(frame_biblioteca, image=img_bt_remover, bd=0, bg=dark_gray, activebackground=dark_gray)

bt_menu = Button(frame_biblioteca, image=img_menu_bt, bd=0, bg=dark_gray, activebackground=dark_gray,
                 command=lambda: [frame_principal.pack(), frame_biblioteca.forget()])
bt_perfil = Button(frame_biblioteca, image=img_bt_perfil, bd=0, bg=dark_gray, activebackground=dark_gray,
                   command=lambda: [frame_perfil.pack(), frame_biblioteca.forget()])
bt_perfil.place(x=5, y=472)
bt_mario_bibli = Button(frame_biblioteca, image=img_supermario, text='SUPER MARIO WORLD', font='palatino 10 bold',
                        bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                        command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                         bt_jogar.place(width=166, height=78, x=253, y=247),
                                         bt_remover.place(width=166, height=78, x=433, y=247)])
bt_sonic_bibli = Button(frame_biblioteca, image=img_sonic_ico, text='SONIC THE HEDGEHOG', font='palatino 10 bold',
                        bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                        command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                         bt_jogar.place(width=166, height=78, x=253, y=247),
                                         bt_remover.place(width=166, height=78, x=433, y=247)])
bt_donkey_bibli = Button(frame_biblioteca, image=img_donkey_ico, text='DONKEY KONG TRILOGY', font='palatino 10 bold',
                         bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white,
                         compound=LEFT,
                         command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                          bt_jogar.place(width=166, height=78, x=253, y=247),
                                          bt_remover.place(width=166, height=78, x=433, y=247)])
bt_mk3_bibli = Button(frame_biblioteca, image=img_mk3, text='MORTAL KOMBAT 3', font='palatino 10 bold',
                      bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                      command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                       bt_jogar.place(width=166, height=78, x=253, y=247),
                                       bt_remover.place(width=166, height=78, x=433, y=247)])

bt_bomber = Button(frame_biblioteca, image=img_sbomber, text='SUPER BOMBER MAN', font='palatino 10 bold',
                   bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                   command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                    bt_jogar.place(width=166, height=78, x=253, y=247),
                                    bt_remover.place(width=166, height=78, x=433, y=247)])
# Fav
fav_mario = Button(frame_biblioteca, image=img_supermario, text='SUPER MARIO WORLD', font='palatino 10 bold',
                   bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                   command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                    bt_jogar.place(width=166, height=78, x=253, y=247),
                                    bt_remover.place(width=166, height=78, x=433, y=247)])

fav_sonic = Button(frame_biblioteca, image=img_sonic_ico, text='SONIC THE HEDGEHOG', font='palatino 10 bold',
                   bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                   command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                    bt_jogar.place(width=166, height=78, x=253, y=247),
                                    bt_remover.place(width=166, height=78, x=433, y=247)])


fav_donkey = Button(frame_biblioteca, image=img_donkey_ico, text='DONKEY KONG TRILOGY', font='palatino 10 bold',
                    bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                    command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                     bt_jogar.place(width=166, height=78, x=253, y=247),
                                     bt_remover.place(width=166, height=78, x=433, y=247)])

fav_mk = Button(frame_biblioteca, image=img_mk3, text='MORTAL KOMBAT 3', font='palatino 10 bold',
                bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                 bt_jogar.place(width=166, height=78, x=253, y=247),
                                 bt_remover.place(width=166, height=78, x=433, y=247)])
fav_bomber = Button(frame_biblioteca, image=img_sbomber, text='SUPER BOMBER MAN', font='palatino 10 bold',
                    bd=0, fg=white, bg=dark_gray, activebackground=dark_gray, activeforeground=white, compound=LEFT,
                    command=lambda: [lb_jogar.place(width=682, height=316, x=238, y=21),
                                     bt_jogar.place(width=166, height=78, x=253, y=247),
                                     bt_remover.place(width=166, height=78, x=433, y=247)])

# Entrys
en_pesquisa = Entry(frame_biblioteca, font='palatino 12 ', bd=0, bg=ligth_gray, fg=black)
# Places
bt_menu.place(width=89, height=31, x=12, y=56)
en_pesquisa.place(width=113, height=21, x=39, y=100)
# =======================================================================================================================
# Tela Perfil
lb_perfil = Label(frame_perfil, image=img_perfil, bd=0)
lb_perfil.pack()
# Label
La_N_exibicao = Label(frame_perfil, text='', font='palatino 15 bold', bd=0, bg=dark_gray, fg=white)
La_Nome = Label(frame_perfil, text='', font='palatino 15 bold', bd=0, bg=dark_gray, fg=white)
La_email = Label(frame_perfil, text='', font='palatino 15 bold', bd=0, bg=dark_gray, fg=white)
La_jogos = Label(frame_perfil, text='0', font='palatino 15 bold', bd=0, bg=dark_gray, fg=white)
# Buttons
bt_biblioteca = Button(frame_perfil, image=img_bt_biblioteca, bd=0, bg=dark_gray, activebackground=dark_gray,
                       command=lambda: [frame_biblioteca.pack(), frame_perfil.forget()])
bt_biblioteca.place(x=4, y=117)
bt_menu = Button(frame_perfil, image=img_menu_bt, bd=0, bg=dark_gray, activebackground=dark_gray,
                 command=lambda: [frame_perfil.forget(), frame_principal.pack()])
bt_menu.place(x=12, y=76)
bt_sair = Button(frame_perfil, text='Sair', font='palatino 15 bold', bd=0, bg=blue, fg=white, activebackground=blue,
                 activeforeground=white, command=lambda: [frame_login.pack(), frame_perfil.forget()])
bt_sair.place(width=109, height=39, x=338, y=472)
bt_excluir = Button(frame_perfil, text='Excluir Conta', font='palatino 15 bold', bd=0, fg=black, bg=ligth_red,
                    activebackground=ligth_red, activeforeground=black,
                    command=lambda: [back.Deletar(en_email, en_senha, frame_login, frame_perfil)])
bt_excluir.place(width=113, height=40, x=553, y=472)
# place
La_N_exibicao.place(width=381, height=22, x=321, y=99)
La_Nome.place(width=384, height=27, x=331, y=303)
La_email.place(width=384, height=25, x=330, y=394)
La_jogos.place(width=25, height=18, x=537, y=170)
# =======================================================================================================================
# Execução da Janela
janela.mainloop()