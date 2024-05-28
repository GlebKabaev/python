# management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_ward/', views.add_ward, name='add_ward'),
]
