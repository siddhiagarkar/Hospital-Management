from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields ='__all__'
		
        
class PatientDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientDetail
		fields ='__all__'
		
class DoctorDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = DoctorDetail
		fields ='__all__'
		
class PatientProblemSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientProblem
		fields ='__all__'
		
class DoctorSolutionSerializer(serializers.ModelSerializer):
	class Meta:
		model = DoctorSolution
		fields ='__all__'
		
