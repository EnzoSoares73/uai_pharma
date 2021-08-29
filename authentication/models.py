from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^[^±!@£$%^&*0-9_+§¡€#¢§¶•ªº«\\/<>?:;|=.,]{1,20}$"
    message = (
        'Insira um nome válido.'
    )
    flags = 0

class regexTelefone(validators.RegexValidator):
    regex = r'^\s*(\d{2}|\d{0})[-. ]?(\d{5}|\d{4})[-. ]?(\d{4})[-. ]?\s*$'
    message = (
        'Insira um telefone válido.'
    )
    flags = 0

class regexAlfabetico(validators.RegexValidator):
    regex = '/^[A-Z]+$/i'
    message = (
        'Insira um valor válido.'
    )
    flags = 0

class User(AbstractUser):
    validador_telefone = regexTelefone()
    validador_nome = UnicodeUsernameValidator()
    first_name = models.CharField('Primeiro nome', validators=[validador_nome], max_length=150) #mask
    last_name = models.CharField('Sobrenome', max_length=150, validators=[validador_nome]) #mask
    username = None #mask
    email = models.EmailField(('Email'), blank=True, unique=True)
    telefone = models.CharField('Número de Telefone', validators=[validador_telefone], max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nome()

    def nome(self):
        return self.get_full_name()

class Endereco(models.Model):
    validador_alfabetico = regexAlfabetico()
    rua = models.CharField('Rua', validators=[validador_alfabetico], max_length=50)
    bairro = models.CharField('Bairro', validators=[validador_alfabetico], max_length=50)
    numero = models.IntegerField('Número')
    complemento = models.CharField('Complemento', validators=[validador_alfabetico], max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)