from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk
from tkinter import messagebox
import cadastro
import time
from threading import Thread


con = sqlite3.connect('banco_de_dados.db')
cursor = con.cursor()


class App:
    def __init__(self):
        prin = Thread(target=self.principal())
        prin.start()

    def principal(self):
        self.raiz = Tk()
        self.raiz.title('   Tela Inicial ')
        self.raiz.state('zoomed')
        self.raiz.iconbitmap('img\ibnpa.ico')
        self.raiz.resizable(0, 0)

        img = ImageTk.PhotoImage(Image.open(r'img\yeshua.jpg'))
        self.imagem = Label(self.raiz, image=img)
        self.imagem.image = img
        self.imagem.place(relwidth=1, relheight=1)


        '''======= Campo de conecção com bancode dados =========='''

        try:
            con = sqlite3.connect('banco_de_dados.db')
            cursor = con.cursor()
            messagebox.showinfo('Banco de Dados', 'Banco de dados conectado com sucesso!')
        except:
            messagebox.showinfo('Banco de Dados', 'A conecção com o Banco de Dados falhou!!!')


        '''======= Campo Faixa do  Menu =========='''

        self._bg_menu = bg = '#0080FF'

        self.faixa_cor_menu = Label(self.raiz, text='', bg=self._bg_menu, width=900, height=3)
        self.faixa_cor_menu.place(x=1, y=2)

        '''======= Campo Imagem Botão Login e Logout =========='''

        self.img_botao_login = PhotoImage(file=r'img\button_login.png')
        self.img_botao_logout = PhotoImage(file=r'img\button_logout.png')

        '''======= Campo Botões do  Menu =========='''

        self.botao_logar = Button(self.raiz, image=self.img_botao_login, cursor='hand2', activebackground=self._bg_menu,
                                  command=self.chama_login, bg=self._bg_menu, bd=0)
        self.botao_logar.place(x=1200, y=5)
        self.botao_inicio = Button(self.raiz, text='Início', bg=self._bg_menu, fg='white', bd=0, font='bold 14',
                                   cursor='hand2', state='disabled', activebackground=self._bg_menu,
                                   command=self.destruir)
        self.botao_inicio.place(x=8, y=10)
        self.botao_cadastrar = Button(self.raiz, text='Cadastrar Aluno', bg=self._bg_menu, fg='white', bd=0,
                                      font='bold 14', cursor='hand2', activebackground=self._bg_menu,
                                      command=self.chama_cadastro, state='disabled')
        self.botao_cadastrar.place(x=160, y=10)
        self.botao_inserir = Button(self.raiz, text='Inserir Notas', bg=self._bg_menu, fg='white', bd=0, font='bold 14',
                                    cursor='hand2', activebackground=self._bg_menu, state='disabled')
        self.botao_inserir.place(x=340, y=10)
        self.botao_consultar = Button(self.raiz, text='Consultar', bg=self._bg_menu, fg='white', bd=0, font='bold 14',
                                      cursor='hand2', activebackground=self._bg_menu, state='disabled',
                                      command=self.option_menu_treeview)
        self.botao_consultar.place(x=495, y=10)
        self.botao_excluir = Button(self.raiz, text='Excluir', bg=self._bg_menu, fg='white', bd=0, font='bold 14',
                                    cursor='hand2', activebackground=self._bg_menu, state='disabled')
        self.botao_excluir.place(x=625, y=10)
        self.botao_sair = Button(self.raiz, text='Sair', bg=self._bg_menu, fg='white', bd=0, font='bold 14',
                                 cursor='hand2', activebackground=self._bg_menu, command=self.chama_sair)
        self.botao_sair.place(x=755, y=10)

        ''' Campo Chamada de Mensagem dos Botões do Menu '''


        self.botao_consultar.bind('<Enter>', self.msg_enter_botao_consultar)
        self.botao_consultar.bind('<Leave>', self.msg_leave_botao_consultar)
        self.botao_excluir.bind('<Enter>', self.msg_enter_botao_excluir)
        self.botao_excluir.bind('<Leave>', self.msg_leave_botao_excluir)

        self.raiz.mainloop()

    ''' Campo Funções das Mensagens Ocultas do Menu '''

    def msg_enter_botao_consultar(self, event):
        self.msg_botao_consultar = Label(self.raiz, text='Faz qualquer consulta\n sobre os alunos',
                                         fg='#848484', font='bold', bg='#E6E6E6')
        self.msg_botao_consultar.place(x=465, y=50, width=160, height=60)

    def msg_leave_botao_consultar(self, event):
        self.msg_botao_consultar.destroy()

    def msg_enter_botao_excluir(self, event):
        self.msg_botao_excluir = Label(self.raiz, text='Exclui qualquer coisa\n sobre os alunos', fg='#848484',
                                       font='bold', bg='#E6E6E6')
        self.msg_botao_excluir.place(x=595, y=50, width=160, height=60)

    def msg_leave_botao_excluir(self, event):
        self.msg_botao_excluir.destroy()

    '''======= Campo de TreeView =========='''

    def tree_view(self):
        self.barra_rolagem_tree_horiz = Scrollbar(self.raiz, orient=HORIZONTAL)
        self.barra_rolagem_tree_horiz.place(x=7, y=693, relwidth=0.98)

        self.barra_rolagem_tree_vert = Scrollbar(self.raiz, orient=VERTICAL)
        self.barra_rolagem_tree_vert.place(x=1346, y=151, relheight=0.75)


        self.tree = ttk.Treeview(self.raiz, columns=('', '', '', '', '', ''),
                                 xscrollcommand=self.barra_rolagem_tree_horiz.set,
                                 yscrollcommand=self.barra_rolagem_tree_vert.set)
        self.tree.place(x=7, y=150,  relheight=0.73, relwidth=0.98)
        self.tree.heading('#0', text='Nome', anchor=CENTER)
        self.tree.heading('#1', text='Senha', anchor=CENTER)
        self.tree.heading('#2', text='cpf', anchor=CENTER)
        self.tree.heading('#3', text='idade', anchor=CENTER)
        self.tree.heading('#4', text='endereço', anchor=CENTER)
        self.tree.heading('#5', text='identidade', anchor=CENTER)
        self.tree.heading('#6', text='sexo', anchor=CENTER)

        self.barra_rolagem_tree_horiz.config(command=self.tree.xview)
        self.barra_rolagem_tree_vert.config(command=self.tree.yview)
        #self.tree.insert('', '0', text='',  values=self.bd_select())

    def option_menu_treeview(self):
        self.opcoes = ['Opções de Pesquisa', 'Alunos', 'Notas', 'Presença']
        self.variavel_opcoes = StringVar()
        self.menu_de_opcoes = ttk.OptionMenu(self.raiz, self.variavel_opcoes, *self.opcoes)
        self.menu_de_opcoes.place(x=10, y=60, width=200)

        self.botao_opcao_consulta = Button(self.raiz, text='Consultar', bg='black', fg='white', font='bold 12',
                                           command=self.chama_consulta_all)
        self.botao_opcao_consulta.place(x=220, y=60)

    def chama_consulta_all(self):
        if (self.variavel_opcoes.get() == self.opcoes[1]):
            self.tree_view()

        elif (self.variavel_opcoes.get() == self.opcoes[2]):
            self.barra_rolagem_tree_horiz.destroy()
            self.barra_rolagem_tree_vert.destroy()
            self.tree.destroy()

        elif (self.variavel_opcoes.get() == self.opcoes[3]):
            pass

    def chama_sair(self):

        self.raiz.destroy()

    def destruir(self):
        try:
            self.barra_rolagem_tree_horiz.destroy()
            self.barra_rolagem_tree_vert.destroy()
            self.tree.destroy()
        except:
            pass

    def chama_cadastro(self):
        try:
            time.sleep(0.5)
            self.ativa_cadastro = 1
            cadastro.Cadastro()
        except:
            messagebox.showinfo('Janela de Cadastro', 'A janela de cadastro não pode ser aberta!')

    def chamada_logout(self):
        self.botao_logout = Button(self.raiz, image=self.img_botao_logout, bd=0, bg=self._bg_menu, cursor='hand2',
                                   activebackground=self._bg_menu, command=self.set_menu_desabilita)
        self.botao_logout.place(x=1200, y=5)

    def set_menu_secretaria_diretor(self):
        self.botao_inicio['state'] = 'normal'
        self.botao_cadastrar.configure(state='normal')
        self.botao_inserir.configure(state='normal')
        self.botao_consultar.configure(state='normal')
        self.botao_excluir.configure(state='normal')

    def set_menu_desabilita(self):
        self.botao_inicio['state'] = 'disabled'
        self.botao_cadastrar.configure(state='disabled')
        self.botao_inserir.configure(state='disabled')
        self.botao_consultar.configure(state='disabled')
        self.botao_excluir.configure(state='disabled')
        self.botao_logout.destroy()

    def libera_menu_professor(self):
        self.botao_inicio.configure(state='normal')
        self.botao_inserir.configure(state='normal')
        self.botao_consultar.configure(state='normal')
        self.botao_excluir.configure(state='normal')

    def chama_login(self):
        time.sleep(1)
        log = Thread(target=self.login())
        log.start()

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
    def login(self):
        # Transparencia onde (0) é totalmente transparente e (1) é totalmente opao
        #self.raiz.attributes('-alpha', 0.6)
        #self.raiz.deiconify()
        self.raiz_login = Toplevel()
        self.raiz_login.resizable(0, 0)
        self.raiz_login.title('>>>>>   TELA DE LOGIN   <<<<<')
        self.raiz_login['bg'] = '#088A85'
        self.raiz_login.attributes('-topmost')
        self.raiz_login.bind('<Return>', self.acesso_ao_sistema)

        self.raiz_login.iconbitmap('img\ibnpa.ico')

        self.entrada_de_dados()

        ''' Campo define janela centralizada '''

        window_width = 380
        window_height = 320
        screen_width = self.raiz_login.winfo_screenwidth()
        screen_height = self.raiz_login.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.raiz_login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


        self.raiz_login.mainloop()

    # Criando label e caixa de digitação para nome
    def entrada_de_dados(self):
        self.texto_principal = Label(self.raiz_login, font='newyork 14', bg='#088A85', fg='#8A4B08',
                                     text='Bem Vindo a Sua Tela de Login\nDigite seu Usuário e Senha\n Para Acessar')
        self.texto_principal.place(x=50, y=45)
        self.label_usuario = Label(self.raiz_login, text='Usuário:', font=('NewYork', '12', 'bold'), width=8,
                                   bg='#088A85', fg='#610B0B')
        self.label_usuario.place(x=2, y=150)
        self.entry_usuario = Entry(self.raiz_login, width=35, font=('NewYork', '10'), bg='#F2F5A9')
        self.entry_usuario.place(x=85, y=150)
        self.entry_usuario.focus()

        # Criando label e caixa de digitação para senha
        self.label_senha = Label(self.raiz_login, text='Senha:', font=('NewYork', '12', 'bold'), width=8,
                                 bg='#088A85', fg='#610B0B')
        self.label_senha.place(x=7, y=178)
        self.entry_senha = Entry(self.raiz_login, width=35, font=('NewYork', '10', 'bold'), bg='#F2F5A9', show='*')
        self.entry_senha.place(x=85, y=178)

        ''' ============== Campo Imagem botão Login ============='''

        self.img_botao_entrar = PhotoImage(file=r'button_entrar.png')
        self.botao_entrar = Button(self.raiz_login, image=self.img_botao_entrar, bg='#088A85', cursor='hand2',
                                   activebackground='#088A85', bd=0, command=self.acesso_ao_sistema)
        self.botao_entrar.image = self.img_botao_entrar
        self.botao_entrar.place(x=84, y=210)
        self.botao_entrar.update()


    def acesso_ao_sistema(self, event=None):
        nome = self.entry_usuario.get()
        senha = self.entry_senha.get()

        cursor.execute('''
                SELECT * FROM Cadastro
                WHERE (nome = ? and senha = ?) ;
                ''', (nome, senha))
        verificacao = cursor.fetchone()
        try:

            if nome in verificacao and senha in verificacao:
                messagebox.showinfo('Acesso', 'Login efetuado com sucesso!')
                self.raiz_login.destroy()
                self.set_menu_secretaria_diretor()
                self.chamada_logout()
        except:
            messagebox.showerror('Error', 'Usuário ou Senha Incorretos')
            self.raiz_login.focus_force()
            self.entry_usuario.delete(0, 'end')
            self.entry_senha.delete(0, 'end')
            self.entry_usuario.focus()



    '''
    ABAIXO VEMOS AS FUNÇÕES DO BANCO DE DADOS
    POR HORA VAMOS DEIXAR DENTRO DESTE ARQUIVO
    FUTURAMENTE FAZER UM ARQUIVO SOMENTE PARA BANCO DE DADOS
    '''

    def criar_tabela(self):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cadastro (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(10) NOT NULL, 
            senha VARCHAR(8) NOT NULL
        );     
        ''')

    def inserir_pessoa(self, nome, senha):
        cursor.execute('''
        INSERT INTO Cadastro (nome, senha)
        VALUES (?, ?)
        ''', (nome, senha))

        con.commit()

if __name__ == '__main__':
    App()








