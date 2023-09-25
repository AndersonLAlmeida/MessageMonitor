from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Adicione campos personalizados, se necessário
    # Exemplo: profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    #data_criacao = models.DateTimeField(default='2023-09-24')
    pass

class MessageSended(models.Model):
    data = models.DateField()
    codigo = models.CharField(max_length=100)
    tipo = models.IntegerField()

    def __str__(self):
        return self.codigo