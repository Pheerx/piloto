from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('exibir/<int:id>/', views.exibir_item, name='exibir_item'),  # Exibir Item
    path('dia/<int:dia>/', views.dia_semana, name='dia_semana'),  # Dia da Semana
    path('contato/', views.contato, name='contato'),  # Página de Contato
    path('produto/', views.produtos, name='produtos'),
    path('produtos/fomulario_produto/', views.produto, name='fomulario2'), 
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),     
]
]
