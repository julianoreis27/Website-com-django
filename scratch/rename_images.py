import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        if ' ' in filename or any(c in filename for c in 'áàâãéèêíìîóòôõúùûç'):
            new_name = filename.lower()
            new_name = new_name.replace(' ', '_')
            new_name = new_name.replace('á', 'a').replace('à', 'a').replace('â', 'a').replace('ã', 'a')
            new_name = new_name.replace('é', 'e').replace('è', 'e').replace('ê', 'e')
            new_name = new_name.replace('í', 'i').replace('ì', 'i').replace('î', 'i')
            new_name = new_name.replace('ó', 'o').replace('ò', 'o').replace('ô', 'o').replace('õ', 'o')
            new_name = new_name.replace('ú', 'u').replace('ù', 'u').replace('û', 'u')
            new_name = new_name.replace('ç', 'c')
            
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            print(f"Renaming: {filename} -> {new_name}")
            try:
                os.rename(old_path, new_path)
            except FileExistsError:
                print(f"File {new_name} already exists, skipping.")

directories = [
    r'c:\Users\juliano.reis\Downloads\Website-com-django\static\imagens',
    r'c:\Users\juliano.reis\Downloads\Website-com-django\static\imagens-elenco'
]

for d in directories:
    if os.path.exists(d):
        rename_files(d)
    else:
        print(f"Directory not found: {d}")
