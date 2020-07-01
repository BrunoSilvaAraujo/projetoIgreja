import sqlite3

con = sqlite3.connect('banco_de_dados.db')
cursor = con.cursor()

class Banco_db(object):
    def __init__(self):
        self.create_tables()
        self.insert_dados()
        self.consult_tables()
        self.delete_user()


    def create_tables(self):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS membros (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(30) NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            rua TEXT NOT NULL
        );
        ''')

        print(' Tabela criada com sucesso ')

    def insert_dados(self,):
        # Obtendo dados do usuário
        print('')
        print('***************************************************************************')
        print('***************************************************************************')
        print('***************************************************************************')
        print('****************     BLOCO DE INCLUSÃO DE MEMBROS     *********************')
        print('')

        parar_laço = True
        while parar_laço:
            print('')
            inserir = input(' Digite ( 1 ) para cadastrar um novo membro :  \n Digite ( 2 ) para não cadastrar : ')
            print('')

            if inserir == '1':
                nome = input(' Insira aqui o nome : ').title()
                cpf = input(' Insira aqui o CPF : ')
                rua = input(' Insira aqui a rua : ').title()

                # Inserindo dados do usuário
                cursor.execute('''
                INSERT INTO membros (nome, cpf, rua)
                VALUES (?,?,?)
                ''', (nome, cpf, rua))

                con.commit()
            elif inserir == '2':
                parar_laço = False
                print('')
                print(' SAINDO DO BLOCO DE INCLUSÃO DE MEMBROS. ')
                print('')
            elif inserir != '1' and '2':
                print(' Sua opção é inválida.')
                print(' Digite o número corretamente >>>')
                print('')

        print('')
        print('***************************************************************************')
        print('***************************************************************************')
        print('***************************************************************************')
        print('****************     TABELA DE MEMBROS CADASTRADOS     ********************')
        print('')

    def delete_user(self):
        print('')
        print('***************************************************************************')
        print('***************************************************************************')
        print('***************************************************************************')
        print('****************     BLOCO DE EXCLUSÃO DE MEMBROS     *********************')
        print('')

        parar_laço = True
        while parar_laço:
            print('')
            sair = input(' Digite ( 1 ) para deletar alguém da tabela acima : \n Digite ( 2 ) para sair: ')
            print('')

            if sair == '1':
                delete = input('inserir o nome para deletar : ').title()
                cursor.execute('''
                DELETE FROM membros
                WHERE nome = ?
                ''', (delete,))

                con.commit()
                print('')
                print(f' {delete} foi deletado(a) com sucesso. ')
                print('')

            elif sair == '2':
                parar_laço = False
                print('')
                print(' Saindo do processo.')
                print('')
            elif sair != '1' and '2':
                print('')
                print(' Sua opção foi inválida.')
                print(' Digite o número certo >>>')
                print('')

    def consult_tables(self):
        cursor.execute('''
        SELECT * FROM membros;
        ''')
        for i in cursor.fetchall():
            print(i)


if __name__ == '__main__':
    Banco_db()
