import os
import re

templates_path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'
target_files = [
    'loja.html', 
    'fale-conosco.html', 
    'login_administrador.html', 
    'login.html', 
    'associe-se.html'
]

for filename in target_files:
    filepath = os.path.join(templates_path, filename)
    if not os.path.exists(filepath):
        continue
    
    print(f"Padronizando {filename}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Substituir containers genéricos por .corpo-historia
    # Procura por <main>, <div class="container">, <div class="loja-container">, etc.
    content = content.replace('<main>', '<main class="corpo-historia">')
    content = content.replace('<div class="container">', '<div class="corpo-historia">')
    content = content.replace('<div class="loja-container">', '<div class="corpo-historia loja-grid">')
    content = content.replace('<div class="container-form">', '<div class="corpo-historia form-page">')
    
    # 2. Padronizar imagens
    content = content.replace('class="produto-img"', 'class="img-historia"')
    content = content.replace('class="plano-img"', 'class="img-historia"')
    
    # 3. Remover classes de títulos vermelhos/com fundo onde existirem
    content = content.replace('class="page-title"', 'style="border-bottom: none; color: var(--gray-900);"')
    content = content.replace('class="loja-hero"', 'class="hero-page-placeholder"') # Evita o fundo vermelho gigante
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Padronização concluída para todas as páginas solicitadas!")
