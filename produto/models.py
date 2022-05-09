from django.db import models


class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto =models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('Estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque minimo', default=0)

    class Meta:
        ordering=('produto',)

    def __str__(self):
        return self.produto
