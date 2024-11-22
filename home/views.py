from django.shortcuts import render, redirect
from .forms import ContatoForm
from .models import Produto  # Certifique-se de que o modelo Produto existe

def index(request):
    return render(request, 'base.html')

def exibir_item(request, id):
    return render(request, 'id.html', {'id': id})

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
    return render(request, 'dia_semana.html', {'dia': dia, 'dia_nome': dia_nome})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Aqui você pode salvar os dados ou enviar um email, por exemplo
            return redirect('index')  # Redireciona após o envio
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})

def home(request):
    context = {
        'username': 'Carlos',
        'items': ['Lápis', 'Caneta', 'Borracha'],
        'welcome_message': 'Bem-vindo ao Dashboard!',
    }
    return render(request, 'home.html', context)


def produtos(request):
    lista_produtos = Produto.objects.all()  # Obtém todos os produtos do banco
    return render(request, 'produto/lista.html', {'lista': lista_produtos})

def excluir_produto(request, id):
    try:
        produto = Produto.objects.get(id=id)
        produto.delete()
    except Produto.DoesNotExist:
        pass  # Ou redirecione para uma página de erro
    return redirect('produtos')
