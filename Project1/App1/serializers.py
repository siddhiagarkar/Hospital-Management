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
		
class ProblemAndSolutionSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProblemAndSolution
		fields ='__all__'
		