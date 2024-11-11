from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


from django.shortcuts import render


def exibir_item(request, id):
    return render(request, 'id.html', {
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
    return render(request, 'dia_semana.html', {
        'dia': dia,
        'dia_nome': dia_nome
    })
