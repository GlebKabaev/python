from django.contrib import admin
from .models import Doctor, Ward, Patient

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'major')
    search_fields = ('name', 'major')

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity')
    search_fields = ('quantity',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_ward', 'id_doc')
    search_fields = ('name',)
    list_filter = ('id_ward', 'id_doc')
