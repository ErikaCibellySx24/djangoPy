from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('listar/', views.listar_contatos, name='listar_contatos'),
    path('adicionar/', views.adicionar_contato, name='adicionar_contato'),
    path('editar/<str:nome>/', views.editar_contato, name='editar_contato'),
    path('excluir/<str:nome>/', views.excluir_contato, name='excluir_contato'),
]


