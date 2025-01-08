from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.executar_processo, name='home'),  # Define "executar_processo" como rota base
    path('briefing/', views.briefing, name='briefing'),
    path('concluida/', views.missao_concluida, name='concluida'), 
]
