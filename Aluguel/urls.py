from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buttons', views.buttons, name='buttons'),
    path('login', views.login, name='login'),
    path('registro-usuario', views.registro_usuario, name='registro-usuario'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('blank', views.blank, name='blank'),
    path('cards', views.cards, name='cards'),
    path('charts', views.charts, name='charts'),
    path('page-error', views.page_error, name='page-error'),
    path('cliente', views.cliente, name='cliente'),
    path('base', views.base, name='base'),
    path('registro-clientes', views.registro_clientes, name='registro-clientes'),
    path('registro-carros', views.registro_carros, name='registro-carros'),
    path('registro-aluguel/<id_cliente>', views.registro_aluguel, name='registro-aluguel'),
    path('lista-alugueis', views.lista_alugueis, name='lista-alugueis'),
    path('excluir/<id_aluguel>', views.excluir_aluguel, name='excluir'),
    path('excluir-clientes/<id_cliente>', views.excluir_clientes, name='excluir-clientes'),
    path('excluir-carros/<id_carro>', views.excluir_carros, name='excluir-carros'),
    path('editar-clientes/<id_cliente>', views.editar_clientes, name='editar-clientes'),
    path('editar-carros/<id_carro>', views.editar_carros, name='editar-carros'),
    path('lista-carros', views.lista_carros, name='lista-carros'),
]
