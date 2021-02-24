from django.urls import path
from django.conf.urls import include
from .views import PatientCreate,PatientList,PatientUpdate,PatientDelete
from rest_framework import routers
from .api.viewsets import PacienteViewSet

router = routers.DefaultRouter()
router.register('paciente', PacienteViewSet)

urlpatterns = [
    path('paciente/novoPaciente',PatientCreate.as_view(),name='addPatient'),
    path('paciente/listar', PatientList.as_view(), name='listPatient'),
    path('paciente/edit/<int:pk>/', PatientUpdate.as_view(), name='editPatient'),
    path('paciente/excluir/<int:pk>/', PatientDelete.as_view(), name='excluirPatient'),
    path('api/',include(router.urls)),

]
