import os
import re

templates_path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'
partida_files = [
    ('partidas-ceara.html', 'Internacional x Ceará', 'ceara.webp', '20/07/2025, 11:00', 'Beira-Rio'),
    ('partidas-vasco.html', 'Internacional x Vasco', 'inter_x_vasco.png', '10/08/2025, 16:00', 'Beira-Rio'),
    ('partidas-santos.html', 'Internacional x Santos', 'inter_x_santos.png', '15/09/2025, 18:30', 'Vila Belmiro'),
    ('partidas-vitoria.html', 'Internacional x Vitória', 'inter_x_vitoria.png', '05/10/2025, 16:00', 'Barradão')
]

for filename, title, img_filename, data_hora, local in partida_files:
    filepath = os.path.join(templates_path, filename)
    if not os.path.exists(filepath):
        continue
    
    print(f"Estruturando {filename} no padrão Títulos...")
    
    new_content = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Internacional</title>
    <link rel="stylesheet" href="{{{{ url_for('static', filename='css/style.css') }}}}">
    <link rel="icon" href="{{{{ url_for('static', filename='imagens/scinternacional.svg') }}}}" type="image/svg+xml">
</head>
<body>
    <header>
        <a href="{{{{ url_for('home') }}}}">
            <img src="{{{{ url_for('static', filename='imagens/scinternacional.svg') }}}}" alt="Inter Clube do Povo">
        </a>
        <ul>
            <li><a href="{{{{ url_for('elenco') }}}}">ELENCO</a></li>
            <li><a href="{{{{ url_for('historia') }}}}">HISTÓRIA</a></li>
            <li><a href="{{{{ url_for('titulos') }}}}">TÍTULOS</a></li>
            <li><a href="{{{{ url_for('noticias') }}}}">NOTÍCIAS</a></li>
            <li><a href="{{{{ url_for('associe_se') }}}}">ASSOCIE-SE</a></li>
            <li><a href="{{{{ url_for('loja') }}}}">LOJA OFICIAL</a></li>
            <li><a href="{{{{ url_for('fale_conosco') }}}}">FALE-CONOSCO</a></li>
        </ul>
    </header>

    <section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(191,30,46,0.5)), url('{{{{ url_for('static', filename='imagens/reforma_beira_rio.jpg') }}}}'); background-attachment: fixed;">
        <div class="hero-content">
            <h1>{title}</h1>
            <p>Próximo Desafio • Brasileirão 2025</p>
        </div>
    </section>

    <main class="corpo-historia">
        <section class="titulos">
            <h1>Informações da Partida</h1>
            
            <article>
                <h2>Local e Data</h2>
                <div class="bloco">
                    <img src="{{{{ url_for('static', filename='imagens/reforma_beira_rio.jpg') }}}}" alt="Estádio" class="img-historia">
                    <p>A partida será realizada no <strong>{local}</strong> em <strong>{data_hora}</strong>. Prepare o seu manto e venha apoiar o Colorado em busca de mais uma vitória rumo ao topo da tabela!</p>
                </div>
            </article>

            <article>
                <h2>Escalação Provável</h2>
                <div class="bloco">
                    <p>O Internacional deve entrar em campo com força total, focando na organização defensiva e na velocidade dos contra-ataques. A base da equipe de 2025 vem demonstrando grande entrosamento.</p>
                </div>
            </article>

            <article>
                <h2>O Adversário</h2>
                <div class="bloco">
                    <p>Enfrentar o adversário exige foco e raça. Historicamente, os confrontos contra equipes tradicionais do Brasileirão são decididos no detalhe, e o apoio da torcida será fundamental.</p>
                </div>
            </article>
        </section>
    </main>

    <footer>
        <div class="footer-container">
            <div class="footer-logo">
               <a href="{{{{ url_for('home') }}}}"><img src="{{{{ url_for('static', filename='imagens/scinternacional.svg') }}}}" alt="Internacional Logo"> </a>
            </div>
            <div class="footer-links">
                <h3>Clube</h3>
                <ul>
                    <li><a href="{{{{ url_for('elenco') }}}}">Elenco</a></li>
                    <li><a href="{{{{ url_for('historia') }}}}">História</a></li>
                    <li><a href="{{{{ url_for('titulos') }}}}">Títulos</a></li>
                    <li><a href="{{{{ url_for('noticias') }}}}">Notícias</a></li>
                </ul>
            </div>
        </div>
        <p class="footer-copy">&copy; 2025 Sport Club Internacional. Todos os direitos reservados.</p>
    </footer>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Páginas de partidas reestruturadas no padrão Títulos!")
