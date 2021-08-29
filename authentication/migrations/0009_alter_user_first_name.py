# Generated by Django 3.2.6 on 2021-08-29 01:19

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210828_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=150, validators=[authentication.models.UnicodeUsernameValidator()], verbose_name='Primeiro nome'),
        ),
    ]
