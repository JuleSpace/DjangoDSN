from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materiel/', include('materiel.urls')),  # Inclure les URLs de l'application 'materiel'
    path('accounts/', include('django.contrib.auth.urls')),  # URLs pour l'authentification
]
