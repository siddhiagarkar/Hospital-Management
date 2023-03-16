from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'P_List':'/patient-list/',
		'D_List':'/doctor-list/',
		# 'Detail View':'/patient-detail/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def patientList(request):
	patient = PatientDetail.objects.all()
	serializer = PatientDetailSerializer(patient, many=True)
	return Response(serializer.data)

# @api_view(['GET'])
# def patientDetail(request, pk):
# 	patient = PatientDetail.objects.get(id=pk)
# 	serializer = PatientDetailSerializer(patient, many=False)
# 	return Response(serializer.data)

@api_view(['GET'])
def doctorList(request):
	doctor = DoctorDetail.objects.all()
	serializer = DoctorDetailSerializer(doctor, many=True)
	return Response(serializer.data)
