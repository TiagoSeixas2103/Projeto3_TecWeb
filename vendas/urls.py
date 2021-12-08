from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.index, name='index'),
    path('delete_Vendas', views.delete_Vendas, name='delete_Vendas'),
    path('put', views.put, name='put'),
    path('lucromensal', views.lucro, name='lucro'),
    path('skus', views.sku, name='skus'),
    path('funcionarios', views.funcionarios, name='funcionarios'),
    path('produtos', views.produtos, name='produtos'),
    path('delete_Produto', views.delete_Produto, name='delete_Produto'),
    path('erro', views.erro, name='erro'),
    path('kpi', views.kpi, name='kpi')]
