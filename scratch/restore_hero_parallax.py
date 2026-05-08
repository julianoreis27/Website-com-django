import os

templates_path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'

# 1. HISTORIA.HTML
path = os.path.join(templates_path, 'historia.html')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

hero_historia = """
    <section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(191,30,46,0.5)), url('{{ url_for('static', filename='imagens/reforma_beira_rio.jpg') }}'); background-attachment: fixed;">
        <div class="hero-content">
            <h1>A Epopeia Colorada</h1>
            <p>Uma trajetória forjada na inclusão e eternizada no topo do mundo.</p>
        </div>
    </section>

    <div class="corpo-historia">"""

content = content.replace('<div class="corpo">', hero_historia)
content = content.replace('<h1>História do Sport Club Internacional</h1>', '') # Remove título duplicado

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. TITULOS.HTML
path = os.path.join(templates_path, 'titulos.html')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

hero_titulos = """
    <section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(191,30,46,0.5)), url('{{ url_for('static', filename='imagens/brasileiro.jpg') }}'); background-attachment: fixed;">
        <div class="hero-content">
            <h1>Galeria de Glórias</h1>
            <p>Conquistas que orgulham uma nação inteira.</p>
        </div>
    </section>

    <main class="corpo-historia">"""

content = content.replace('<main class="corpo-historia">', hero_titulos)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# 3. ELENCO.HTML
path = os.path.join(templates_path, 'elenco.html')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

hero_elenco = """
    <section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(191,30,46,0.5)), url('{{ url_for('static', filename='imagens/inter_2025.jpg') }}'); background-attachment: fixed;">
        <div class="hero-content">
            <h1>Esquadrão Colorado</h1>
            <p>Os heróis que defendem o manto hoje.</p>
        </div>
    </section>

    <main><div class="corpo-historia">"""

content = content.replace('<main><div class="corpo-historia">', hero_elenco)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Efeito Parallax e Seções Hero restauradas com sucesso!")
