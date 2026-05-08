import os

path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates\historia.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Tag original no topo da página
old_tag = '<section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(191,30,46,0.5)), url(\'{{ url_for(\'static\', filename=\'imagens/reforma_beira_rio.jpg\') }}\'); background-size: cover; background-position: center; min-height: 450px; display: flex; align-items: center; justify-content: center;">'

# Nova tag com Parallax (background-attachment: fixed)
new_tag = '<section class="hero-page" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(191,30,46,0.5)), url(\'{{ url_for(\'static\', filename=\'imagens/reforma_beira_rio.jpg\') }}\'); background-size: cover; background-position: center; background-attachment: fixed; min-height: 450px; display: flex; align-items: center; justify-content: center;">'

if old_tag in content:
    content = content.replace(old_tag, new_tag)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Parallax aplicado com sucesso na História!")
else:
    print("Tag original não encontrada. Verifique se o arquivo já foi alterado.")
