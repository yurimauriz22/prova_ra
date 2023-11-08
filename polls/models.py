from django.db import models

# Create your models here.
class Carro(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField(default=0)
    imagem = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Aluguel(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

    def __str__(self):
        return self.carro.nome