from django.contrib import admin
from .models import Category, PatientDetail, DoctorDetail, ProblemAndSolution, Appointment, Bill

# Register your models here.

admin.site.register(Category)
admin.site.register(PatientDetail)
admin.site.register(DoctorDetail)

@admin.register(ProblemAndSolution)
class ProblemAndSolutionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'problem', 'solution')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment', 'created_on', 'amount', 'payment_status')
