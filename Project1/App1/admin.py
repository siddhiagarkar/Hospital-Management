from django.contrib import admin
from .models import Category, PatientDetail, DoctorDetail, ProblemAndSolution

# Register your models here.

admin.site.register(Category)
admin.site.register(PatientDetail)
admin.site.register(DoctorDetail)

@admin.register(ProblemAndSolution)
class ProblemAndSolutionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'problem', 'solution')
