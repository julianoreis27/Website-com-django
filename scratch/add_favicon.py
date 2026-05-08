import os
import re

path = r'c:\Users\juliano.reis\Downloads\Website-com-django\templates'
icon_tag = "    <link rel=\"icon\" href=\"{{ url_for('static', filename='imagens/scinternacional.svg') }}\" type=\"image/svg+xml\">\n"

for f in os.listdir(path):
    if f.endswith('.html'):
        filepath = os.path.join(path, f)
        print(f"Adding favicon to {f}...")
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if 'rel="icon"' not in content:
            # Tenta inserir após o stylesheet
            if '<link rel="stylesheet"' in content:
                new_content = re.sub(r'(<link rel="stylesheet".*?>)', r'\1\n' + icon_tag, content)
            else:
                # Se não tiver stylesheet, insere após o <head>
                new_content = content.replace('<head>', '<head>\n' + icon_tag)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
        else:
            print(f"Favicon already exists in {f}")
