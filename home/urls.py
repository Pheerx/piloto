from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contato/', views.index, name="entre_em_contato"),
    path('Sobre/', views.index, name="Sobre"),
]
