# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def exibir_item(request, id):
    return render(request, 'dashboard.html', {
        'section': 'exibir_item',
        'section_title': 'Exibir Item',
        'id': id
    })

def dia_semana(request, dia):
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    dia_nome = dias_semana.get(dia, "Dia inválido")
    return render(request, 'dashboard.html', {
        'section': 'dia_semana',
        'section_title': 'Dia da Semana',
        'dia': dia,
        'dia_nome': dia_nome
    })