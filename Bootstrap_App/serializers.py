from rest_framework import  serializers
from .models import Doctors,Appointment,Patients

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'
class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        doctor = data['doctor']
        date = data['date']
        time = data['time']

        if Appointment.objects.filter(doctor=doctor, date=date, time=time).exists():
            raise serializers.ValidationError('Appointment already exists, Kindly book another time')
        return  data