# gestion_materiel/urls.py
from django.contrib import admin
from django.urls import path, include
from materiel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajouter_enseignant/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('ajouter_materiel/', views.ajouter_materiel, name='ajouter_materiel'),
    path('changer_possesseur/<int:materiel_id>/', views.changer_possesseur, name='changer_possesseur'),
    path('accounts/', include('django.contrib.auth.urls')),
]
