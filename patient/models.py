from django.db import models
from datetime import datetime

class Paciente(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=25)
    dataNascimento = models.DateField(null=True, blank=True)
    endereco=models.CharField(max_length=250, null=True, blank=True)
    cidade = models.CharField(max_length=250, null=True,blank=True)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name="Paciente"

class Exame(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Consulta(models.Model):
    data = models.DateField(auto_now=True)
    anotacaoConsulta = models.TextField(verbose_name="Anotação da Consulta")
    dataRetorno = models.DateField(verbose_name="Data de Retorno")
    anotacaoRetorno = models.TextField()
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, related_name="consulta")
    exames = models.ManyToManyField(Exame,related_name="consulta",through="ConsultaExame")
    class Meta:
        verbose_name="Consulta"

    def __str__(self):
        return "{} - {}".format(self.date,self.patient.name)

    def save(self, *args, **kwargs):
        super(Consulta, self).save(*args, **kwargs)



class ConsultaExame(models.Model):
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE, related_name="consulta_exa")
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name="consulta_exa")
    resultado = models.TextField(max_length=250)


