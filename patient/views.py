from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from .models import Patient
from .forms import PatientForm
from django.contrib import messages


class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'patient/form.html'

    def get_context_data(self, **kwargs):
        data = super(PatientCreate, self).get_context_data(**kwargs)
        return data

    def get_success_url(self):
        return reverse_lazy('listPatient')


class PatientList(ListView):
    model = Patient
    context_object_name = 'list_patient'  # your own name for the list as a template variable
    template_name = 'patient/list.html'  # Specify your own template name/location

class PatientUpdate(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/update_form.html'
    success_url='/paciente/listar'

