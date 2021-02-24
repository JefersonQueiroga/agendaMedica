from rest_framework import serializers
from patient.models import Paciente

class PacienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Paciente
        fields = ['id','nome','email', 'dataNascimento']