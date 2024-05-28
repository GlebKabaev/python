# management/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Ward, Patient
from .forms import DoctorForm, WardForm, PatientForm

def index(request):
    patients = Patient.objects.all()
    return render(request, 'management/index.html', {'patients': patients})

def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DoctorForm()
    return render(request, 'management/add_doctor.html', {'form': form})

def add_ward(request):
    if request.method == "POST":
        form = WardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WardForm()
    return render(request, 'management/add_ward.html', {'form': form})

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PatientForm()
    return render(request, 'management/add_patient.html', {'form': form})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'management/patient_detail.html', {'patient': patient})
