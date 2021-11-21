from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('put', views.put, name='put'),
    path('lucromensal', views.lucro, name='lucro'),
    path('skus', views.sku, name='skus'),
    path('funcionarios', views.funcionarios, name='funcionarios'),
]