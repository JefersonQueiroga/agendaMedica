from django.contrib import admin
from .models import Patient,Servidor


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone',)

admin.site.register(Patient,PatientAdmin)
admin.site.register(Servidor)
