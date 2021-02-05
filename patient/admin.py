from django.contrib import admin
from .models import Paciente,Exame,Consulta,ConsultaExame


class PatientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone',)


class ConsultaExameInline(admin.TabularInline):
    model = ConsultaExame

class ConsultaAdmin(admin.ModelAdmin):
    inlines = (ConsultaExameInline,)

admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Paciente,PatientAdmin)
admin.site.register(Exame)


