import sqlite3

con = sqlite3.connect('banco_de_dados.db')
cursor = con.cursor()

class Database:
    def criar_tabelas(self):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos(
            id aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            cpf VARCHAR(11) NOT NULL,
            nome VARCHAR(30) NOT NULL,
            sexo VARCHAR(10) NOT NULL, 
            naturalidade VARCHAR(10) NOT NULL,
            nacionalidade VARCHAR(10) NOT NULL,
            data_nascimento DATE NOT NULL,
            pai VARCHAR(30) NOT NULL,
            mae VARCHAR(30) NOT NULL,
            profissao VARCHAR(20) NOT NULL,
            estado_civil VARCHAR(10) NOT NULL,
            identidade INTEGER NOT NULL,
            orgao_expedidor VARCHAR(10) NOT NULL,
            igreja VARCHAR(30) NOT NULL,
            nome_do_pastor VARCHAR(30) NOT NULL,
        );
        ''')