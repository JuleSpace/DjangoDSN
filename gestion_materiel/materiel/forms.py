# materiel/forms.py
from django import forms
from .models import Enseignant, Materiel, Historique

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['nom', 'type', 'budget', 'responsable', 'localisation', 'possesseur', 'accessoires']

class ChangementPossesseurForm(forms.ModelForm):
    class Meta:
        model = Historique
        fields = ['nouveau_possesseur', 'lieu', 'occasion', 'etat_accessoires']
