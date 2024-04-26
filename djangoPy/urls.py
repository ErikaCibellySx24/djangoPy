from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agenda.urls')),  # Inclui as URLs da aplicação agenda
]
