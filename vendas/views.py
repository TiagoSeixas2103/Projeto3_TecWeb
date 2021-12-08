from django.shortcuts import render, redirect
from django.db.models import F, Sum
from .models import Venda, Produto


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        # TAREFA: Utilize o title e content para criar um novo Venda no banco de dados
        if Produto.objects.filter(name = product).exists():
            print('has')
            prod = Produto.objects.get(name = product)
        else:
            return redirect('erro')
        film = Venda.objects.create(title = title, quantity = quantity)
        film.product.add(prod.id)
        print(Venda.product)
        return redirect('index')
    else:
        all_vendas = Venda.objects.order_by('title')
        return render(request, 'vendas/index.html', {'vendas': all_vendas})

def delete_Vendas(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Venda.objects.filter(id=id).delete()
        return redirect('index')
    else:
        all_vendas = Venda.objects.order_by('title')
        return render(request, 'vendas/index.html', {'vendas': all_vendas})

def put(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        new_venda = Venda()
        new_venda.title = title
        new_venda.product = product
        new_venda.quantity = quantity
        new_venda.id = id
        new_venda.save()
        return redirect('index')
    else:
        all_vendas = Venda.objects.order_by('title')
        return render(request, 'vendas/index.html', {'vendas': all_vendas})

def lucro(request):
    lucros = {}
    total = 0
    lucros["Total"] = 0
    if Produto.objects.all() and Venda.objects.all():
        for prod in Produto.objects.all():
            quant = Venda.objects.filter(product = prod).values('quantity').aggregate(sum = Sum('quantity')).get('sum')
            total = total + prod.price * quant - prod.cost*quant
    lucros["Total"] = total

    return render(request, 'vendas/lucros.html', {'lucros': lucros})

def sku(request):
    skus = {}
    if Produto.objects.all():
        for prod in Produto.objects.all():
            if prod.name in skus.keys():
                pass
            else:
                if Venda.objects.all():
                    quant = Venda.objects.filter(product = prod).values("quantity").aggregate(sum = Sum('quantity')).get('sum')
                else:
                    quant = 0
                skus[prod.name] = { 'lucro' :prod.price * quant - prod.cost*quant, 'quantidade':quant}
    return render(request, 'vendas/skus.html', {'skus': skus})


def funcionarios(request):
    funcionarios = {}
    if Produto.objects.all() and Venda.objects.all():
        for func in Venda.objects.all():
            temp = 0
            if func.title in funcionarios.keys():
                pass
            else:
                for prod in Venda.objects.filter(title=func.title).values("product"):
                    preco = Produto.objects.filter(id = prod['product']).values("price")[0]['price']
                    custo = Produto.objects.filter(id = prod['product']).values("cost")[0]['cost']
                    quant = Venda.objects.filter(title=func.title, product = prod['product']).values("quantity").aggregate(sum = Sum('quantity')).get('sum')
                    temp = temp + preco*quant-custo*quant
                funcionarios[func.title] = temp
    return render(request, 'vendas/funcionarios.html', {'funcionarios': funcionarios})

def produtos(request):
    if request.method == 'POST':
        name = request.POST.get('nome')
        price = request.POST.get('preco')
        cost = request.POST.get('custo')
        film = Produto.objects.create(name = name, price = price, cost = cost)
        return redirect('produtos')
    else:
        all_produtos = Produto.objects.order_by('name')
        return render(request, 'vendas/produtos.html', {'produtos': all_produtos})

def delete_Produto(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Produto.objects.filter(id=id).delete()
        return redirect('produtos')
    else:
        all_produtos = Produto.objects.order_by('name')
        return render(request, 'vendas/produtos.html', {'produtos': all_produtos})

def erro(request):
    return render(request, 'vendas/erro.html')

def kpi(request):
    lucro = 0
    receita = 0
    if Produto.objects.all() and Venda.objects.all():
        for prod in Produto.objects.all():
            if Venda.objects.filter(product=prod).exists():
                quant = Venda.objects.filter(product = prod).values('quantity').aggregate(sum = Sum('quantity')).get('sum')
            else:
                quant = 0
            lucro = lucro + prod.price * quant - prod.cost*quant
            receita = receita + prod.price * quant
    
    skus = {}
    if Produto.objects.all():
        for prod in Produto.objects.all():
            if prod.name in skus.keys():
                pass
            else:
                if Venda.objects.filter(product=prod).exists():
                    quant = Venda.objects.filter(product = prod).values("quantity").aggregate(sum = Sum('quantity')).get('sum')
                else:
                    quant = 0
                skus[prod.name] = { 'lucro' :prod.price * quant - prod.cost*quant, 'receita':prod.price * quant}
    
    if receita > 0:
        lucratividade_operação = lucro/receita*100
    else:
        lucratividade_operação = 0
    if skus:
        lucratividade_produto = {}
        for prod, item in skus.items():
            if item['receita']> 0:
                lucratividade_produto[prod] = item['lucro']/item["receita"]*100
            else:
                lucratividade_produto[prod] = 0
    return render(request, 'vendas/kpi.html', {'lucratividade_operação': lucratividade_operação, 'lucratividade_produto': lucratividade_produto})

