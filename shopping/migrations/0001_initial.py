# Generated by Django 3.2.6 on 2021-08-26 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shopping.models
import shopping.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=shopping.models.fixed_date)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('promocao', models.IntegerField(validators=[shopping.validators.validate_range], verbose_name='Valor da promoção')),
                ('em_estoque', models.BooleanField(verbose_name='Em estoque?')),
                ('ativado', models.BooleanField(verbose_name='Ativado?')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('prioridade', models.IntegerField(help_text='Prioridade da tag com relação às outras', validators=[shopping.validators.validate_range], verbose_name='Prioridade')),
                ('produto', models.ManyToManyField(to='shopping.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Item_carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.carrinho')),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='shopping.produto')),
            ],
        ),
    ]
