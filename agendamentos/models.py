from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Modelo Agendamento
class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos')
    data = models.DateTimeField()
    servico = models.CharField(max_length=50, choices=[
        ('montagem_pc', 'Montagem de PC Gamer'),
        ('limpeza_pc', 'Limpeza de PC Gamer'),
        ('orcamento_basico', 'Orçamento Básico'),
        ('organizacao_setup', 'Organização de Setup'),
        ('consultoria_setup', 'Consultoria de Setup'),
        ('agendamento_empresarial', 'Agendamento Empresarial'),
    ])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico} - {self.status}"
