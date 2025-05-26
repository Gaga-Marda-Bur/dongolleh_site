# create_superuser.py

import os
import django

from django.contrib.auth import get_user_model

# Définir le fichier settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dongolleh_site.settings")

# Initialiser Django
django.setup()

# Obtenir le modèle User
User = get_user_model()

# Infos du superutilisateur à créer
USERNAME = "dongadmin"
EMAIL = "gagapetitfils@gmail.com"
PASSWORD = "Marda..05D"

# Créer le superuser s'il n'existe pas déjà
if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"✅ Superutilisateur '{USERNAME}' créé avec succès.")
else:
    print(f"ℹ️ Superutilisateur '{USERNAME}' existe déjà.")
