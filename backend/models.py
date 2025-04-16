from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SETOR_CHOICES = (
        ("administrativo", "Administrativo"),
        ("comunicacao", "Comunicação"),
        ("marketing", "Marketing"),
    )

    CARGO_CHOICES = (
        ("colaborador", "Colaborador"),
        ("diretor", "Diretor"),
        ("presidente", "Presidente"),
    )

    setor = models.CharField(max_length=20, choices=SETOR_CHOICES, default="administrativo")
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES, default="colaborador")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.setor} - {self.cargo}"


class Relatorio(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    titulo_modificado = models.CharField(max_length=50, blank=True)

    descricao = models.TextField(null=True)
    descricao_modificada = models.TextField(blank=True)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    hora = models.IntegerField(default=0, null=True)
    hora_modificada = models.IntegerField(default=0)

    colaborador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    setor = models.CharField(max_length=20, choices=User.SETOR_CHOICES, default="administrativo", null=True)
    diretor = models.ForeignKey(User, related_name='relatorios_diretor', on_delete=models.CASCADE, null=True)

    aprovado_direroria = models.BooleanField(default=False)
    aprovado_presidencia = models.BooleanField(default=False)

