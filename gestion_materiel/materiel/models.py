# materiel/models.py
from django.db import models

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Salle(models.Model):
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero

class Materiel(models.Model):
    BUDGET_CHOICES = [
        ('COURANT', 'Budget courant'),
        ('PROJETS', 'Budget projets'),
        ('EXCEPTIONNEL', 'Budget financements exceptionnels')
    ]
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES)
    responsable = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='responsable_materiel')
    localisation = models.ForeignKey(Salle, on_delete=models.CASCADE)
    possesseur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='possesseur_materiel')
    accessoires = models.TextField()

    def __str__(self):
        return self.nom

class Historique(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    ancien_possesseur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='ancien_possesseur')
    nouveau_possesseur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='nouveau_possesseur')
    date = models.DateTimeField(auto_now_add=True)
    lieu = models.ForeignKey(Salle, on_delete=models.CASCADE)
    occasion = models.CharField(max_length=100)
    etat_accessoires = models.TextField()

    def __str__(self):
        return f'{self.materiel.nom} - {self.date}'
