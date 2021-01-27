from django.urls import path
from .views import PatientCreate,PatientList,PatientUpdate
urlpatterns = [
    path('paciente/novoPaciente',PatientCreate.as_view(),name='addPatient'),
    path('paciente/listar', PatientList.as_view(), name='listPatient'),
    path('paciente/edit/<int:pk>/', PatientUpdate.as_view(), name='editPatient'),

]
