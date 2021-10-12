from django.db import models

# Create your models here.


class Diarista(models.Model):
    nome_completo = models.CharField(max_length=256, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    logradouro = models.CharField(max_length=128, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=30, null=False, blank=False)
    complemento = models.CharField(max_length=96, null=False, blank=True)
    cep = models.CharField(max_length=9, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    codigo_ibge = models.IntegerField(null=False, blank=False)
    foto_usuario = models.ImageField(null=False)
