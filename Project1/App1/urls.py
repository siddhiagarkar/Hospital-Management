from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
	path('patient-list/', views.patientList, name="patient-list"),
	# path('patient-detail/<str:pk>/', views.patientDetail, name="patient-detail"),
	path('doctor-list/', views.doctorList, name="doctor-list"),
	path('problemsolution-list/', views.problemsolutionList, name="problemsolution-list"),
]
