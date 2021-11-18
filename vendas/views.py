from django.shortcuts import render, redirect
from .models import Venda


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('content')
        price = request.POST.get('price')
        # TAREFA: Utilize o title e content para criar um novo Venda no banco de dados
        film = Venda(title = title, content = content, price = price)
        film.save()
        return redirect('index')
    else:
        all_vendas = Venda.objects.all()
        return render(request, 'vendas/index.html', {'vendas': all_vendas})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Venda.objects.filter(id=id).delete()
        return redirect('index')
    else:
        all_vendas = Venda.objects.all()
        return render(request, 'Vendas/index.html', {'vendas': all_vendas})

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('content')
        price = request.POST.get('price')
        new_venda = Venda()
        new_venda.title = title
        new_venda.content = content
        new_venda.price = price
        new_venda.id = id
        new_venda.save()
        return redirect('index')
    else:
        all_vendas = Venda.objects.all()
        return render(request, 'Vendas/index.html', {'vendas': all_vendas})