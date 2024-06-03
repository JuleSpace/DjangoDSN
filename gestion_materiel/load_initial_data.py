import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_materiel.settings')
django.setup()

from materiel.models import Enseignant, Salle, Materiel

# Ajout des enseignants
enseignants = [
    {"nom": "Dubois", "prenom": "Pierre"},
    {"nom": "Durand", "prenom": "Philippe"},
    {"nom": "Dupré", "prenom": "Thierry"},
    {"nom": "Dupuy", "prenom": "Sophie"}
]

for enseignant in enseignants:
    Enseignant.objects.get_or_create(nom=enseignant["nom"], prenom=enseignant["prenom"])

# Ajout des salles
salles = ["001", "101", "102", "103", "104", "105", "201", "202", "203", "204", "205", "301", "302", "303", "304", "305"]

for numero in salles:
    Salle.objects.get_or_create(numero=numero)

# Ajout des matériels avec détails complets
materiels = [
    {"nom": "Smartphone 1", "type": "Smartphone", "budget": "COURANT", "responsable_id": 1, "localisation_id": 1, "possesseur_id": 1, "accessoires": "Chargeur + câble USB"},
    {"nom": "Smartphone 2", "type": "Smartphone", "budget": "COURANT", "responsable_id": 2, "localisation_id": 1, "possesseur_id": 2, "accessoires": "Chargeur + câble USB"},
    {"nom": "Tablette 1", "type": "Tablette", "budget": "COURANT", "responsable_id": 3, "localisation_id": 1, "possesseur_id": 3, "accessoires": "Chargeur + câble USB"},
    {"nom": "Tablette 2", "type": "Tablette", "budget": "COURANT", "responsable_id": 4, "localisation_id": 1, "possesseur_id": 4, "accessoires": "Chargeur + câble USB"},
    {"nom": "Écran 1", "type": "Écran", "budget": "COURANT", "responsable_id": 1, "localisation_id": 1, "possesseur_id": 1, "accessoires": "Câble d’alimentation + câble HDMI"},
    {"nom": "Écran 2", "type": "Écran", "budget": "COURANT", "responsable_id": 2, "localisation_id": 1, "possesseur_id": 2, "accessoires": "Câble d’alimentation + câble HDMI"},
    {"nom": "Vidéo-projecteur 1", "type": "Vidéo-projecteur", "budget": "COURANT", "responsable_id": 3, "localisation_id": 1, "possesseur_id": 3, "accessoires": "Câble d’alimentation + câble HDMI"},
    {"nom": "Vidéo-projecteur 2", "type": "Vidéo-projecteur", "budget": "COURANT", "responsable_id": 4, "localisation_id": 1, "possesseur_id": 4, "accessoires": "Câble d’alimentation + câble HDMI"},
    {"nom": "Vidéo-projecteur 3", "type": "Vidéo-projecteur", "budget": "COURANT", "responsable_id": 1, "localisation_id": 1, "possesseur_id": 1, "accessoires": "Câble d’alimentation + câble HDMI"},
    {"nom": "Pointeur laser 1", "type": "Pointeur laser", "budget": "COURANT", "responsable_id": 2, "localisation_id": 1, "possesseur_id": 2, "accessoires": "Piles"},
    {"nom": "Pointeur laser 2", "type": "Pointeur laser", "budget": "COURANT", "responsable_id": 3, "localisation_id": 1, "possesseur_id": 3, "accessoires": "Piles"},
    {"nom": "Pointeur laser 3", "type": "Pointeur laser", "budget": "COURANT", "responsable_id": 4, "localisation_id": 1, "possesseur_id": 4, "accessoires": "Piles"}
]

for materiel in materiels:
    Materiel.objects.get_or_create(
        nom=materiel["nom"],
        type=materiel["type"],
        budget=materiel["budget"],
        responsable_id=materiel["responsable_id"],
        localisation_id=materiel["localisation_id"],
        possesseur_id=materiel["possesseur_id"],
        accessoires=materiel["accessoires"]
    )

print("Données initiales ajoutées avec succès")
