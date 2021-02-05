
from django.forms import ModelForm
from .models import Paciente

class PatientForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


