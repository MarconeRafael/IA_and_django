from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agente/', include('agente.urls')),  # Rota para o app "agente"
    path('', lambda request: redirect('agente/', permanent=True)),  # Redireciona para "agente/"
]
