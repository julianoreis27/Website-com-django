import sys
import os

# Adiciona o diretório pai ao path para importar app.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Exporta para a Vercel
export = app
