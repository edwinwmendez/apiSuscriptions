from pathlib import Path

# Ruta absoluta al directorio raíz de tu proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración para servir archivos estáticos
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Configuración de Gunicorn
bind = "0.0.0.0:8000"
workers = 3
