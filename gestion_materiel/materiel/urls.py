from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajouter_enseignant/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('ajouter_materiel/', views.ajouter_materiel, name='ajouter_materiel'),
    path('changer_possesseur/<int:materiel_id>/', views.changer_possesseur, name='changer_possesseur'),
    path('materiels_par_salle/', views.materiels_par_salle, name='materiels_par_salle'),
    path('materiels_par_salle/<int:salle_id>/', views.materiels_par_salle, name='materiels_par_salle'),
    path('materiels_par_responsable/', views.materiels_par_responsable, name='materiels_par_responsable'),
    path('materiels_par_responsable/<int:enseignant_id>/', views.materiels_par_responsable, name='materiels_par_responsable'),
    path('historique_materiel/', views.liste_materiels, name='historique_materiel'),
    path('historique_materiel/<int:materiel_id>/', views.historique_materiel, name='historique_materiel_detail'),
]
