from django.contrib import admin
from .models import Cliente, Agendamento

# Registrar os modelos no painel administrativo
admin.site.register(Cliente)
admin.site.register(Agendamento)
