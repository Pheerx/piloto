
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('exibir_item/<int:id>/', views.exibir_item, name="exibir_item"),
    path('dia_semana/<int:dia>/', views.dia_semana, name="dia_semana"),
]
