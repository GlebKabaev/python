# management/forms.py
from django import forms
from .models import Doctor, Ward, Patient

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'major']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WardForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'id_ward', 'id_doc']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_ward': forms.Select(attrs={'class': 'form-control'}),
            'id_doc': forms.Select(attrs={'class': 'form-control'}),
        }
