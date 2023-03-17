from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'P_List':'/patient-list/',
		'D_List':'/doctor-list/',
		'ProblemSolution_List':'/problemsolution-list/',
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

@api_view(['GET'])
def problemsolutionList(request):
	data = ProblemAndSolution.objects.all()
	serializer = DoctorDetailSerializer(data, many=True)
	return Response(serializer.data)

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('store')
    else:
        print('USER NOT FOUND')

    context = {}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('store')
    # Redirect to a success page.

