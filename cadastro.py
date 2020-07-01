from tkinter import *
import time
from tkinter import messagebox
from tkcalendar import DateEntry


class Cadastro:
    def __init__(self):
        self.raiz = Toplevel()
        self.raiz.title('   IBNPA  AQUÁRIOS  _______  STEBAN-RJ  ________  FICHA DE CADASTRO')
        self.raiz['bg'] = 'lightblue'
        # Faz a janela iniciar em tamanho total
        self.raiz.state('zoomed')
        #self.raiz.geometry('1370x900')
        self.raiz.resizable(0, 0)
        self.raiz.iconbitmap('img\ibnpa.ico')

        '''================================ variavéis mais usadas ======================= '''
        fonte = font='Newyork 13 '
        background = bg='lightblue'
        foreground = fg='darkgreen'
        foreground_entry = fg='maroon'
        background_entry = '#FBF8EF'

        '''================================ Configura a variavel do radio buton ============== '''

        self.variavel_radio_button = IntVar()
        self.variavel_radio_button_sexo = IntVar()
        self.variavel_radio_button_documento = IntVar()
        self.variavel_radio_button_escolaridade = IntVar()
        self.variavel_radio_button_escolha_curso = IntVar()

        '''=============================== Campo titulo principal ======================= '''

        self.titulo_principal = Label(self.raiz, text='Ficha de Matrícula', font=('newyork 15 bold'),
                                      fg='white', bg='#0B0B61', width=113, height=2)
        self.titulo_principal.place(x=3, y=3)
        self.label_botao_curso = Label(self.raiz, text='Curso Pretendido:', font=fonte,
                                       fg='darkgreen', bg=background)
        self.label_botao_curso.place(x=20, y=60)

        '''=============================== Campo radio button curso ===================== '''

        self.botao_escolha_curso = Radiobutton(self.raiz, text='Básico', value=1, bg=background, font=fonte,
                                               fg='darkred', variable=self.variavel_radio_button_escolha_curso)
        self.botao_escolha_curso.place(x=160, y=60)
        self.botao_escolha_curso_2 = Radiobutton(self.raiz, text='Bacharel', value=2, bg=background, font=fonte,
                                                 fg='darkred', variable=self.variavel_radio_button_escolha_curso)
        self.botao_escolha_curso_2.place(x=260, y=60)

        '''========================= Campo titulo dados pessoais ================================================= '''

        self.titulo_dados_pessoais = Label(self.raiz, text='Dados Pessoais', bg=background, fg='#DF0101',
                                           font=('newyork 13 bold'))
        self.titulo_dados_pessoais.place(x=600, y=90)

        '''======================== Campo linha pontilhada de separação ========================================== '''

        self.linha_pontilhada_dupla = Label(self.raiz, text='=========' * 30, bg=background, fg='blue')
        self.linha_pontilhada_dupla.place(x=1, y=115)


        # Registra a funçao na raiz para retornar o que é digitado no entry
        validador = self.raiz.register(self.teste_msg)

        '''==================================== Campo nome  ======================================================= '''

        self.text_nome = Label(self.raiz, text='Nome:', bg=background, fg='darkgreen', font=fonte)
        self.text_nome.place(x=20, y=135)
        self.entry_nome = Entry(self.raiz, width=100, fg=foreground_entry, font='newyork 11', bd=2,
                                bg=background_entry, validate='key', validatecommand=(validador, '%S'))
        self.entry_nome.focus()
        self.entry_nome.place(x=73, y=135)

        '''==================================== Campo radio button sexo ========================================== '''

        self.texto_sexo = Label(self.raiz, text='Sexo:', bg=background, fg='darkgreen', font=fonte)
        self.texto_sexo.place(x=900, y=133)
        self.botao_masc_sexo = Radiobutton(self.raiz, text='M', value=1, variable=self.variavel_radio_button_sexo,
                                           bg=background, fg='darkred', font='newyork 11')
        self.botao_masc_sexo.place(x=950, y=133)
        self.botao_fem_sexo = Radiobutton(self.raiz, text='F', value=2, variable=self.variavel_radio_button_sexo,
                                          bg=background, fg='darkred', font='newyork 11')
        self.botao_fem_sexo.place(x=1000, y=133)

        '''=================================== Campo nacionalidade ======================'''

        self.texto_nacionalidade = Label(self.raiz, text='Nacionalidade:', font=fonte, bg=background,
                                         fg=foreground)
        self.texto_nacionalidade.place(x=20, y=163)
        self.entry_nacionalidade = Entry(self.raiz, width=40, fg=foreground_entry, font='newyork 11', bd=2,
                                         bg=background_entry)
        self.entry_nacionalidade.place(x=135, y=163)

        '''=================================== Campo naturalidade ======================= '''

        self.texto_naturalidade = Label(self.raiz, text='Naturalidade:', bg=background, font=fonte,
                                        fg=foreground)
        self.texto_naturalidade.place(x=483, y=163)
        self.entry_naturalidade = Entry(self.raiz, width=30, fg=foreground_entry, font='newyork 11',
                                        bg=background_entry, bd=2)
        self.entry_naturalidade.place(x=588, y=163)

        '''=================================== Campo data de nascimento ================== '''

        self.texto_data= Label(self.raiz, text='Data de Nascimento:', bg=background, font=fonte,
                               fg=foreground)
        self.texto_data.place(x=853, y=163)
        self.entry_data = Entry(self.raiz, width=41, fg=foreground_entry, font='newyork 11', bd=2, bg=background_entry)
        self.entry_data.place(x=1016, y=163)

        '''=================================== Campo filiação =============================='''

        self.titulo_filiacao = Label(self.raiz, text='Filiação__', bg=background, fg='red',
                                     font=fonte)
        self.titulo_filiacao.place(x=20, y=193)
        self.nome_pai = Label(self.raiz, text='Pai:', bg=background, fg='darkgreen', font=fonte)
        self.nome_pai.place(x=98, y=193)
        self.entry_pai = Entry(self.raiz, width=70, fg=foreground_entry, font='newyork 11', bd=2,
                               bg=background_entry)
        self.entry_pai.place(x=135, y=193)
        self.nome_mae = Label(self.raiz, text='Mãe:', bg=background, fg='darkgreen', font=fonte)
        self.nome_mae.place(x=720, y=193)
        self.entry_mae = Entry(self.raiz, width=72, fg=foreground_entry, font='newyork 11', bd=2,
                               bg=background_entry)
        self.entry_mae.place(x=768, y=193)

        '''==================================== Campo de profissão =========================='''

        self.nome_profissao = Label(self.raiz, text='Profissão:', bg=background, fg='darkgreen',
                                    font=fonte)
        self.nome_profissao.place(x=20, y=223)
        self.entry_profissao = Entry(self.raiz, width=70, fg=foreground_entry, font='newyork 11', bd=2,
                                     bg=background_entry)
        self.entry_profissao.place(x=103, y=223)

        '''==================================== Campo estado civil ==========================='''

        self.nome_estado_civil = Label(self.raiz, text='Estado Civil:', bg=background, fg='darkgreen',
                                       font=fonte)
        self.nome_estado_civil.place(x=685, y=223)
        self.entry_estado_civil = Entry(self.raiz, width=70, fg=foreground_entry, font='newyork 11', bd=2,
                                        bg=background_entry)
        self.entry_estado_civil.place(x=785, y=223)

        '''==================================== Campo identidade =============================='''

        self.nome_identidade = Label(self.raiz, text='Identidade:', bg=background, fg='darkgreen',
                                     font=fonte)
        self.nome_identidade.place(x=20, y=253)
        self.entry_identidade = Entry(self.raiz, width=30, fg=foreground_entry, font='newyork 11', bd=2,
                                      bg=background_entry)
        self.entry_identidade.place(x=110, y=253)

        '''===================================== Campo orgão expedidor ========================='''

        self.nome_orgao_expedidor = Label(self.raiz, text='Orgão Expedidor:', bg=background,
                                          fg='darkgreen', font=fonte)
        self.nome_orgao_expedidor.place(x=370, y=253)
        self.entry_orgao_expedidor = Entry(self.raiz, width=33, fg=foreground_entry, font='newyork 11', bd=2,
                                           bg=background_entry)
        self.entry_orgao_expedidor.place(x=509, y=253)

        '''====================================== Campo cpf ======================================'''

        self.nome_cpf = Label(self.raiz, text='Cpf:', bg=background, fg='darkgreen', font=fonte)
        self.nome_cpf.place(x=795, y=253)
        self.entry_cpf = Entry(self.raiz, width=40, fg=foreground_entry, font='newyork 11', bd=2,
                               bg=background_entry)
        self.entry_cpf.place(x=840, y=253)

        '''====================================== Campo endereço =================================='''

        self.nome_endereco = Label(self.raiz, text='Endereço:', bg=background, fg='darkgreen', font=fonte)
        self.nome_endereco.place(x=20, y=283)
        self.entry_endereco = Entry(self.raiz, width=70, fg=foreground_entry, font='newyork 11', bd=2,
                                    bg=background_entry)
        self.entry_endereco.place(x=110, y=283)

        '''====================================== Campo número =================================='''

        self.nome_numero = Label(self.raiz, text='Número:', bg=background, fg='darkgreen',
                                 font=fonte)
        self.nome_numero.place(x=690, y=283)
        self.entry_numero = Entry(self.raiz, width=8, fg=foreground_entry, font='newyork 11', bd=2,
                                  bg=background_entry)
        self.entry_numero.place(x=762, y=283)

        '''====================================== Campo complemento =================================='''

        self.nome_complemento = Label(self.raiz, text='Complemento:', bg=background, fg='darkgreen',
                                      font=fonte)
        self.nome_complemento.place(x=845, y=283)
        self.entry_complemento = Entry(self.raiz, width=48, fg=foreground_entry, font='newyork 11', bd=2,
                                       bg=background_entry)
        self.entry_complemento.place(x=960, y=283)

        '''====================================== Campo bairro ========================================'''

        self.nome_bairro = Label(self.raiz, text='Bairro:', bg=background, fg='darkgreen',
                                 font=fonte)
        self.nome_bairro.place(x=20, y=313)
        self.entry_bairro = Entry(self.raiz, width=45, fg=foreground_entry, font='newyork 11', bd=2,
                                  bg=background_entry)
        self.entry_bairro.place(x=80, y=313)

        '''====================================== Campo município ======================================'''

        self.nome_municipio = Label(self.raiz, text='Município:', bg=background, fg='darkgreen',
                                    font=fonte)
        self.nome_municipio.place(x=465, y=313)
        self.entry_municipio = Entry(self.raiz, width=40, fg=foreground_entry, font='newyork 11', bd=2,
                                     bg=background_entry)
        self.entry_municipio.place(x=551, y=313)

        '''====================================== Campo estado =========================================='''

        self.nome_estado = Label(self.raiz, text='Estado:', bg=background, fg='darkgreen', font=fonte)
        self.nome_estado.place(x=893, y=313)
        self.entry_estado = Entry(self.raiz, width=25, fg=foreground_entry, font='newyork 11', bd=2,
                                  bg=background_entry)
        self.entry_estado.place(x=960, y=313)

        '''====================================== Campo cep =============================================='''

        self.nome_cep = Label(self.raiz, text='Cep:', bg=background, fg='darkgreen', font=fonte)
        self.nome_cep.place(x=20, y=343)
        self.entry_cep = Entry(self.raiz, width=12, fg=foreground_entry, font='newyork 11', bd=2,
                               bg=background_entry)
        self.entry_cep.place(x=65, y=343)

        '''====================================== Campo tel. celular ======================================'''

        self.nome_tel_celular = Label(self.raiz, text='Tel. Celular:', bg=background, fg='darkgreen',
                                      font=fonte)
        self.nome_tel_celular.place(x=182, y=343)
        self.entry_tel_celular = Entry(self.raiz, width=30, fg=foreground_entry, font='newyork 11', bd=2,
                                       bg=background_entry)
        self.entry_tel_celular.place(x=278, y=343)

        '''====================================== Campo tel. residencial ==================================='''

        self.nome_tel_residencial = Label(self.raiz, text='Tel. Residencial:', bg=background, fg='darkgreen',
                                          font=fonte)
        self.nome_tel_residencial.place(x=540, y=343)
        self.entry_tel_residencial = Entry(self.raiz, width=30, fg=foreground_entry, font='newyork 11', bd=2,
                                           bg=background_entry)
        self.entry_tel_residencial.place(x=670, y=343)

        '''====================================== Campo email ==============================================='''

        self.nome_email = Label(self.raiz, text='E-mail:', bg=background, fg='darkgreen',font=fonte)
        self.nome_email.place(x=930, y=343)
        self.entry_email = Entry(self.raiz, width=44, fg=foreground_entry, font='newyork 11', bd=2,
                                 bg=background_entry)
        self.entry_email.place(x=990, y=343)

        '''====================================== Campo igreja  =============================================='''

        self.nome_igreja = Label(self.raiz, text='Igreja:', bg=background, fg='darkgreen',font=fonte)
        self.nome_igreja.place(x=20, y=373)
        self.entry_igreja = Entry(self.raiz, width=65, fg=foreground_entry, font='newyork 11', bd=2,
                                  bg=background_entry)
        self.entry_igreja.place(x=75, y=373)

        '''========================================= Campo nome do pastor  =========================================='''

        self.nome_pastor = Label(self.raiz, text='Nome do Pastor:', bg=background, fg='darkgreen', font=fonte)
        self.nome_pastor.place(x=620, y=373)
        self.entry_nome_pastor = Entry(self.raiz, width=74, fg=foreground_entry, font='newyork 11', bd=2,
                                       bg=background_entry)
        self.entry_nome_pastor.place(x=750, y=373)

        '''======================================== Campo titulo escolaridade  ======================================'''

        self.nome_escolaridade = Label(self.raiz, text='Escolaridade', bg=background, fg='#DF0101',
                                       font=('newyork 13 bold'))
        self.nome_escolaridade.place(x=600, y=413)

        '''============================== Campo 2° linha pontilhada de separação =================================== '''

        self.linha_pontilhada_dupla = Label(self.raiz, text='=========' * 30, bg=background, fg='blue')
        self.linha_pontilhada_dupla.place(x=1, y=438)

        '''===================================== Campo titulo grau de escolaridade ================================= '''

        self.titulo_grau_escolaridade = Label(self.raiz, text='Grau de Escolaridade:', bg=background, fg='darkgreen',
                                              font=fonte, )
        self.titulo_grau_escolaridade.place(x=20, y=458)

        '''=================================== Campo fundamental incompleto ======================================== '''

        self.fundamental_incompleto = Radiobutton(self.raiz, text='Ensino Fundamental Incompleto', value=1, font=fonte,
                                                  variable=self.variavel_radio_button_escolaridade, bg=background,
                                                  fg='darkred', command=self.habilita_desabilita_campo_curso_superior)
        self.fundamental_incompleto.place(x=200, y=458)

        '''===================================== Campo fundamental completo ======================================== '''

        self.fundamental_completo = Radiobutton(self.raiz, text='Ensino Fundamental Completo', value=2, font=fonte,
                                                variable=self.variavel_radio_button_escolaridade, bg=background,
                                                fg='darkred', command=self.habilita_desabilita_campo_curso_superior)
        self.fundamental_completo.place(x=470, y=458)

        '''====================================== Campo ensino medio incompleto ==================================== '''

        self.fundamental_incompleto = Radiobutton(self.raiz, text='Ensino Médio Incompleto', value=3, font=fonte,
                                                  variable=self.variavel_radio_button_escolaridade, bg=background,
                                                  fg='darkred', command=self.habilita_desabilita_campo_curso_superior)
        self.fundamental_incompleto.place(x=730, y=458)

        '''===================================== Campo ensino medio completo======================================== '''

        self.medio_completo = Radiobutton(self.raiz, text='Ensino Médio Completo', value=4, font=fonte,
                                          variable=self.variavel_radio_button_escolaridade, bg=background, fg='darkred',
                                          command=self.habilita_desabilita_campo_curso_superior)
        self.medio_completo.place(x=960, y=458)

        '''================================== Campo ensino superior  ================================================'''

        self.ensino_superior = Radiobutton(self.raiz, text='Ensino Superior', value=5, font=fonte,
                                           variable=self.variavel_radio_button_escolaridade, bg=background,
                                           fg='darkred', command=self.habilita_desabilita_campo_curso_superior)
        self.ensino_superior.place(x=1170, y=458)

        '''===================================== Campo descrição curso superior ================================= '''

        self.titulo_descricao_curso_superior = Label(self.raiz, text='Curso Superior:', bg=background, fg='darkgreen',
                                                     font=fonte, state='disabled')
        self.titulo_descricao_curso_superior.place(x=20, y=488)
        self.entry_descricao_curso_superior = Entry(self.raiz, width=60, fg=foreground_entry, font='newyork 11', bd=2,
                                                    bg=background_entry, state='disabled')
        self.entry_descricao_curso_superior.place(x=150, y=488)

        '''===================================== Campo descrição instituicao superior ============================== '''

        self.titulo_instituicao = Label(self.raiz, text='Nome Instituição:', bg=background, fg='darkgreen',
                                        font=fonte, state='disabled')
        self.titulo_instituicao.place(x=660, y=488)
        self.entry_instituicao = Entry(self.raiz, width=68, fg=foreground_entry, font='newyork 11', bd=2,
                                       bg=background_entry, state='disabled')
        self.entry_instituicao.place(x=800, y=488)

        '''===================================== Campo titulo curso idiomas ======================================== '''

        self.titulo_curso_idiomas = Label(self.raiz, text='Curso de Lingua Estrangeira:', bg=background,
                                          fg='darkgreen', font=fonte, )
        self.titulo_curso_idiomas.place(x=20, y=519)
        self.entry_idioma = Entry(self.raiz, width=35, fg=foreground_entry, font='newyork 11', bd=2,
                                  bg=background_entry)
        self.entry_idioma.place(x=250, y=519)

        '''================================== Campo Curso Teologico  ================================================'''

        self.titulo_curso_teologico = Label(self.raiz, text='Curso Teológico:', bg=background,
                                            fg='darkgreen', font=fonte, )
        self.titulo_curso_teologico.place(x=553, y=519)
        self.entry_curso_teologico = Entry(self.raiz, width=25, fg=foreground_entry, font='newyork 11', bd=2,
                                           bg=background_entry)
        self.entry_curso_teologico.place(x=690, y=519)

        '''================================== Campo Instituição Teologica  =========================================='''

        self.titulo_instituicao_teologica = Label(self.raiz, text='Instituíção:', bg=background,
                                                  fg='darkgreen', font=fonte, )
        self.titulo_instituicao_teologica.place(x=915, y=519)
        self.entry_instituicao_teologica = Entry(self.raiz, width=42, fg=foreground_entry, font='newyork 11', bd=2,
                                                 bg=background_entry)
        self.entry_instituicao_teologica.place(x=1008, y=519)

        '''=============================== Campo titulo documentos entregue   ======================================'''

        self.nome_escolaridade = Label(self.raiz, text='Documentos Entregues', bg=background, fg='#DF0101',
                                       font=('newyork 13 bold'))
        self.nome_escolaridade.place(x=600, y=559)

        '''============================== Campo 3° linha pontilhada de separação =================================== '''

        self.linha_pontilhada_dupla = Label(self.raiz, text='=========' * 30, bg=background, fg='blue')
        self.linha_pontilhada_dupla.place(x=1, y=584)

        '''================================== Campo opcões de documentos entregues  ================================='''

        self.opcao_certificado = Radiobutton(self.raiz, text='Certificado', value=1, font=fonte,
                                             variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_certificado.place(x=20, y=604)
        self.opcao_dec_trabalho = Radiobutton(self.raiz, text='Dec. Trabalho', value=2, font=fonte,
                                              variable=self.variavel_radio_button_documento,
                                              bg=background, fg='darkred')
        self.opcao_dec_trabalho.place(x=200, y=604)
        self.opcao_historico_escolar = Radiobutton(self.raiz, text='Histórico Escolar', value=3, font=fonte,
                                                   variable=self.variavel_radio_button_documento,
                                                   bg=background, fg='darkred')
        self.opcao_historico_escolar.place(x=400, y=604)
        self.opcao_certificado_reservista = Radiobutton(self.raiz, text='Certificado de Reservista', value=4,
                                                        font=fonte, variable=self.variavel_radio_button_documento,
                                                        bg=background, fg='darkred')
        self.opcao_certificado_reservista.place(x=640, y=604)
        self.opcao_termo_comp = Radiobutton(self.raiz, text='Termo Comp.', value=5, font=fonte,
                                            variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_termo_comp.place(x=900, y=604)
        self.opcao_fotos = Radiobutton(self.raiz, text='Fotos', value=6, font=fonte,
                                       variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_fotos.place(x=1090, y=604)
        self.opcao_comp_residencia = Radiobutton(self.raiz, text='Comp. Residência', value=7, font=fonte,
                                                 variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_comp_residencia.place(x=20, y=624)
        self.opcao_tipo_sangue = Radiobutton(self.raiz, text='Tipo Sangue', value=8, font=fonte,
                                             variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_tipo_sangue.place(x=200, y=624)
        self.opcao_carta_recomendacao = Radiobutton(self.raiz, text='Carta de Recomendação', value=9, font=fonte,
                                                    variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_carta_recomendacao.place(x=400, y=624)
        self.opcao_identidade = Radiobutton(self.raiz, text='Identidade', value=10, font=fonte,
                                            variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_identidade.place(x=640, y=624)
        self.opcao_certidao_cas_nasc = Radiobutton(self.raiz, text='Certidão (Nasc./Cas.)', value=11, font=fonte,
                                                   variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_certidao_cas_nasc.place(x=1090, y=624)
        self.opcao_cpf = Radiobutton(self.raiz, text='Cpf', value=12, font=fonte,
                                     variable=self.variavel_radio_button_documento, bg=background, fg='darkred')
        self.opcao_cpf.place(x=900, y=624)

        '''============================== Campo faixa de cor inferior  =========================================== '''

        self.faixa_de_cor = Label(self.raiz, text='', bg='#0B0B61', width=194, height=3)
        self.faixa_de_cor.place(x=1, y=654)

        '''================================== Campo imagens botões inferiores ======================================='''

        self.img_botao_gravar = PhotoImage(file=r'img\button_gravar.png')
        self.img_botao_limpar = PhotoImage(file=r'img\button_limpar.png')
        self.img_botao_cancelar = PhotoImage(file=r'img\button_cancelar.png')

        '''================================== Campo botões inferiores =============================================='''

        self.botao_gravar = Button(self.raiz, image=self.img_botao_gravar, bd=0, bg='#0B0B61',
                                   activebackground='#0B0B61', cursor='hand2')
        self.botao_gravar.place(x=1100, y=660)
        self.botao_limpar = Button(self.raiz, image=self.img_botao_limpar, bd=0, bg='#0B0B61',
                                   activebackground='#0B0B61', cursor='hand2', command=self.limpar)
        self.botao_limpar.place(x=830, y=660)
        self.botao_cancelar = Button(self.raiz, image=self.img_botao_cancelar, bd=0, bg='#0B0B61',
                                     activebackground='#0B0B61', cursor='hand2', command=self.fechar)
        self.botao_cancelar.place(x=560, y=660)

        self.raiz.mainloop()

    def teste_msg(self, S):
        if S.isdigit():
            self.msg_entry_nome()
        if S.isalpha():
            return True
        else:
            return False

    def msg_entry_nome(self):
        self.aviso_entry_nome = Label(self.raiz, text='este campo só pode receber letras', bg='blue')
        self.aviso_entry_nome.place(x=40, y=90)

    def destroi_msg_entry_nome(self):
        try:
            self.aviso_entry_nome.destroy()
        except:
            pass

    def habilita_desabilita_campo_curso_superior(self):
        self.confere = self.variavel_radio_button_escolaridade.get()
        if (self.confere == 5):
            self.titulo_descricao_curso_superior.configure(state='normal')
            self.entry_descricao_curso_superior.configure(state='normal')
            self.titulo_instituicao.configure(state='normal')
            self.entry_instituicao.configure(state='normal')
        if (self.confere == 4 or self.confere == 3 or self.confere == 2 or self.confere == 1):
            self.entry_descricao_curso_superior.delete(0, 'end')
            self.entry_instituicao.delete(0, 'end')
            self.titulo_descricao_curso_superior.configure(state='disabled')
            self.entry_descricao_curso_superior.configure(state='disabled')
            self.titulo_instituicao.configure(state='disabled')
            self.entry_instituicao.configure(state='disabled')

    def fechar(self):
        self.limpar()
        self.raiz.destroy()
        time.sleep(1)

    def limpar(self):
        self.entry_nome.delete(0, 'end')
        self.entry_nacionalidade.delete(0, 'end')
        self.entry_naturalidade.delete(0, 'end')
        self.entry_data.delete(0, 'end')
        self.entry_pai.delete(0, 'end')
        self.entry_mae.delete(0, 'end')
        self.entry_profissao.delete(0, 'end')
        self.entry_estado_civil.delete(0, 'end')
        self.entry_identidade.delete(0, 'end')
        self.entry_orgao_expedidor.delete(0, 'end')
        self.entry_cpf.delete(0, 'end')
        self.entry_endereco.delete(0, 'end')
        self.entry_numero.delete(0, 'end')
        self.entry_complemento.delete(0, 'end')
        self.entry_bairro.delete(0, 'end')
        self.entry_municipio.delete(0, 'end')
        self.entry_estado.delete(0, 'end')
        self.entry_cep.delete(0, 'end')
        self.entry_tel_celular.delete(0, 'end')
        self.entry_tel_residencial.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_igreja.delete(0, 'end')
        self.entry_nome_pastor.delete(0, 'end')
        self.entry_descricao_curso_superior.delete(0, 'end')
        self.entry_instituicao.delete(0, 'end')
        self.entry_idioma.delete(0, 'end')
        self.entry_curso_teologico.delete(0, 'end')
        self.entry_instituicao_teologica.delete(0, 'end')


if __name__ == '__main__':
    Cadastro()

