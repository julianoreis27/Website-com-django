import sqlite3
from flask import Flask, render_template, session, request, redirect, url_for
#Imports
app = Flask(__name__)



noticias_publica =  [   {
        "titulo": "Internacional contrata lateral direito Alan Benitez",
        "imagem": "static/imagens/alan benitez.webp",
        "endpoint": "noticia_contratacao"
    },
    {
        "titulo": "Internacional vence Bahia de 2x1 e garante sua classificação para o mata-mata da libertadores ...",
        "imagem": "static/imagens/bernabei.jpg",
        "endpoint": "noticia_libertadores"
    },
    {
       "titulo": "Elenco colorado conquista seu 46º título do campeonato estadual ... ",
        "imagem": "static/imagens/taça.jpg",
        "endpoint": "noticia_gauchao"  
        }
    ]

noticias_logado = [{
        "titulo": "Internacional sofre derrota de 2x1 no Beira Rio para o Fluminense...",
        "imagem": "static/imagens/fluminense.jpg",
        "endpoint": "noticia_gauchao"},
{
       "titulo": "Internacional contrata meio-campo uruguaio Alan Rodríguez...",
        "imagem": "static/imagens/alan_rodriguez.webp",
        "endpoint": "noticia_gauchao"
}, 
     
{
       "titulo": "Repercurção no vestiário colorado que envolve 4 jogadores e filha de empresário... ",
        "imagem": "static/imagens/amarok.jpg",
        "endpoint": "noticia_gauchao"
}
]

@app.route('/')
def home():
    if 'nome' in session:
        noticias = noticias_logado

    else:
        noticias = noticias_publica

    return render_template('index.html', noticias=noticias, nome=session.get('nome'))

@app.route('/elenco')
def elenco():
    return render_template('elenco.html')


@app.route('/associe-se')
def associe_se():
    return render_template('associe-se.html')


@app.route('/fale-conosco')
def fale_conosco():
    return render_template('fale-conosco.html')

@app.route('/pagina_usuario')
def pagina_usuario():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    usuario = session['usuario']

    # buscar dados no banco de dados
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nome, email, cpf FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

    if resultado:
        nome, email, cpf = resultado
        return render_template('pagina_usuario.html', nome=nome, email=email, cpf=cpf)
    else:
        return "Usuário não encontrado", 404

@app.route('/historia')
def historia():
    return render_template('historia.html')


@app.route('/loja')
def loja():
    return render_template('loja.html')


@app.route('/noticia_contratacao')
def noticia_contratacao():
    return render_template('manchete_noticia_contratacao.html')

@app.route('/noticia_gauchao')
def noticia_gauchao():
    return render_template('manchete_noticia_gauchao.html')

@app.route('/noticia_libertadores')
def noticia_libertadores():
    return render_template('manchete_noticia_libertadores.html')


@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/titulos')
def titulos():
    return render_template('titulos.html')

@app.route('/partidas-ceara')
def partidas_ceara():
    return render_template('partidas-ceara.html')

@app.route('/partidas-santos')
def partidas_santos():
    return render_template('partidas-santos.html')

@app.route('/partidas-vasco')
def partidas_vasco():
    return render_template('partidas-vasco.html')

@app.route('/partidas-vitoria')
def partidas_vitoria():
    return render_template('partidas-vitoria.html')

@app.route('/ola')
def pagina_ola():
    return render_template('ola.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        with sqlite3.connect('usuarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT senha_hash, nome FROM usuarios WHERE usuario = ?', (usuario,))
            resultado = cursor.fetchone()

            if resultado is None:
                erro = 'Usuário não encontrado.'
            else:
                senha_correta = (resultado[0] == senha)
                if senha_correta:
                    session['usuario'] = usuario
                    session['nome'] = resultado[1]
                    return redirect(url_for('home'))
                else:
                    erro = 'Senha incorreta.'

    return render_template('login.html', erro=erro)


###########################################
@app.post('/login')
def validar_login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    nome = buscar_nome_usuario(usuario, senha)

    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        if nome:
            session['nome'] = nome
            session['usuario'] = usuario
            return render_template("ola.html", nome=nome)
        cursor.execute("SELECT 1 FROM usuarios WHERE usuario = ?", (usuario,))
        if cursor.fetchone():
            return render_template("login.html", erro)

#FUNÇÃO PARA BUSCAR O NOME DO USUÁRIO:
def buscar_nome_usuario(usuario, senha):
    with sqlite3.connect("usuarios.db") as conn:
        cursor = conn.cursor()
        sql = "SELECT nome FROM usuarios WHERE usuario = ? AND senha_hash = ?"
        cursor.execute(sql, (usuario, senha))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None




@app.route('/criar_cadastro_pagina')
def criar_cadastro_pagina():
    return render_template('criar_cadastro.html')

@app.post('/criar_cadastro')
def criar_cadastro():
    usuario = request.form['usuario']
    nome = request.form['nome']
    email = request.form['email'] 
    cpf = request.form['cpf']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    if senha != confirmar_senha:
        return render_template("criar_cadastro.html",
                               erro="As senhas não coincidem.",
                               usuario=usuario, nome=nome, email=email, cpf=cpf)

    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM usuarios WHERE usuario = ?", (usuario,))
        if cursor.fetchone():
            return render_template("criar_cadastro.html",
                                   erro="Usuário já existe. Escolha outro nome.",
                                   usuario=usuario, nome=nome, email=email, cpf=cpf)

        cursor.execute("SELECT 1 FROM usuarios WHERE email = ?", (email,))
        if cursor.fetchone():
            return render_template("criar_cadastro.html",
                                   erro="E-mail já cadastrado.",
                                   usuario=usuario, nome=nome, email=email, cpf=cpf)

        cursor.execute("SELECT 1 FROM usuarios WHERE cpf = ?", (cpf,))
        if cursor.fetchone():
            return render_template("criar_cadastro.html",
                                   erro="CPF já cadastrado.",
                                   usuario=usuario, nome=nome, email=email, cpf=cpf)

        # Aqui define o nível fixo como 0 (usuário comum)
        sql = '''
        INSERT INTO usuarios (nivel, usuario, nome, email, cpf, senha_hash)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(sql, (0, usuario, nome, email, cpf, senha))  # <- nível 0 aqui
        conn.commit()

    return redirect(url_for('login'))



@app.context_processor
def inject_user():
    nome = session.get('nome')
    return dict(nome_usuario=nome)
app.secret_key = '1234'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/login_administrador')
def login_administrador():
    return render_template('login_administrador.html')



#FIM CÓDIGO
if __name__ == '__main__':
    app.run(debug=True)
