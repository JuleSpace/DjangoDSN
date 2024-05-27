# materiel/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Enseignant, Salle, Materiel, Historique
from .forms import EnseignantForm, MaterielForm, ChangementPossesseurForm

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm()
    return render(request, 'ajouter_enseignant.html', {'form': form})

def ajouter_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_materiels')
    else:
        form = MaterielForm()
    return render(request, 'ajouter_materiel.html', {'form': form})

def changer_possesseur(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    if request.method == 'POST':
        form = ChangementPossesseurForm(request.POST)
        if form.is_valid():
            historique = form.save(commit=False)
            historique.materiel = materiel
            historique.ancien_possesseur = materiel.possesseur
            materiel.possesseur = historique.nouveau_possesseur
            historique.save()
            materiel.save()
            return redirect('detail_materiel', materiel_id=materiel.id)
    else:
        form = ChangementPossesseurForm()
    return render(request, 'changer_possesseur.html', {'form': form, 'materiel': materiel})
