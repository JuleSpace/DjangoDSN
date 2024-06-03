from django.shortcuts import render, get_object_or_404, redirect
from .models import Enseignant, Salle, Materiel, Historique
from .forms import EnseignantForm, MaterielForm, ChangementPossesseurForm

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EnseignantForm()
    return render(request, 'ajouter_enseignant.html', {'form': form})

def ajouter_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            materiel.localisation = historique.lieu
            materiel.responsable = historique.nouveau_possesseur
            historique.save()
            materiel.save()
            return redirect('index')
    else:
        form = ChangementPossesseurForm()
    return render(request, 'changer_possesseur.html', {'form': form, 'materiel': materiel})



def index(request):
    enseignants = Enseignant.objects.all()
    salles = Salle.objects.all()
    materiels = Materiel.objects.all()
    return render(request, 'index.html', {'enseignants': enseignants, 'salles': salles, 'materiels': materiels})

def materiels_par_salle(request, salle_id=None):
    if salle_id:
        salle = get_object_or_404(Salle, id=salle_id)
        materiels = Materiel.objects.filter(localisation=salle)
        return render(request, 'materiels_par_salle.html', {'salle': salle, 'materiels': materiels})
    else:
        salles = Salle.objects.filter(materiel__isnull=False).distinct()
        return render(request, 'liste_salles.html', {'salles': salles})

def materiels_par_responsable(request, enseignant_id=None):
    if enseignant_id:
        enseignant = get_object_or_404(Enseignant, id=enseignant_id)
        materiels = Materiel.objects.filter(responsable=enseignant)
        return render(request, 'materiels_par_responsable.html', {'enseignant': enseignant, 'materiels': materiels})
    else:
        enseignants = Enseignant.objects.filter(responsable_materiel__isnull=False).distinct()
        return render(request, 'liste_enseignants.html', {'enseignants': enseignants})

def liste_materiels(request):
    materiels = Materiel.objects.all()
    return render(request, 'liste_materiels.html', {'materiels': materiels})

def historique_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    historique = Historique.objects.filter(materiel=materiel)
    return render(request, 'historique_materiel.html', {'materiel': materiel, 'historique': historique})

