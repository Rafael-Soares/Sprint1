from django.db import models
from datetime import datetime

class QuemSomos(models.Model):
    descricao = models.TextField('Descrição', blank=True)
    valores = models.TextField('Valores', blank=True)
    missao = models.TextField('Missão', blank=True)
    visao = models.TextField('Visão', blank=True)

