import sqlite3

conn = sqlite3.Connection('usuarios.db')


sql_criar_tabela_usuarios = '''
CREATE TABLE IF NOT EXISTS usuarios (
    nivel INTEGER NOT NULL,
    usuario TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cpf TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL
);
'''
conn.execute(sql_criar_tabela_usuarios)
conn.commit()


sql_insert_produtos = '''
INSERT INTO usuarios (nivel, usuario, nome, email, cpf, senha_hash) VALUES (?, ?, ?, ?, ?, ?);
'''

lista_de_usuarios = [
    (   
        '1',
        'jreis',
        'Juliano Reis',
        'julianoreis2006@gmail.com',
        '05415064044',
        'senha123'
    ),

    (   
        '0',
        'teste',
        'teste silva',
        'teste@gmail.com',
        '05400000000',
        'senha123'
    ),

]


conn.executemany(sql_insert_produtos, lista_de_usuarios)




conn.commit()

conn.close()