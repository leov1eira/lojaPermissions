from django.conf import settings
from django.db import models

from .comentario import Comentario

class Produto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=False)
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='produtos', height_field=None, width_field=None, max_length=100)
    descricao = models.CharField(max_length=500)
    comentario = models.ForeignKey(Comentario, null=True, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()


    def __str__(self):
        return self.nome