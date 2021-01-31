from django.shortcuts import render
from xlwings import view

from patientweb.models import Patient

def home(request):
    Data = {'Patients': Patient.objects.all()}
    return render(request, 'patient/list.html', Data)
#
# def view(request, id):
#     view = Patient.objects.get(id = id)
#     return render(request, 'patients/view.html', {'Patients': view})