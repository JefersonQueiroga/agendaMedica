from rest_framework import viewsets
from patient.models import Paciente
from .serializers import PacienteSerializer
from rest_framework.permissions import IsAuthenticated

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    permission_classes = (IsAuthenticated,)