from django.db import models

# Create your models here.
class MessageSended(models.Model):
    data = models.DateField()
    codigo = models.CharField(max_length=100)
    tipo = models.IntegerField()

    def __str__(self):
        return self.codigo