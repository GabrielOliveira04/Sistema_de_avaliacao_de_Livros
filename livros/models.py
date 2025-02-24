from django.db import models


class Categorias(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Livros(models.Model):
    streaming_choices = (('AK', 'Amazon Kindle'), ('F', 'Físico'))
    nome = models.CharField(max_length=50)
    streaming = models.CharField(max_length=2, choices=streaming_choices)
    nota = models.IntegerField(null=True, blank=True)
    categoria = models.ManyToManyField(Categorias)    

    def __str__(self):
        return self.nome