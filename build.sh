#!/usr/bin/env bash
set -o errexit

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques
python manage.py collectstatic --no-input

# Appliquer les migrations
python manage.py migrate

# Créer automatiquement un superuser (si pas déjà existant)
#python create_superuser.py
