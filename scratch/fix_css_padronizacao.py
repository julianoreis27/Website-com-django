import re
import os

path = r'c:\Users\juliano.reis\Downloads\Website-com-django\static\css\style.css'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

new_block = """/* ── PADRONIZAÇÃO (HISTÓRIA, TÍTULOS, ELENCO) ── */
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

# Procura a seção de História e substitui
content = re.sub(r'/\* ── HISTÓRIA ── \*/.*?/\* ── LOJA ── \*/', new_block + '\n\n/* ── LOJA ── */', content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS padronizado com sucesso!")
