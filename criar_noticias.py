# criar_noticias.py
import sqlite3

conn = sqlite3.connect('noticias.db')
cursor = conn.cursor()

# Criação da tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS noticias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    imagem TEXT,
    url_endpoint TEXT,
    visibilidade TEXT NOT NULL
)
''')

# Inserção de notícias
noticias = [
    ("Internacional contrata lateral direito Alan Benitez", "Internacional contrata lateral direito Alan Benitez ...", "static/imagens/alan benitez.webp", "noticia_contratacao", "publica"),
    ("Elenco colorado conquista seu 46º título estadual", "Elenco colorado conquista seu 46º título estadual ...", "static/imagens/taça.jpg", "noticia_gauchao", "publica"),
    ("Inter vence Bahia e se classifica para o mata-mata", "Internacional vence Bahia de 2x1 e garante sua classificação para o mata-mata da libertadores ...", "static/imagens/bernabei.jpg", "noticia_libertadores", "logado")
]

for titulo, conteudo, imagem, endpoint, visibilidade in noticias:
    cursor.execute('''
        INSERT INTO noticias (titulo, conteudo, imagem, url_endpoint, visibilidade)
        VALUES (?, ?, ?, ?, ?)
    ''', (titulo, conteudo, imagem, endpoint, visibilidade))

conn.commit()
conn.close()
