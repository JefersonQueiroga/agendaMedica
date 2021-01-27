from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=25)
    dateBirth = models.DateField()
    adress=models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Paciente"