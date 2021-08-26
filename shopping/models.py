from datetime import datetime, timezone, timedelta

from django.db import models

from authentication.models import User
from shopping import validators

def fixed_date():
    return datetime.now(timezone(timedelta(hours=-3)))

class Tag(models.Model):
    nome = models.CharField("Nome", max_length=50)
    prioridade = models.IntegerField("Prioridade", help_text="Prioridade da tag com relação às outras", validators=[validators.validate_range])

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=50)
    descricao = models.CharField("Descrição", max_length=200)
    preco = models.FloatField("Preço")
    promocao = models.IntegerField("Valor da promoção (%)", validators=[validators.validate_range])
    tags = models.ManyToManyField(Tag)
    em_estoque = models.BooleanField("Em estoque?")
    ativado = models.BooleanField("Ativado?")

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(default=fixed_date)

class Item_carrinho(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.PROTECT)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
