from django.shortcuts import render, redirect
from .models import Venda


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        price = request.POST.get('preço')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        film = Venda(title = title, content = content, price = price)
        film.save()
        return redirect('index')
    else:
        all_vendas = Venda.objects.all()
        return render(request, 'vendas/index.html', {'vendas': all_vendas})