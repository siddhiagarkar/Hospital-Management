from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

class PatientDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=True)
    patient_fullname = models.CharField(max_length=100, default=True)
    age = models.PositiveIntegerField()
    contact = models.PositiveIntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class DoctorDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    doc_fullname = models.CharField(max_length=100, default=True)
    specialization = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    experience = models.PositiveIntegerField()
    reg = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Dr. "+ self.doc_fullname

class Appointment(models.Model):
    patient = models.ForeignKey(PatientDetail, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


class ProblemAndSolution(models.Model):
    patient = models.ForeignKey(PatientDetail, on_delete=models.CASCADE, default=True)
    doctor = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE, default=True)
    problem = models.CharField(max_length=400, default=True)
    solution = models.CharField(max_length=400, default=False)

class Bill(models.Model):
    patient = models.ForeignKey(PatientDetail, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    payment_status_choices = [
        ('SUCCESS', 'SUCCESS'),
        ('FAILURE', 'FAILURE'),
        ('PENDING', 'PENDING')]
    payment_status = models.CharField(max_length=10, choices=payment_status_choices, default='PENDING')

    def __str__(self):
        return f'{self.patient} {self.created_on}'
