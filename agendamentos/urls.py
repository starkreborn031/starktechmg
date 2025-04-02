from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
]

'''
urlpatterns = [
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
]
'''