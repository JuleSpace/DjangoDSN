from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materiel/', include('materiel.urls')),  # Include the URLs from the 'materiel' app
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
]
