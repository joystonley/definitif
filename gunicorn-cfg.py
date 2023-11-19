# gunicorn_config.py

import multiprocessing
import os

# Adresse et port sur lesquels Gunicorn écoutera
bind = "0.0.0.0:8000"

# Nombre de travailleurs Gunicorn
workers = multiprocessing.cpu_count() * 2 + 1

# Déterminez le chemin complet du module d'application
# Utilisez 'vaovao' comme nom de projet Django
app_module = "vaovao.core.wsgi:application"

# Optionnel : spécifiez le répertoire de travail
chdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vaovao')
