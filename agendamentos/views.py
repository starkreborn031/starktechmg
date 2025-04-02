from django.shortcuts import render
from .models import Agendamento 

def homepage(request):
    return render(request, 'agendamentos/index.html')

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()  
    return render(request, 'agendamentos/index.html', {'agendamentos': agendamentos})

'''
from django.shortcuts import render
from .models import Agendamento

# View para listar todos os agendamentos
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()  
    return render(request, 'agendamentos/listar_agendamentos.html', {'agendamentos': agendamentos})
'''