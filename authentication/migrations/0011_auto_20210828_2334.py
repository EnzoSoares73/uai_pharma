# Generated by Django 3.2.6 on 2021-08-29 02:34

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20, validators=[authentication.models.UnicodeUsernameValidator()], verbose_name='Primeiro nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20, validators=[authentication.models.UnicodeUsernameValidator()], verbose_name='Sobrenome'),
        ),
    ]
