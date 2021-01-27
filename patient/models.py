from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=25)
    dateBirth = models.DateField(null=True, blank=True)
    adress=models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Paciente"


class Servidor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural="Servidores"

    def __str__(self):
        return '{}'.format(self.nome)
