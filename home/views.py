# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def exibir_item(request, id):
    return render(request, 'id.html', {
        'section': 'id',
        'section_title': 'id',
        'id': id
    })

