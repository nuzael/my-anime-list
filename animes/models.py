from django.contrib.auth.models import User
from django.db import models


class Anime(models.Model):
    STATUS_CHOICES = (
        ('Assistir', 'Assistir'),
        ('Assistido', 'Assistido'),
        ('Assistindo', 'Assistindo'),
    )

    nome = models.CharField(max_length=255)
    temporada = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    comentarios = models.TextField(max_length=50, blank=True, verbose_name='Comentários')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome