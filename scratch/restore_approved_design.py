import os
import re

templates_path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'
css_path = r'c:\Users\juliano.reis\Downloads\Website-com-django\static\css\style.css'

# 1. Restaurar CSS Padronizado
new_css_block = """/* ── PADRONIZAÇÃO (HISTÓRIA, TÍTULOS, ELENCO) ── */
.corpo-historia {
  padding: 60px 20px;
  max-width: 1100px;
  margin: 0 auto;
  font-family: 'Inter', sans-serif;
}
.corpo-historia h1 {
  font-size: 32px;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--red);
  letter-spacing: 1px;
  margin-bottom: 30px;
  text-align: center;
  border-bottom: 3px solid var(--red);
  padding-bottom: 10px;
}
.corpo-historia h2 {
  font-size: 22px;
  color: var(--red-dark);
  font-weight: 700;
  margin: 40px 0 20px;
  text-transform: uppercase;
}
.corpo-historia p {
  line-height: 1.8;
  font-size: 16px;
  margin-bottom: 20px;
  color: #333;
}
.img-historia {
  display: block;
  margin: 30px auto;
  max-width: 100%;
  height: auto;
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
  transition: var(--transition);
}
.img-historia:hover {
  transform: scale(1.02);
  box-shadow: var(--shadow-lg);
}"""

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if "/* ── HISTÓRIA ── */" in css_content:
    css_content = re.sub(r'/\* ── HISTÓRIA ── \*/.*?/\* ── LOJA ── \*/', new_css_block + '\n\n/* ── LOJA ── */', css_content, flags=re.DOTALL)
else:
    # Se não achar o comentário, adiciona no final
    css_content += "\n\n" + new_css_block

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Atualizar HISTORIA.HTML
hist_path = os.path.join(templates_path, 'historia.html')
with open(hist_path, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('<div class="corpo">', '<div class="corpo-historia">')
with open(hist_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Atualizar TITULOS.HTML
tit_path = os.path.join(templates_path, 'titulos.html')
with open(tit_path, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('<main class="corpo_titulos">', '<main class="corpo-historia">')
content = content.replace('class="imagem-titulos"', 'class="img-historia"')
with open(tit_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 4. Atualizar ELENCO.HTML
ele_path = os.path.join(templates_path, 'elenco.html')
with open(ele_path, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('<div class="container">', '<div class="corpo-historia">')
content = content.replace('<h1 class="page-title">Nosso Elenco Principal</h1>', '<h1 style="border-bottom: none; color: var(--gray-900);">Nosso Elenco Principal</h1>')
with open(ele_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Design restaurado para História, Títulos e Elenco!")
