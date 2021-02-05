from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Paciente
from .forms import PatientForm
from django.contrib import messages


class PatientCreate(CreateView):
    model = Paciente
    fields = '__all__'
    template_name = 'patient/form.html'

    def get_context_data(self, **kwargs):
        data = super(PatientCreate, self).get_context_data(**kwargs)
        return data

    def get_success_url(self):
        return reverse_lazy('listPatient')


class PatientList(ListView):
    model = Paciente
    context_object_name = 'list_patient'  # your own name for the list as a template variable
    template_name = 'patient/list.html'  # Specify your own template name/location

class PatientUpdate(UpdateView):
    ## implementacao da regra de negocio
    model = Paciente
    form_class = PatientForm
    template_name = 'patient/form.html'
    success_url='/paciente/listar'


class PatientDelete(DeleteView):
    model = Paciente
    success_url=reverse_lazy('listPatient')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


