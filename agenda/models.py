from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'agenda'
