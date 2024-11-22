from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('exibir/<int:id>/', views.exibir_item, name='exibir_item'),
    path('dia/<int:dia>/', views.dia_semana, name='dia_semana'),
    path('contato/', views.contato, name='contato'),
    path('produto/', views.produtos, name='produtos'),
    path('produtos/fomulario_produto/', views.contato, name='fomulario2'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]
