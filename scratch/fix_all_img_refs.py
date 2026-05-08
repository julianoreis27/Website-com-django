import os

# Mapeamento de nomes antigos para novos (baseado na renomeação anterior)
renames = {
    "alan benitez.webp": "alan_benitez.webp",
    "bone inter.webp": "bone_inter.webp",
    "cachecol inter.webp": "cachecol_inter.webp",
    "celeiro de ases.webp": "celeiro_de_ases.webp",
    "contratacao feminino.webp": "contratacao_feminino.webp",
    "copa do brasil titulo.jpg": "copa_do_brasil_titulo.jpg",
    "copa do brasil.jpeg": "copa_do_brasil.jpeg",
    "gol iluminado.jpg": "gol_iluminado.jpg",
    "hat trick.webp": "hat_trick.webp",
    "historia mundial.webp": "historia_mundial.webp",
    "inter 2025.jpg": "inter_2025.jpg",
    "inter feminino.jpg": "inter_feminino.jpg",
    "inter x ceara.png": "inter_x_ceara.png",
    "inter x santos.png": "inter_x_santos.png",
    "inter x vasco.png": "inter_x_vasco.png",
    "inter x vitoria.png": "inter_x_vitoria.png",
    "mochila inter.avif": "mochila_inter.avif",
    "reforma beira rio.jpg": "reforma_beira_rio.jpg",
    "rolo compressor.jpg": "rolo_compressor.jpg",
    "taça.jpg": "taca.jpg",
    "treino aberto.webp": "treino_aberto.webp"
}

path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'

for f in os.listdir(path):
    if f.endswith('.html'):
        filepath = os.path.join(path, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        for old, new in renames.items():
            if old in content:
                print(f"Fixing '{old}' in {f}")
                content = content.replace(old, new)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
        else:
            print(f"No changes needed in {f}")
