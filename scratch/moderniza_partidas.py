import os
import re

templates_path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'
partida_files = [
    ('partidas-ceara.html', 'Internacional x Ceará', 'ceara.webp'),
    ('partidas-vasco.html', 'Internacional x Vasco', 'inter_x_vasco.png'),
    ('partidas-santos.html', 'Internacional x Santos', 'inter_x_santos.png'),
    ('partidas-vitoria.html', 'Internacional x Vitória', 'inter_x_vitoria.png')
]

for filename, title, img_filename in partida_files:
    filepath = os.path.join(templates_path, filename)
    if not os.path.exists(filepath):
        continue
    
    print(f"Modernizando {filename}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Corrigir o título da aba
    content = content.replace('<title>História - Internacional</title>', f'<title>{title} - Internacional</title>')
    
    # 2. Adicionar Hero Page com Parallax e remover conteúdo antigo do topo
    # A imagem da partida será usada como fundo se possível, ou uma genérica do Beira-Rio
    hero_html = f"""
    <section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(191,30,46,0.5)), url('{{{{ url_for('static', filename='imagens/reforma_beira_rio.jpg') }}}}'); background-attachment: fixed;">
        <div class="hero-content">
            <h1>{title}</h1>
            <p>Brasileirão 2025 • Beira-Rio</p>
        </div>
    </section>

    <div class="corpo-historia">"""

    # Procura a div corpo-partidas e substitui pelo novo topo
    content = re.sub(r'<div class="corpo-partidas">.*?<h1>.*?Informações da Partida:.*?</h1>', hero_html, content, flags=re.DOTALL)
    
    # Ajusta o container final
    content = content.replace('</div>\n    \n\n    <footer>', '</div>\n    <footer>')
    
    # Padroniza as imagens dentro do conteúdo
    content = content.replace('class="card-times"', 'class="card-times corpo-historia"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Páginas de partidas modernizadas com sucesso!")
