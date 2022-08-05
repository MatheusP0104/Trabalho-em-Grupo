import mysql.connector


class BlackDB:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='blackmegb')
        self.mycursor = self.conexao.cursor()
        self.user = ''

    def cadas_user(self,nome, sobrenome, nome_exibicao, email, senha):
        comando_sql = f'insert into Usuarios (nome, sobrenome, nome_exibicao, email, senha) values ("{nome}",' \
                       f'"{sobrenome}","{nome_exibicao}", "{email}", "{senha}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()


    def check_user(self, entry_email, entry_senha):
        self.mycursor.execute('select email,senha from Usuarios')
        self.user = self.mycursor.fetchall()
        verifica = False
        for usuarios in self.user:
            if entry_email == usuarios[0] and entry_senha == usuarios[1]:
                verifica = True
            else:
                pass
        if verifica:
            return True
        else:
            return False

    def delete_accont(self, email):
        self.mycursor.execute(f'select id from Usuarios where email = "{email}"')
        codigo = self.mycursor.fetchall()
        self.mycursor.execute(f'delete from Usuarios where id = "{codigo[0][0]}" ')
        self.conexao.commit()
