from django.contrib import admin
from .models import Category, PatientDetail, DoctorDetail, PatientProblem, DoctorSolution

# Register your models here.

admin.site.register(Category)
admin.site.register(PatientDetail)
admin.site.register(DoctorDetail)

@admin.register(PatientProblem)
class PatientProblemAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'your_choice')

@admin.register(DoctorSolution)
class DoctorSolutionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'problem', 'solution')
