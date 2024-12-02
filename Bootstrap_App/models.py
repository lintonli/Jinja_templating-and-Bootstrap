from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

class Doctors(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return  self.user.username
class Patients(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    years = models.IntegerField()
    profession = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    mobile=models.IntegerField()
    def __str__(self):
        return self.date
