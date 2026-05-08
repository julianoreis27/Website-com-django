import os

templates_path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'

# Dados específicos de cada partida
partidas = [
    {
        'file': 'partidas-vasco.html',
        'titulo': 'Internacional x Vasco',
        'adversario': 'VASCO DA GAMA',
        'img_adv': 'imagens partidas/ceara.webp', # Usando a que está disponível ou similar
        'data': '10 de Agosto, 2025',
        'horario': 'Domingo às 16:00',
        'local': 'Estádio Beira-Rio',
        'cidade': 'Porto Alegre, RS'
    },
    {
        'file': 'partidas-santos.html',
        'titulo': 'Internacional x Santos',
        'adversario': 'SANTOS FC',
        'img_adv': 'imagens partidas/ceara.webp',
        'data': '15 de Setembro, 2025',
        'horario': 'Segunda às 18:30',
        'local': 'Vila Belmiro',
        'cidade': 'Santos, SP'
    },
    {
        'file': 'partidas-vitoria.html',
        'titulo': 'Internacional x Vitória',
        'adversario': 'EC VITÓRIA',
        'img_adv': 'imagens partidas/ceara.webp',
        'data': '05 de Outubro, 2025',
        'horario': 'Domingo às 16:00',
        'local': 'Estádio Barradão',
        'cidade': 'Salvador, BA'
    }
]

for p in partidas:
    filepath = os.path.join(templates_path, p['file'])
    print(f"Modernizando {p['file']}...")
    
    content = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p['titulo']} - Match Center</title>
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

    <section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.8), rgba(191,30,46,0.6)), url('{{{{ url_for('static', filename='imagens/reforma_beira_rio.jpg') }}}}'); background-attachment: fixed;">
        <div class="hero-content">
            <span class="era-badge" style="background: var(--gold); color: var(--gray-900);">Brasileirão 2025 • Confronto Direto</span>
            <h1>{p['titulo']}</h1>
            <p>Todas as informações sobre o próximo duelo do Colorado</p>
        </div>
    </section>

    <main class="corpo-historia">
        <div class="match-center-header" style="display: flex; justify-content: space-around; align-items: center; padding: 40px 0; background: var(--gray-100); border-radius: 20px; margin-bottom: 40px; box-shadow: var(--shadow-sm);">
            <div class="team-info" style="text-align: center;">
                <img src="{{{{ url_for('static', filename='imagens/scinternacional.svg') }}}}" alt="Inter" style="width: 120px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
                <h2 style="margin-top: 15px; color: var(--red);">INTERNACIONAL</h2>
            </div>
            <div class="vs" style="text-align: center;">
                <h1 style="font-size: 4rem; color: var(--gray-400); margin: 0; border: none;">VS</h1>
            </div>
            <div class="team-info" style="text-align: center;">
                <img src="{{{{ url_for('static', filename='imagens/scinternacional.svg') }}}}" alt="{p['adversario']}" style="width: 120px; border-radius: 50%; box-shadow: 0 4px 15px rgba(0,0,0,0.2); filter: grayscale(1);">
                <h2 style="margin-top: 15px; color: var(--gray-800);">{p['adversario']}</h2>
            </div>
        </div>

        <div class="info-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 50px;">
            <div class="info-card" style="background: var(--white); padding: 25px; border-radius: 15px; border-left: 5px solid var(--red); box-shadow: var(--shadow-sm);">
                <h3 style="color: var(--red); font-size: 0.9rem; text-transform: uppercase; margin-bottom: 10px;">Local da Partida</h3>
                <p style="font-size: 1.2rem; font-weight: 700; color: var(--gray-900);">{p['local']}</p>
                <p style="color: var(--gray-600);">{p['cidade']}</p>
            </div>
            <div class="info-card" style="background: var(--white); padding: 25px; border-radius: 15px; border-left: 5px solid var(--gold); box-shadow: var(--shadow-sm);">
                <h3 style="color: var(--gold); font-size: 0.9rem; text-transform: uppercase; margin-bottom: 10px;">Data e Horário</h3>
                <p style="font-size: 1.2rem; font-weight: 700; color: var(--gray-900);">{p['data']}</p>
                <p style="color: var(--gray-600);">{p['horario']}</p>
            </div>
        </div>

        <h2 style="text-align: center; margin-bottom: 30px; font-weight: 900; color: var(--red);">PROVÁVEIS TIMES</h2>
        <div class="lineups" style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 60px;">
            <div class="lineup-card">
                <h3 style="text-align: center; margin-bottom: 15px; font-size: 1.1rem; color: var(--red);">Internacional</h3>
                <img src="{{{{ url_for('static', filename='imagens partidas/inter elenco x vitoria.png') }}}}" alt="Escalação Inter" class="img-historia" style="margin: 0;">
            </div>
            <div class="lineup-card">
                <h3 style="text-align: center; margin-bottom: 15px; font-size: 1.1rem; color: var(--gray-700);">Adversário</h3>
                <p style="text-align: center; padding: 40px; background: var(--gray-200); border-radius: 15px;">Escalação em análise tática pelo comando técnico.</p>
            </div>
        </div>

        <div class="tabela-section" style="background: var(--gray-900); padding: 40px; border-radius: 20px; color: var(--white);">
            <h2 style="color: var(--gold); margin-bottom: 25px; text-align: center;">Classificação Atual</h2>
            <img src="{{{{ url_for('static', filename='imagens partidas/tabela brasileirao.png') }}}}" alt="Tabela" class="img-historia" style="max-width: 800px; opacity: 0.95;">
        </div>
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
        f.write(content)

print("Match Center aplicado em todas as páginas!")
