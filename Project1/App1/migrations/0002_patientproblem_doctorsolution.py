# Generated by Django 4.1.7 on 2023-03-16 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=300)),
                ('doc_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.doctordetail')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('your_choice', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='App1.category')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(default=False, max_length=400)),
                ('doctor', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='App1.doctordetail')),
                ('patient', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='App1.patientdetail')),
                ('problem', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='App1.patientproblem')),
            ],
        ),
    ]
