# Utiliser une image de base Python 3.8
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY . /app

# Installer les dépendances nécessaires
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc \
    && pip --timeout=1000 install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel Gunicorn va écouter
EXPOSE 8000

# Commande par défaut pour démarrer l'application avec Gunicorn
CMD ["gunicorn", "nom_du_projet.app:app", "-b", "0.0.0.0:8000", "-w", "4"]
